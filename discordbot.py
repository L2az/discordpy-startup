from discord.ext import commands
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']



import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    GLOBAL_CH_NAME = "🌸姉妹クラン募集" # グローバルチャットのチャンネル名
    GLOBAL_WEBHOOK_NAME = "hoge-webhook" # グローバルチャットのWebhook名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する
        await message.delete()

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        for channel in global_channels:
            ch_webhooks = await channel.webhooks()
            webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)

            if webhook is None:
                # そのチャンネルに hoge-webhook というWebhookは無かったので無視
                continue
            await webhook.send(content=message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url_as(format="png"))

client.run(token)


