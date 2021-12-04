import discord
from random import randint
from demoji import replace_with_desc
import asyncio
#from discord import activity
#from discord import activity
import markovify
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message): 
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response
        

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.write("")
        for guild in self.guilds:
            for channel in guild.text_channels:
                async for message in channel.history(limit=None):
                    if message.author != self.user and not message.author.bot:
                        with open('data.txt','a', encoding="utf-8") as file:
                            file.write(f"{message.content}\n")
        
        print("done")
        channel = MyClient.get_channel(self, 759370772665335843)
        while True:
            await channel.send("siema")
            await asyncio.sleep(259200)
        #with open("data/data.txt", "w") as



    async def on_message(self, message):
        if message.author != self.user and not message.author.bot:
            with open('data.txt','a', encoding="utf-8") as file:
                file.write(f"{message.content}\n")
            text = message.content.lower()
            if 'dejw' in text or self.user.mentioned_in(message):
                randomizer = randint(1,2)
                
                if randomizer == 1:
                    async with message.channel.typing():
                        text = replace_with_desc(text)
                        if '>' or '<' in text in text:
                            text = text.replace('<', '')
                            text = text.replace('>', '')
                        reponse = get_response(text)
                    await message.reply(f"{reponse}", mention_author=True)
                else:
                    async with message.channel.typing():
                        with open('data.txt','r', encoding="utf-8") as f:
                            text1 = f.read()
                        text_model = markovify.Text(text1, state_size=3)
                    await message.reply(f"{text_model.make_short_sentence(280, 2, tries=100)}", mention_author=True)

client = MyClient()
client.run('YOUR BOT TOKEN')
