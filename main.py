import discord
import qrcode
import pathlib
import random
# import tracemalloc memoryallocation 로우레벨 낮아질때 쓰는거임
import re

client = discord.Client() #시작


@client.event #시작 골뱅이는 뭔가요? 데코레이터 함수 묶음 이라고 생각하세요
async def on_ready(): #
    print("봇준비")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(type=discord.Game, name="!help | !도움"))
    print("준비완료")


@client.event
async def on_message(message):
    msg = message.content
    if message.author.bot:  # 봇이 보낸거는 무시
        return

    if msg == '!핑' or msg == '!ping':
        embed = discord.Embed(title=':ping_pong: 퐁!', description=str(round(client.latency * 1000)) + 'ms',
                              color=0x00ffc4)
        embed.set_footer(text="Copyright © Odyssey#0615 Allright Reserved 2020")
        await message.channel.send(embed=embed)

    if msg == '!퐁' or msg == "!pong":
        embed = discord.Embed(title=':ping_pong: 핑!', description=str(round(client.latency * 1000)) + 'ms',
                              color=0x00ffc4)
        embed.set_footer(text="Copyright © Odyssey#0615 Allright Reserved 2020")
        await message.channel.send(embed=embed)

    if message.content == "!현재":
        channel = message.channel
        msg = "유현재 할짝"
        await channel.send(msg)
        await message.channel.send(file=discord.File("lick.gif"))

    if message.content == "!원현":
        channel = message.channel

        msg = "던져! 던져!"

        await channel.send(msg)
        await message.channel.send(file=discord.File("soh.gif"))

    if message.content == "!시진핑":
        channel = message.channel
        msg = "핑핑"
        await channel.send(msg)
        await message.channel.send(file=discord.File("xijin.jpg"))

    bad = ['ㅅㅂ', '시발', '씨발', "지랄", "tlqkf", "염병", "병신", "닥쳐", "씹새끼", "씹", "ㅗ", "엿",]

    for i in bad:
        if i in msg:
            await message.channel.send('이상한 말!')
            await message.delete()

    sa_bi_ru_sa = ['느그루사', "느그루사어", '더러운 사비루사', "느그노보", "더러운", "좆비루사", "너거루사", "느ㄱ그루사", "치워라", "느그루사 치워라 역하다",
                   "봇 메세지 검열완료"]
    # re.compile('느그루사') 정규식 배우고 나서 하자
    #TODO: jungusik learn
    message_contant = message.content
    for i in sa_bi_ru_sa:
        if i in msg:
            await message.channel.send('사비루사는 위대하다!')
            await message.delete()

    whisky = ['위스키련', '미친봇', "개새끼"]

    for i in whisky:
        if i in msg:
            await message.channel.send('위스키를 욕하지 마라!')
            await message.delete()

    if message.content == "sa bi ru sa":
        channel = message.channel
        msg = "ju sae no bo"
        await channel.send(msg)

    if message.content == "사비루사":
        channel = message.channel
        msg = "주세노보"
        await channel.send(msg)

    if message.content == "ju sae no bo":
        channel = message.channel
        msg = "kkal kkal kki kkol kkal"
        await channel.send(msg)

    if message.content == "주세노보":
        channel = message.channel
        msg = "칼칼킬콜칼"
        await channel.send(msg)

    if (msg == '!사비루사' or msg == '!sa bi ru sa'):
        embed = discord.Embed(title="사비루사 사전", description="sa bi ru sa Dictionary", color=0x00ffc7)
        embed.set_author(name="Made by Odyssey")
        embed.add_field(name="sa bi ru sa", value="안녕하세요", inline=False)
        embed.add_field(name="ju sae no bo", value="반갑습니다", inline=False)
        embed.add_field(name="kkal kkal kki kkol kkal", value="ㅋㅋㅋ", inline=False)
        embed.add_field(name="sa run ahn in joe", value="ㄹㅇㅋㅋ", inline=False)
        embed.add_field(name="po phen tio", value="포토샵", inline=False)
        embed.add_field(name="ming na", value="미안(밍나)", inline=False)
        embed.set_footer(text="Copyright © Odyssey#5373 Allright Reserved 2022")
        await message.channel.send(embed=embed)

    sexual = ['자1지', '보지', '보1지', "섹스", "섹1스", "기모찌", "앙기모띠", "기모띠", ":point_right: :ok_hand:", "자지", "sex", "せっす",
              "いるだ だっざんへ", "いずせっ げんや ちゅうん", "そをんへんちゃうん さらんへ", "좆"]

    for i in sexual:
        if i in msg:
            await message.channel.send('야한 말!')
            print(msg)
            await message.delete()

    if message.content == "!동기":
        channel = message.channel
        msg = "^^"
        await channel.send(msg)
        await message.channel.send(file=discord.File("flyahn.png"))

    if message.content == "!루피야 저리가":
        channel = message.channel
        msg = "나는 루피가 아니라 위스키야!"
        await channel.send(msg)

    if (msg == '!도움' or msg == '!help'):
        embed = discord.Embed(title="명령어 사용법", description="!help", color=0x00ffc4)
        embed.set_author(name="Whisky")
        embed.add_field(name="!사비루사", value="사비루사 사전 불러오기", inline=True)
        embed.add_field(name="!핑", value="서버의 핑 보기", inline=True)
        embed.add_field(name="!현재", value="현재 짤 불러오기", inline=True)
        embed.add_field(name="!원현", value="원현 짤 불러오기", inline=True)
        embed.add_field(name="!시진핑", value="핑핑~", inline=True)
        embed.add_field(name="!동기", value="^^", inline=True)
        embed.add_field(name="!about", value="위스키에 대해", inline=True)
        embed.add_field(name="!패치노트", value="매주 추가되는 위스키의 패치!", inline=True)
        embed.set_footer(text="Copyright © Odyssey#5373 Allright Reserved 2022")
        await message.channel.send(embed=embed)

    if (msg == "!about"):
        embed = discord.Embed(title="About Whisky", description="Made by Odyssey#7451", color=0x00ffc4)
        embed.set_author(name="위스키에 대해서")
        embed.add_field(name="위스키는 2020년 12월 23일에 태어났어요", value="Whisky", inline=True)
        embed.set_footer(text="Copyright © Odyssey#5373 Allright Reserved 2022")
        await message.channel.send(embed=embed)

    if (msg == "!패치노트"):
        embed = discord.Embed(title="Patch Note", description="1월 1주차 패치 v1.2 Stable 안정 3", color=0x00ffc4)
        embed.set_author(name="패치노트")
        embed.add_field(name="안동기 짤 추가", value="^^~", inline=False)
        embed.set_footer(text="Copyright © Odyssey#5373 Allright Reserved 2022")
        await message.channel.send(embed=embed)

    if msg == "!도박" or msg == '!gamble':
        embed = discord.Embed(title="Gamble", description="도박 중독은 국번없이 1336", color=0x00ffc4)
        embed.set_author(name="도박")
        embed.add_field(name="가정의 행복까지 베팅하진 마십시오. 과도한 도박은 빚만 불러오지 않습니다.", value="관련 전문기관의 도움을 받으세요", inline=False)
        embed.set_footer(text="Copyright © Odyssey#5373 Allright Reserved 2022")
        await message.channel.send(embed=embed)

    juseok = ["주석", "이주석"]
    message_contant = message.content
    for i in juseok:
        if i in message_contant:
            await message.channel.send('주석이가 좋아?')

    if message.content.startswith('!qr'):
        qr = qrcode.QRCode()
        rn = random.random()
        msg = message.content[4:]
        qr.add_data(msg)
        qr.make()
        img = qr.make_image(fill='black', back_color="white")
        img.save(pathlib.Path(f'./qrcodes/qr-code-{msg.replace(" ", "-")}-{rn}.png'), 'PNG')
        await message.channel.send(
            file=discord.File(pathlib.Path(f'./qrcodes/qr-code-{message.content[6:].replace(" ", "-")}-{rn}.png')))



    if msg == "나에게 천사가 내려왔다":
        channel = message.channel
        msg = "안녕하세요 안동기가 사랑하는 Wataten 입니다."
        await channel.send(msg)


client.run("null")
