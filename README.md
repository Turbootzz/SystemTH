# SystemTH
 
 
 This is a fantastic System bot. It provides with essential commands that you need for your server.
 If you are going to use some of the code, provide any sort of credits to me, for example in the embeds or in the help page. Please be a decent person :)
 
 ## Installation
 
 Go to the projects directory:
 ```
 cd your-bot-source
 ```

 Create a Virtual Enviromment
 Windows:
 ```
 SystemTH\Scripts\activate.bat
 ```
 Linux/Mac:
 ```
 source SystemTH/bin/activate
 ```

 Install packages
 ```
 pip install wheel
 pip install requirements.txt
 pip install youtube-dl
 ```

 Create a file called config.json
 
 Paste this in the file:
 ```
{
    "token": "",
    "reddit_username": "",
    "reddit_password": "",
    "reddit_client_id": "",
    "reddit_client_secret": ""
}
 ```
 Put your bot token in here and optionally your reddit credentials so you are able to use meme commands or pull images.

 <b>Sounds to play [Optionally]</b>
 Create a folder called sounds
 
 Paste your sounds in mp3 format and use the .playsound command and change the code in the fun.py

 ## Commands
 To see all the commands type:
 ```
 .help (page number)
 ```
 It's still in beta, so there will be more commands and features added in the future! The list below are some commands you can try. For the whole list type .help [as shown above].

 <b>Basic commands: </b>
 ```
 .ping
 .vote
 .website
 .predict [predicts the future] 
 ```
 <b>Fun commands: [Not working since migration.. Work in progress]</b>
 ```
 .meme [pulls a meme from reddit] reddit credentials required
 .foodporn [pulls a reddit picture of some delicious food :)] reddit credentials required
 .sounds [shows a list of sounds you can play]
 .playsound (sound)
 ```
 <b>Music commands: [Not working since discord banned playing music from bots.. Work in progress]</b>
 ```
 .play (YouTube URL)
 .stop 
 .volume (number)
 ```
 Add the bot to your server: [Click here](https://top.gg/bot/653220332454412288)\
 \
 
 Thanks :)
