#!/usr/bin/env bash

LOG="./fix_web_vulns.error.$(date +%s).log"
function log() {
  echo "$1 $(date) | $2" | tee > $LOG
}

if [[ "$EUID" -ne 0 ]]; then 
  ERROR="Please run with sudo."
  echo $ERROR
  log "[-]" $ERROR
  exit 128
fi

# Pull new Docker Containers
log "[+]" "Pulling docker containers..."
docker pull cyberxsecurity/dvwa
docker pull cyberxsecurity/hackazon

#####################################
# REWRITE START_DVWA/HACKAZON SCRIPTS
#####################################
LOCAL="/usr/local/bin"
log "[+]" "Creating $LOCAL/start_dvwa..."
cat << EOF > /usr/local/bin/start_dvwa
#!/usr/bin/env bash
docker run --rm -p 8001:80 -d cyberxsecurity/dvwa
EOF
log "[+]" "$LOCAL/start_dvwa created successfully."

log "[+]" "Creating $LOCAL/start_hackazon..."
cat << EOF > /usr/local/bin/start_hackazon
#!/usr/bin/env bash
docker run --rm -p 8002:80 -d cyberxsecurity/hackazon
EOF
log "[+]" "$LOCAL/start_hackazon created successfully."

# Set execute permissions
log "[+]" "Adding execute privileges to $LOCAL/start_dvwa and $LOCAL/start_hackazon..."
chmod +x /usr/local/bin/start_dvwa
chmod +x /usr/local/bin/start_hackazon
log "[+]" "Execute permissions set successfully."

###############
# INSTALL NGINX
###############
log "[+]" "Installing nginx..."

apt remove apache2 -y && apt autoremove --purge apache2 -y
apt update -y && apt install -y nginx
systemctl stop nginx > /dev/null 2>&1

#################
# CONFIGURE NGINX
#################
SITES_ENABLED="/etc/nginx/sites-enabled"

NGINX_CONF_J2_URL="https://tinyurl.com/y3lmutcg"
HOSTS_URL="https://tinyurl.com/yxc9jobq"
DEFAULT="default"

log "[+]" "Pulling hosts to /etc/hosts..."
curl -L -o /etc/hosts $HOSTS_URL
if [[ $? -ne 0 ]]; then
  log "[-]" "Error pulling hosts"
  log "[-]" "Please read $LOG for details."
fi

log "[+]" "Removing and re-creating empty /etc/nginx/sites-enabled/default..."
DEFAULT_PATH="$SITES_ENABLED/$DEFAULT"
rm $DEFAULT_PATH > /dev/null 2>&1
touch $DEFAULT_PATH

log "[+]" "Pulling nginx.conf.j2 to /etc/nginx/sites-enabled/nginx.conf.j2..."
curl -L -o /etc/nginx/sites-enabled/nginx.conf.j2 $NGINX_CONF_J2_URL
if [[ $? -ne 0 ]]; then
  log "[-]" "Error pulling nginx.conf.j2."
  log "[-]" "Please read $LOG for details."
fi

##################
# RESTART SERVICES
##################
log "[+]" "Restarting nginx..."
systemctl restart nginx
if [[ $? -ne 0 ]]; then
  log "[-]" "Nginx could not be restarted."
  log "[-]" "Please run systemctl status nginx and read $LOG for details."
fi

log "[+]" "Starting DVWA and Hackazon..."
docker rm -vf $(docker ps -aq)
bash /usr/local/bin/start_dvwa
bash /usr/local/bin/start_hackazon
if [[ $? -ne 0 ]]; then
  log "[-]" "DVWA or Hackazon could not be restarted."
  log "[-]" "Please $LOG for details."
fi


if [[ $? -eq 0 ]]; then
  log "[+]" "Installation and configuration successfully completed."
else
  log "[-]" "Please show a TA your /tmp/$LOG."
  log "[-]" "Good luck!"
fi
