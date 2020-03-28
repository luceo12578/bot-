import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("WEB을 확인한다")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("$사용법"):
        await message.channel.send("사용법"
                                   "$사용법 | 사용법을 알려줍니다"
                                   "$web | web 페이지가 몇게 있는지 알려줍니다"
                                   "$ftp | ftp 계정을 모두 알려줍니다"
                                   "끝")



@client.event
async def on_message(message):
    if message.content.startswith("$web"):
        await message.channel.send("3개"
                                   "edu.cherrynet.xyz"
                                   "db.cherrynet.xyz"
                                   "cherrynet.xyz"
                                   "끝")


@client.event
async def on_message(message):
    if message.content.startswith("$ftp"):
        await message.channel.send("edu.cherrynet.xyz"
                                   "ftp계정"
                                   "id:u172661722.educherry"
                                   "pwd:masteredu"
                                   "동시접속가능 "
                                   "cherrynet.xyz"
                                   "ftp계정"
                                   "id:u172661722.cherryuser"
                                   "pwd:user1234"
                                   "db.cherrynet.xyz"
                                   "id:u172661722.dbcherry"
                                   "pwd:db0001")




client.run("NjkzMzE3MjYxNDIzMDE4MDE2.Xn7UPQ.AFTm0GjRoOVnlVBzWpn6nSFhc8U")