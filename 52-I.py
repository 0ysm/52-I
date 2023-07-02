import discord, asyncio, datetime, pytz
import random as ran


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        #if message.content.startswith ("!번호"):
            numCh = client.get_channel(1124999062844866561)
            if message.author.roles[1]:
                await message.channel.purge(limit=1)
                global num
                num = ran.randint(0,100)
                embed = discord.Embed(title="{}님의 번호는 {}번 입니다.".format(message.author.name,num), description="입장하러 가자 (겹치면 다시)", color=0x64ffbf)

                await numCh.send(embed=embed)
                
            else:
                await message.channel.purge(limit=1)
                await message.channel.send("{}는 권한이 없어".format(message.author.name))

        if message.content.startswith ("!입장"):
            intoCh = client.get_channel(1124999034667532298)
            oldrole = discord.utils.get(message.guild.roles, name="임시")
            newrole = discord.utils.get(message.guild.roles, name="챌린지 중")
            user = message.author
            if message.author.roles[1]:
                await message.channel.purge(limit=1)
                #global numlist
                #numlist = {}
                #numlist[user] = num

                await intoCh.send ("{}님 입장을 환영합니다.".format(message.author.mention))
                await user.add_roles(newrole)
                await user.remove_roles(oldrole)
                
            else:
                await message.channel.purge(limit=1)


        if message.content.startswith ("!지목"):
            pointoutCh = client.get_channel(1125021465629184100)
            role = discord.utils.get(message.guild.roles, name="클리어")
            user = message.author
            if message.author.roles[0]:
                await message.channel.purge(limit=1)
                name = message.content[4:]
                embed = discord.Embed(title="**{}님이 다음 타자를 지목했습니다!**".format(message.author.name),description="\n-------------------------\n\n\t{}\n\n-------------------------\n".format(name),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x64ffbf)
                await pointoutCh.send("@everyone",embed=embed)
                await user.remove_roles(role)
            
            else:
                await message.channel.purge(limit=1)
                await message.content("{}는 권한이 없어".format(message.author.mention))


        if message.content == '0입장 안내0':
            intoCh = client.get_channel(1124999034667532298)
            await intoCh.purge(limit=1)
            embed = discord.Embed(title="사람은 절망하라", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x64ffbf)
            
            embed.add_field(name="당신이 위대한 도전을 시작하기 전, 마지막 기회입니다.\n",value="포기를 모르는 자는 입장을...\n!입장 (번호표 뽑고 오셈)", inline=False)
            embed.set_footer(text="Bot Made by. 0ysm",icon_url="https://cdn.discordapp.com/attachments/1125007001395658854/1125007429223067678/0ysm1.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125007001395658854/1125016739151884400/baby_Bina.png")
            
            await intoCh.send("@everyone",embed=embed)

        #if message.content == '0번호 안내0':
            #numCh = client.get_channel(1124999062844866561)
            #await numCh.purge(limit=1)
            #embed = discord.Embed(title="사람은 절망하라", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x64ffbf)
            
            #embed.add_field(name="당신이 위대한 도전을 시작하기 전, 마지막 기회입니다.\n",value="(!번호)를 입력하고 번호표 뽑기", inline=False)
            #embed.set_footer(text="Bot Made by. 0ysm",icon_url="https://cdn.discordapp.com/attachments/1125007001395658854/1125007429223067678/0ysm1.png")
            #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125007001395658854/1125016739151884400/baby_Bina.png")
            
            #await numCh.send("@everyone",embed=embed)

        if message.content.startswith ("!공지"):
            inforCh = client.get_channel(1125055940467642419)
            i = (message.author.guild_permissions.administrator)
            if i is True:
                notice = message.content[4:]
                embed = discord.Embed(title="**새로운 공지가 올라왔습니다. 모두 확인해 주세요**",description="\n--------------------\n\n{}\n\n--------------------\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x64ffbf)
                await inforCh.send("@everyone", embed=embed)
            if i is False:
                await message.channel.send ('{}님의 권한이 부족'.format(message.author.mantion))

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTEyNDk2NTIzMDg3MTU5NzIwNw.GV557z.3Cz4MDccJF2XH38Zk-YIeMRc3ecVyYYY3MbCKU')