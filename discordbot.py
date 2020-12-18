from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pongg')

bot.run(token)

import discord #discordでBOTを使うのにこれが必ずいる

client = discord.Client()

@client.event #BOT起動時にCMDに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    print(message)
    if message.content == "おはよう":
    #:(コロン)を忘れずつけよう！Enterを押すと自動で改行されるよ！
        await client.send_message(message.channel, "Hello world!!")

# この＊＊＊に自分のトークンを書き替える
client.run(token)
