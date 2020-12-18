from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pongg')

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content == "おはよう":
    #:(コロン)を忘れずつけよう！Enterを押すと自動で改行されるよ！
        await client.send_message(message.channel, "Hello world!!") 

bot.run(token)
client.run(token)
