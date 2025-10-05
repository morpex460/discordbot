import discord
from discord.ext import commands

TOKEN = "MTQxNzE3NTg1Njg3NDUyNDY3Mg.G2ULnn.TD9Y4UPXTp-omWsImImiKo3rPlzkA-_mAqtBAY"  # ⚠️ Никогда не храни его в коде публично!
NUMBER_OF_INVITES = 5

# включаем доступ к содержимому сообщений
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# ✅ Теперь команда работает только для админов
@bot.command()
@commands.has_permissions(administrator=True)
async def invite(ctx, amount: int = NUMBER_OF_INVITES):
    """Создаёт несколько одноразовых бессрочных инвайтов"""
    invites = []
    for i in range(amount):
        invite = await ctx.channel.create_invite(
            max_age=0,     # бессрочно
            max_uses=1,    # только 1 использование
            unique=True
        )
        invites.append(invite.url)

    await ctx.send("🎟 Сгенерированные приглашения:\n" + "\n".join(invites))

# ⚠️ Обработчик ошибки, если кто-то без прав попробует вызвать команду
@invite.error
async def invite_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nope")

bot.run(TOKEN)
