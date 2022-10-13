"""
Usage:
A sample to send telegram message from a bot.


There is a TgBotConfig.ini file containing the token and your id.
The Ini file content:
[bot]
MYTOKEN = [your__token]
MYID = [your__id]


Possible problems:
if your__token is not correct:
message will be shown: 'telegram bot is not defined'

if your__id is not correct:
message will be shown: 'Error: Chat not found'


User-defined variables:
message_sent_by_bot
"""
from lib.botlib import SendBotMessage

def main():
    try:
        #User-defined variables
        message_sent_by_bot = "hello, I am bot."

        #Send the message from bot to you.
        SendBotMessage(message_sent_by_bot)

    except Exception as e:
        print('Error:',e)    
    finally:
        print('End of program.')    


if __name__ == '__main__':
    main()
