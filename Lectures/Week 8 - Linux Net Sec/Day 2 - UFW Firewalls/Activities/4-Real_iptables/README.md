# Real iptables

Before beginning please make sure to download the following file 
- [rules.tar](./rules.tar)

## Instructions
- Extract the provided archive with: `tar xvf rules.tar`.

- Inspect `default.rules` and answer the following:
  - How many rule entries are registered on the firewall?
      - **Hint**: Just count lines with `wc`.
  - These are the iptable rules UFW sets _by default_—before you set anything yourself. Do these rules block/allow packets?

- Inspect `apache.full.rules`. These rules are designed to allow access to an Apache web server.
  - Which ports do you expect to be open?
  - Find the rules providing/denying access to these ports.
  - Do the iptables rules have built-in protections against users who make a large number of requests?

- Inspect `openssh.rules` and answer the following:
  - Which ports do you expect to opened?
  - Find the rules corresponding to these ports.
  - Explain the rule(s) in detail. I.e., explain each flag. Use the output of `iptables --help`, as well as the documentation at: http://ipset.netfilter.org/iptables.man.html
