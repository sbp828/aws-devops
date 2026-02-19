## Linux Basics

* `pwd` → Shows current working directory
* `ls` → Lists files and folders
* `ls -l` → Lists files with permissions, owner, size
* `ls -a` → Shows hidden files
* `cd /path` → Changes directory
* `cd ..` → Moves one level up
* `clear` → Clears terminal screen
* `whoami` → Shows current logged-in user
* `hostname` → Shows system hostname
* `date` → Displays current date & time
* `cal` → Shows calendar
* `man ls` → Opens manual for command
* `history` → Shows previously executed commands

---

## Linux File System

* `ls /` → Lists root directories
* `tree` → Displays directory structure as tree
* `find / -name file.txt` → Searches file in filesystem
* `locate file.txt` → Quickly finds file using index
* `stat file.txt` → Shows file metadata
* `df -h` → Shows disk space usage
* `du -sh folder` → Shows folder size
* `mount` → Shows mounted filesystems
* `umount /mnt` → Unmounts filesystem

---

## Linux Permissions

* `ls -l` → Shows file permissions
* `chmod 777 file.txt` → Gives full permissions
* `chmod 755 script.sh` → Common permission for scripts
* `chmod u+x file.sh` → Adds execute permission to user
* `chown user file.txt` → Changes file owner
* `chown user:group file.txt` → Changes owner & group
* `getfacl file.txt` → Shows ACL permissions
* `setfacl -m u:user:rwx file.txt` → Grants ACL permission

---

## Linux Users and Groups

* `who` → Shows logged-in users
* `w` → Shows user activity
* `id` → Shows UID, GID, groups
* `useradd username` → Creates new user
* `passwd username` → Sets user password
* `usermod -aG group user` → Adds user to group
* `userdel username` → Deletes user
* `groupadd groupname` → Creates group
* `groups username` → Shows user groups
* `su - username` → Switches user

---

## Linux Networking

* `ip a` → Shows network interfaces
* `ip r` → Shows routing table
* `ifconfig` → Displays network configuration
* `ping google.com` → Tests network connectivity
* `netstat -tulnp` → Shows open ports & services
* `ss -tulnp` → Modern alternative to netstat
* `curl url` → Sends HTTP request
* `wget url` → Downloads file
* `nslookup google.com` → DNS lookup
* `traceroute google.com` → Traces network path

---

## Linux Process Management

* `ps` → Shows running processes
* `ps -ef` → Shows all processes
* `top` → Real-time process monitoring
* `htop` → Interactive process viewer
* `uptime` → Shows system running time
* `kill PID` → Stops process
* `kill -9 PID` → Force kills process
* `pkill process` → Kills process by name
* `bg` → Resumes job in background
* `fg` → Brings job to foreground
* `jobs` → Lists background jobs

---

## Linux Disk Management

* `lsblk` → Lists disk partitions
* `blkid` → Shows UUIDs of disks
* `df -h` → Shows disk usage
* `du -h` → Shows directory size
* `mount /dev/sdb1 /mnt` → Mounts disk
* `umount /mnt` → Unmounts disk
* `fdisk -l` → Lists disk partitions
* `mkfs.ext4 /dev/sdb1` → Formats disk
* `fsck /dev/sdb1` → Checks filesystem

---

## Linux System Monitoring

* `top` → CPU & memory usage
* `htop` → Advanced monitoring
* `free -m` → Memory usage
* `vmstat` → Memory & CPU stats
* `iostat` → Disk I/O stats
* `mpstat` → CPU stats
* `uptime` → Load average
* `dmesg` → Kernel logs
* `journalctl` → System logs
* `journalctl -xe` → Error logs

---

## Linux Shell Scripting

* `#!/bin/bash` → Script interpreter
* `echo "Hello"` → Prints output
* `read name` → Takes user input
* `if [ condition ]` → Conditional logic
* `for i in {1..5}` → Loop execution
* `while true` → Infinite loop
* `case $var in` → Multiple conditions
* `grep "text" file` → Searches text
* `awk '{print $1}' file` → Processes columns
* `sed 's/old/new/' file` → Replaces text

---

## Linux Cron Jobs

* `crontab -e` → Edit cron jobs
* `crontab -l` → List cron jobs
* `crontab -r` → Remove cron jobs
* `systemctl status cron` → Check cron service
* `systemctl restart cron` → Restart cron service

---



## linux-shell-advanced
- Example commands for **linux-shell-advanced**
- (Add real commands here later)
