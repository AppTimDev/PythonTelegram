# Usage
Create a simple library to use telegram bot.

---

# Telegram setup
## Create a new bot
1. Add 'BotFather' as a friend.
2. Type the command /newbot to him.
3. Choose a name for your bot
4. choose a username for your bot
5. Then a token [[your token]] will be given

## Find your id
1. Go to https://api.telegram.org/bot[[your token]]/getUpdates
2. A json result should be given and there is a field called 'id', and its value will be [[your__id]].

## Create a file called TgBotConfig.ini with the following contents
[bot]
MYTOKEN = [[your token]]
MYID =[[your__id]]

---

## Environment:
- Windows 10
- Python 3.10.4
- pip 22.2.2
- python-telegram-bot 13.14

---

## Installation
### Install pip and python-telegram-bot
```python
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade python-telegram-bot
``` 
or
```python
python -m pip install --upgrade pip
python -m pip install --upgrade python-telegram-bot
```

### If the codes do not work for the latest package, then try to install the specific version
```python
pip install python-telegram-bot==13.14
``` 

---

## Commands
### Check python version
```python
python -V
```

### Check pip version
```python
pip --version
```

### Check the version of the package
```python
pip show python-telegram-bot
```

### List all the installed package of python
```python
pip list
```

### Run the python script
```python
python tgbot.py
``` 

---

## Reference
1. https://core.telegram.org/bots/features#botfather
2. https://github.com/python-telegram-bot/python-telegram-bot