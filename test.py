import discord #discordでBOTを使うのにこれが必ずいる
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            return
            # メッセージを書きます
            m = "おはようございます" + message.author.nick + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
            
    if message.content.startswith("おやすみ"):
        if client.user != message.author:
            return
            m = "おやすみ！" + message.author.nick + "さん！"
            await message.channel.send(m)

# 実行
client.run(token)
