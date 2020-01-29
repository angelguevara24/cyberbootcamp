cat << EOF > wrapper
#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
  echo "Please run as root."
  exit 127
fi

# Install nginx
apt update -y
apt install -y nginx

# Run install script
bash dependencies.sh
EOF

chmod +x wrapper
./wrapper
