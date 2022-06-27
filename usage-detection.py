#Created by Blake McCullough
#Discord - Spoiled_Kitten#4911
#Discord Server - https://discord.gg/X25F6Sfpq7
#Github - https://github.com/Blake-McCullough/
#Website - https://blakemccullough.com/
#Email - privblakemccullough@protonmail.com
#Twitch - https://www.twitch.tv/spoiled_kitten_

#Required imports,
#Use `pip install discord-webhook` in order to install the required webhook package.
import os, time
from discord_webhook import DiscordWebhook
from datetime import datetime


#The url by following the tutorial `https://progr.interplanety.org/en/how-to-get-the-discord-channel-webhook-url/`
webhookURL = 'WEBHOOK_URL_HERE'

#The ID for the user/role that you wish to be notified on critical alerts.
notifyID = "ID_HERE"


#Gets the cpu's usage and returns the string amount.
def getCPUuse():
    return float(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

def run():
    
    #Loops.
    while True:
        try:
            #Adding delay to avoid spam/causing issues.
            time.sleep(5)
            #Gets the cpu usage.
            use = getCPUuse()
            #For debugging.
            print(str(use))
            #Gets the current time.
            now = datetime.now()
            nowTime = now.strftime("%d/%m/%Y %H:%M:%S")
            #Checking if the value is above allowed.
            if use >= 90:
                #Sends webhook message.
                webhook = DiscordWebhook(url=webhookURL, content=f'**{nowTime}** - __**EMERGENCY:**__ <@{notifyID}> Above 90% utilisation!!!')
                response = webhook.execute()
            elif use >= 75:
                #Sends webhook message.
                webhook = DiscordWebhook(url=webhookURL, content=f'**{nowTime}** - __**WARNING:**__ Above 75% utilisation!!!')
                response = webhook.execute()
            elif use >= 50:
                #Sends webhook message.
                webhook = DiscordWebhook(url=webhookURL, content=f'**{nowTime}** - __**ALERT:**__ Above 50% utilisation!!!')
                response = webhook.execute()
        except:
            
            #On error will send another webhook.
            webhook = DiscordWebhook(url=webhookURL, content='The bot failed to get the usage!')
            response = webhook.execute()

#Prevents auto run.
if __name__ == "__main__":
    run()