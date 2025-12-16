

## Linux Basics
Linux POC 1: Linux as a Server
## Objective
Run an app securely with a dedicated user and proper permissions.
## Steps
```bash
# Check current user
pwd
whoami

# Create app user & directory
sudo useradd appuser
sudo mkdir -p /opt/app
sudo chown -R appuser:appuser /opt/app
sudo chmod 755 /opt/app

# Switch user and create app
su - appuser
cd /opt/app
echo -e '#!/bin/bash\necho "App started"\ndate >> app.log' > app.sh
chmod +x app.sh
./app.sh
cat app.log
```
## Linux File System
- Proof of concept ideas for **Linux File System**
- (Scripts / configs later)


## Linux Permissions
- Proof of concept ideas for **Linux Permissions**
- (Scripts / configs later)


## Linux Users and Groups
- Proof of concept ideas for **Linux Users and Groups**
- (Scripts / configs later)


## Linux Networking
- Proof of concept ideas for **Linux Networking**
- (Scripts / configs later)


## Linux Process Management
Linux POC 2: Process & Port Understanding

## Objective
Understand processes, ports, and how apps run & listen.

## Steps
```bash
# Start simple server
cd /opt/app
python3 -m http.server 8080

# Check running process
ps aux | grep python

# Check port
ss -tulnp | grep 8080

# Stop server
pkill -f "python3 -m http.server"
```


## Linux Disk Management
- Proof of concept ideas for **Linux Disk Management**
- (Scripts / configs later)


## Linux System Monitoring
- Proof of concept ideas for **Linux System Monitoring**
- (Scripts / configs later)


## Linux Shell Scripting
- Proof of concept ideas for **Linux Shell Scripting**
- (Scripts / configs later)


## Linux Cron Jobs
- Proof of concept ideas for **Linux Cron Jobs**
- (Scripts / configs later)
