import discord
from discord.ext import commands

OWNER_ID = 969898192466485329  # 🔥 сюда вставь свой Discord ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Глобальная проверка: все команды теперь доступны только тебе
@bot.check
async def global_owner_check(ctx):
    return ctx.author.id == OWNER_ID

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} готов!")

# Нежно-красное сообщение
@bot.command(name="красный")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF7F7F  # нежный красный
    )
    embed.add_field(
        name="**❗️WHAT IS IN OUR DISCORD?❗️**",
        value="",
        inline=False
    )
    embed.add_field(
        name="**Before starting a conversation, be sure to read the information below!**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-красное сообщение
@bot.command(name="красный1")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF0000  # нежный красный
    )
    embed.add_field(
        name="**❗RULES THAT ARE MANDATORY FOR ABSOLUTELY ALL SERVER MEMBERS 👇🏼️**",
        value="",
        inline=False
    )
    embed.add_field(
        name="",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="красный2")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0xFF0000  # нежный зелёный
    )
    embed.add_field(
        name="**🚫 FORBIDDEN**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**1. Any insult towards any member of the server, regardless of the reason – Ban without warning**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**2. Political topics – Ban without warning**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**3. Any distribution of information about other courses, projects, leaked trainings, and anything similar – INSTANT BAN**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**4. Spamming is forbidden – 1 warning is given (Mute 1 hour), further – Ban**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**5. It is forbidden to send links / any files / programs, etc. – 1 warning is given (Mute 1 hour), further – Ban**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**❗️6. TAGGING AN ADMIN OR MODERATOR WITHOUT AN IMPORTANT REASON (Scam / Flood / Violation of rules, etc.) – Ban**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**7. Any action that may harm the project – Ban**",
        value="",
        inline=False
    )

    await ctx.send(embed=embed)

# Нежно-красное сообщение
@bot.command(name="красный3")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF7F7F  # нежный красный
    )
    embed.add_field(
        name="**HOW TO CHECK YOUR LEVEL?**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Go to the <#1417254932108673194> channel and enter:**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**/rank — to check your level**",
        value="",
        inline=False
    )
    embed.add_field(
        name="**/leaderboard — to view the leaderboard**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-красное сообщение
@bot.command(name="красный4")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF7F7F  # нежный красный
    )
    embed.add_field(
        name="**✅ YOU CAN GET FREE ACCESS TO THE PROP ACCOUNTS GROUP 👇🏼**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**TO DO THIS, YOU NEED TO REACH LEVEL 35 ON DISCORD.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**(Communication must be trading-related and beneficial to other members. Simple spam will not count — this will be monitored.)**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-красное сообщение
@bot.command(name="красный5")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF7F7F  # нежный красный
    )
    embed.add_field(
        name="**🔥 THE FREE VERSION IS JUST A PREVIEW**",
        value="",
        inline=False
    )
    embed.add_field(
        name="**With full access on our website, you’ll get:**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-красное сообщение
@bot.command(name="красный6")
async def krasnyi(ctx):
    embed = discord.Embed(
        color=0xFF0000  # нежный красный
    )
    embed.add_field(
        name="**❗️DOUBLE-CHECK THE USERNAME AND LINKS!❗️️**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="красный7")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # нежный зелёный
    )
    embed.add_field(
        name="**These are my ONLY OFFICIAL CONTACTS — everything else is a SCAM.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**The ONLY Discord username: yypstrade**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**The ONLY official website: https://www.yypstrade.com**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**YouTube: https://www.youtube.com/@yypstrade**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Telegram: https://t.me/yypstrade**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Main Group: https://discord.gg/wtrHgDXtrH**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Instagram: https://instagram.com/yypstrade**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Twitter (X): https://twitter.com/yypstrade**",
        value="",
        inline=False
    )

    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="зеленый")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x7FFF7F  # нежный зелёный
    )
    embed.add_field(
        name="**1. RULES**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Violating these rules will result in a ban on our server without warning.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**The rules in this channel - <#1417174828531843235>**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="зеленый1")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x7FFF7F  # нежный зелёный
    )
    embed.add_field(
        name="**2. ACTIVITY BONUSES**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**For being active on Discord, you can recieve**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**FULL ACCESS FOR FREE - <#1417244302228066345>**",
        value="",
        inline=False
    )
    embed.add_field(
        name="**Bonuses for activity - <#1417437191784894537>**",
        value="",
        inline=False
    )

    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="зеленый2")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x7FFF7F  # нежный зелёный
    )
    embed.add_field(
        name="**3. USEFUL RESOURCES**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**I have gathered all the useful resources for traders for you.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**FULL ACCESS FOR FREE - <#1417474258082467890>**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="зеленый3")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x7FFF7F  # нежный зелёный
    )
    embed.add_field(
        name="**WHAT ARE BONUSES GIVEN FOR?**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**- For any activity in chats, except spam.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**- For every boost to this chanel — 300 points.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**- For creating content that helps promote the project — bonus: 500 points.**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**- For a video on Instagram / TikTok / YouTube about the project that gains 10,000+ views — 1,500 points.**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Нежно-зелёное сообщение
@bot.command(name="зеленый4")
async def zelenyi(ctx):
    embed = discord.Embed(
        color=0x7FFF7F  # нежный зелёный
    )
    embed.add_field(
        name="**✅ FULL ACCESS TO ALL LESSONS AND MATERIALS**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**✅ IN-DEPTH BREAKDOWNS AND STRATEGIES**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**✅ AN EXCLUSIVE MEMBERS-ONLY COMMUNITY**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**✅ HIDDEN RULES ANALYSIS**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**✅ ACCESS TO THE MONITORING GROUP**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**AND MUCH MORE, ALL AVAILABLE ON THE WEBSITE**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)




# Синее сообщение
@bot.command(name="синий")
async def sinii(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # синий
    )
    embed.add_field(
        name="**BONUS FOR LEVEL 15**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Review of your trading plan and setups, with feedback on mistakes.**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Синее сообщение
@bot.command(name="синий1")
async def sinii(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # синий
    )
    embed.add_field(
        name="**BONUS FOR LEVEL 35**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**You get free access to the prop hack group.**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Синее сообщение
@bot.command(name="синий2")
async def sinii(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # синий
    )
    embed.add_field(
        name="**AFTER REACHING THIS LEVEL, CONTACT THE ADMIN OF THIS DISCORD**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**Discord - yypstrade**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Синее сообщение
@bot.command(name="синий3")
async def sinii(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # синий
    )
    embed.add_field(
        name="**👉 TO UNLOCK FULL ACCESS, SUBSCRIBE DIRECTLY ON THE WEBSITE**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**THE ONE AND ONLY LINK TO THE WEBSITE - https://www.yypstrade.com/**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

# Синее сообщение
@bot.command(name="синий4")
async def sinii(ctx):
    embed = discord.Embed(
        color=0x87CEFA  # синий
    )
    embed.add_field(
        name="**1️⃣ VISIT THE SITE TO LEARN EVERYTHING ABOUT THE GROUP – https://www.yypstrade.com/**",
        value="\u200b",
        inline=False
    )
    embed.add_field(
        name="**2️⃣ PAY FOR ACCESS USING ANY CURRENCY CONVENIENT FOR YOU (ONLY CRYPTO)**",
        value="",
        inline=False
    )
    embed.add_field(
        name="**3️⃣ AFTER PAYMENT, YOU WILL RECEIVE A ONE-TIME DISCORD LINK THAT WILL GRANT YOU ACCESS TO THE PRIVATE COMMUNITY.**",
        value="",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command(name="рес")
async def menu(ctx):
    embed = discord.Embed(title="Полезные ресурсы", description="Выбери нужный инструмент:")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Индикатор сессий", url="https://example.com"))
    view.add_item(discord.ui.Button(label="Календарь новостей", url="https://example.com"))
    view.add_item(discord.ui.Button(label="Калькулятор лота", url="https://example.com"))
    await ctx.send(embed=embed, view=view)


bot.run("MTQxNzE3NTg1Njg3NDUyNDY3Mg.GeK6fD.WOQmb_44bIgAWFvqgcRF0euW3SdHr0dfeEx2Eg")