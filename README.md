# nano

# installation

### install [python](https://python.org) and make sure to add it to your path

### download and extract nano's zip file found in this repository

### run install_modules.bat
----
# configuring

```json
{
    "token": "",
    "front": "nano:",
    "your_webhook": "1065899279312486420/6ZJXYZrL-Z3oqyyOnJ3vD6ZmEuxzNF4jikHGc44c0XWsp3hjTqE3YKq9k4MaCJ8XCIbJ",
    
    "delay": 0,

    "your_id": ,
    "channel": ,
    "victim": ,
    "guild_id": ,

    "invisible_ping": false,
    "discord": true,
    "alerts": true,
    
    "live_mode": false
}
```

## string values

### token - your discord auth key
### front - example: {"front": "byte:"} 
### byte: Sent: example

### your_webhook - used if 'alerts' is true, example format: 
##### {"your_webhook": "1065899279312486420/6ZJXYZrL-Z3oqyyOnJ3vD6ZmEuxzNF4jikHGc44c0XWsp3hjTqE3YKq9k4MaCJ8XCIbJ"}

## integer values

### delay - set delay for features measured in seconds, example:
#### {"delay": 0.1} = 100 milliseconds

### your_id - checks this ID for pings
### channel - used for sending messages to channels
### victim - ping someone with invis ping
### guild_id - not used yet

## boolean values

### invisible_ping - uses invisible pings when afk checking
### discord - enables/disables discord functionality, disable for speed
### alerts - send alerts to yourself using webhooks

### live_mode - insert your variables for your scripts inside the terminal rather than the settings file
---
# License

## Copyright 2023 [Byte](https://bytedev.cf)

#### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE