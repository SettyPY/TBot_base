# TBot_base
Telegram bot for managing a database in xlsx format.
This repository contains 2 bots and 1 xlsx file:

main.py - a bot for your users. in which they will be able to check their phone number for availability in the database.

edit.py - bot for adding data to the database (xlsx file)

## Don't judge me harshly I'm a beginner ^^

# **How to install?**

 ``` 
 pip install python-telegram-bot openpyxl termcolor
 git clone https://github.com/SettyPY/TBot_base.git
 ```
# **How to configure?**
open both files and change the TOKEN field to the token you received from Botfather.

also in the `edit.py` need to enter your id in the ALLOWED_IDS field

# **How to launch?**
```
python3 main.py # to launch a bot for users

python3 edit.py # to launch a bot for admins
```
