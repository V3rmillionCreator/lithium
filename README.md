<!DOCTYPE html>
<h1>Nano</h1>

<h3>Combined script of perpetual and carbon, contact me here: <a href="https://bytedev.cf/links/nano" target="__blank">Discord server</a> or byte#6110
</h3>

<h1>Installation</h1>

<h3>
1. Go to the official <a href="https://python.org">Python</a> website and download the latest version<br><br>
2. Run the installer, and make sure to add PIP/Python to your path<br><br>
3. After installing it is generally recommended that you restart your system<br><br>
4. Download Perpetual via the Github link by pressing the green "Code" button and press download zip<br><br>
5. Extract the .zip folder<br><br>

Inside is 1 folder which contain what you need to get setup
</h3>
<h1>Information</h1>
<h2>

'nano.py' - main script

'settings.json' - settings file

'wordlists' - grab words for packgen

'auto_pressure_lists' - grab words for auto pressure
</h2>

<h1>Configuring</h1>

<h2>
Inside your 'settings.json' file you should find this:

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

    "channel": 1064363544335892551,
    "server": 1057851883466793032,
    "user_id": 836938676881719387,
    "target": 836935511285170176,
    "rate_limit": 2,
    "delay": 0.2
}
```
</h2>
<h1>String values</h1>
<h2>

```json
{
    "token": "",
    "front": "➜ nano:",
    "send_front": "",
}
```
'token' - discord authentication key or 'token'. <br><br>

'front' - purely visual and will act like your terminal header for outputs.<br><br>

The 'send_front' - for when you want to show off to your friends, used in the Auto Pressure and Auto AFK Check features.<br><br>
</h2>
<h1>Boolean values (true/false)</h1>
<h2>

```json
{
    "dms": true,
    "server_check": false,
    "single_server": true,
    "rate_limiting": true,
    "fake_ping": true,
    "logs": true,
    "discord": true,
}
```
'dms' - check for incoming DMs.<br><br>

server_check' - cross-wide server checking. (This will significantly delay AFK Alert's performance.)<br><br>

'single_server' - when you only want to check 1 server.
</h2>
<h1>Integer Values</h1>
<h2>

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
'channel' - used in the Auto Pressure and Auto AFK Check features.<br><br>

'server' - for checking where you want to check for AFK checks.<br><br>

user_id' - used for when you want to be checked for if you get pinged.<br><br>

'rate_limit' - determine how long you want the Auto Pressure or Auto AFK Check features to retry sending a post request when you get ratelimited.<br><br>

'target' - used for ghostpinging with Auto AFK Check feature.<br><br>

'delay' - how fast you want features to execute<br><br>
</h2>

<h1>Features</h1>
<h2>
<li>AFK Alert</li>
<li>Auto Pressure</li>
<li>Auto AFK Check (custom unicode)</li>
<li>Topicgen</li>
<li>Packgen GUI</li>
</h2>

<h1>LICENSE</h1>
<h3>
This software is under a <a href="https://choosealicense.com/licenses/mit/">MIT License</a>, meaning you can change this code to however you like without my knowledge, this is free and open source as so it is yours to do with what you please, I would only ask that you wouldn't embed any malicious code alongside nano.
</h3>
