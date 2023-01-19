# Nano

### Combined script of perpetual and carbon, contact me here: [discord](https://bytedev.cf/links/nano) or byte#6110
---
# Installation

### 1. Go to the official [Python](https://python.org) website and download the latest version

### 2. Run the installer, and make sure to add PIP/Python to your path
### 3. After installing it is generally recommended that you restart your system
### 4. Download Perpetual via the Github link by pressing the green "Code" button and press download zip
### 5. Extract the .zip folder
### Inside is 1 folder which contain what you need to get setup
---
# Information

### 'nano.py' - main script.

### 'settings.json' - settings file.

### 'ascii.txt' - if custom_ascii is enabled this will be used for the ascii. it is by default an astronaut.

### 'topicgen.txt' - where the topicgen outputs.

### 'packs.txt' - where the default packgen outputs.

### 'wordlists' - grab words for packgen.

### 'wordlists_2' - grab words for auto pressure.

### 'ascii_archive' - ascii art that i used when testing ascii features, feel free to use.

# Configuring

## Inside your 'settings.json' file you should find this:


```json
{
    "token": "",
    "front": "➜ nano:",
    "send_front": "",
    
    "dms": true,
    "server_check": false,
    "single_server": true,
    "rate_limiting": true,
    "fake_ping": true,
    "logs": true,
    "discord": true,
    "custom_ascii": true,

    "channel": 1064363544335892551,
    "server": 1057851883466793032,
    "user_id": 836938676881719387,
    "target": 836935511285170176,
    "rate_limit": 2,
    "delay": 0.2
}
```

# String values(words/characters)

```json
{
    "token": "",
    "front": "➜ nano:",
    "send_front": "",
}
```

### 'token' - discord authentication key or 'token'.

### 'front' - purely visual and will act like your terminal header for outputs.

### 'send_front' - for when you want to show off to your friends, used in the Auto Pressure and Auto AFK Check features.

# Boolean values (true/false)

```json
{
    "dms": true,
    "server_check": false,
    "single_server": true,
    "rate_limiting": true,
    "fake_ping": true,
    "logs": true,
    "discord": true,
    "custom_ascii": true,
}
```

### 'dms' - check for incoming DMs.

### 'server_check' - cross-wide server checking. (This will significantly delay AFK Alert's performance.)

### 'single_server' - when you only want to check 1 server.

### 'rate_limiting' - enable or disable delay when you get ratelimited

### 'fake_ping' - fake pings the user when using the Auto AFK script.

### 'logs' - disable or enable logs (not enabled globally yet)

### 'discord' - whether you want to enable discord functionality (not enabled globally yet)

### 'custom_ascii' - uses custom ascii art instead of the default 'nano' ascii

# Integer Values (numbers)

```json
{
    "channel": 1064363544335892551,
    "server": 1057851883466793032,
    "user_id": 836938676881719387,
    "target": 836935511285170176,
    "rate_limit": 2,
    "delay": 0.2
}
```

### 'channel' - used in the Auto Pressure and Auto AFK Check features.

### 'server' - for checking where you want to check for AFK checks.

### 'user_id' - used for when you want to be checked for if you get pinged.

### 'rate_limit' - determine how long you want the Auto Pressure or Auto AFK Check features to retry sending a post request when you get ratelimited.

### 'target' - used for ghostpinging with Auto AFK Check feature.

### 'delay' - how fast you want features to execute

# Features
### Packgen
### AFK Alert
### Auto AFK Check (custom unicode)
### Topicgen
### Packgen GUI

# License

## This software is under a <a href="https://choosealicense.com/licenses/mit/">MIT License</a>, meaning you can change this code to however you like without my knowledge, this is free and open source as so it is yours to do with what you please, I would only ask that you wouldn't embed any malicious code alongside nano.
