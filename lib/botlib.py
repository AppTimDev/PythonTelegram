from configparser import ConfigParser
from telegram import Bot
'''
how to use
from lib.botlib import SendBotMessage

from lib.botlib import LoadTgBotConfig
MYTOKEN, MYID = LoadTgBotConfig()

from lib.botlib import MYTOKEN, MYID
'''
def LoadConfigFile(ini_filename):
    config = ConfigParser()
    config.read(ini_filename)
    return config


def LoadTgBotConfig(ini_filename='TgBotConfig.ini'):
    config = LoadConfigFile(ini_filename)
    MYTOKEN = config['bot']['MYTOKEN']
    MYID = config['bot']['MYID']
    return MYTOKEN, MYID


def SendBotMessage(message):
    if MYBOT is not None:
        MYBOT.send_message(chat_id = MYID, text = message)
    else:
        print('telegram bot is not defined')


try:
    #global variable
    MYTOKEN, MYID = LoadTgBotConfig()
    MYBOT = Bot(token=(MYTOKEN))

    #print('init botlib success')
except Exception as e:
    print('init botlib fail')
    MYTOKEN = MYID = MYBOT = None



