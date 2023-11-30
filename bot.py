import nextcord
from nextcord.ext import commands

@bot.command()
async def dev(ctx):
    embed = nextcord.Embed(
        title="Разработчики",
        description="Мы разрабатываем Leafy!\n[Сервер поддержки](https://discord.gg/eK9PQxQgHm)",
        color=0x2b2d31,
    )
    
    user = ctx.author
    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

    embed.add_field(
        name=f"{user.name}#{user.discriminator}",
        value=f"Статус: `Создатель`\nКомментарий: `Надеюсь, вам нравится Лифи!`",
        inline=False,
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar)
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)
    await ctx.send(embed=embed)

bot.run('Твой токен')
