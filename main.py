import httpx, time
token = "OTYzNDI2MjY4OTkxMzQ4NzQ2.GJXdV-.h4QUSUb_XAAlU_-7UE74QvJA0GR-HJdIV1-pPU"
content = "<a:verifygreen:1019661388567818260> **Sudo Shop** <a:verifygreen:1019661388567818260>\n\n<a:trusted:859510878796644392> **MM accepted for big orders** <a:trusted:859510878796644392> \n\n<a:Money:1012387448963223572> Payment methods <a:anex_arrows:933803135686824018> <:ltc:1010534327530049546> <:crypto:919504579886985247> <:PAYPAL:993843598158204949> \n\n<a:YOUTUBE:985807212318453760> **Youtube Services** <a:YOUTUBE:985807212318453760> \n\n```Subscribers,Likes,Views,Watchtime,Target countries Views...```\n\n<:instagram:1008189111359787029> **Instagram Services** <:instagram:1008189111359787029> \n\n```Followers,Reel/Post views,Custom comments, Live Viewers...```\n\n<:telegram:1019287476000542801> **Telegram Services** <:telegram:1019287476000542801> \n\n```Members,Post views/votes```\n\n<:TikTok:1008189093471068221> **TikTok Services** <:TikTok:1008189093471068221> \n\n```Followers,Views,Likes,Comments,Shares```\n\n<:1_Discord:1008843821087465582> **Discord Services** <:1_Discord:1008843821087465582> \n\n```Offline/Online Members,Friends Requests,MassDM```\n\n<a:hacker:1003507067711135754> **Doxxing/Osint Service** <a:hacker:1003507067711135754> \n \n ```Dm for price, depends on the victim and how much info you already have``` \n \n DM me to buy/ask price"
channelid = "1016778881694433320"
channelid2 = "999940052987674625"
channelid3 = "999940296160854066"
channelid4 = "1003506407989051482"
channelid5 = "1000899439688425615"
delay = 900
delay2 = 2
while True:
    time.sleep(delay)
    ree = httpx.post(f'https://discord.com/api/v9/channels/{channelid}/messages', headers={'authorization': token}, json={"content": content})
    if ree.status_code == 200:
        print(f"Succesfully sent to channel with ID {channelid}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)
    time.sleep(delay2)
    ree2 = httpx.post(f'https://discord.com/api/v9/channels/{channelid2}/messages', headers={'authorization': token}, json={"content": content})
    if ree2.status_code == 200:
        print(f"Succesfully sent to channel with ID {channelid2}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)
    time.sleep(delay2)
    ree3 = httpx.post(f'https://discord.com/api/v9/channels/{channelid3}/messages', headers={'authorization': token}, json={"content": content})
    if ree3.status_code == 200:
        print(f"Succesfully sent to channel with ID {channelid3}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)
    time.sleep(delay2)
    ree4 = httpx.post(f'https://discord.com/api/v9/channels/{channelid4}/messages', headers={'authorization': token}, json={"content": content})
    if ree4.status_code == 200:
        print(f"Succesfully sent to channel with ID {channelid4}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)
    time.sleep(delay2)
    ree5 = httpx.post(f'https://discord.com/api/v9/channels/{channelid5}/messages', headers={'authorization': token}, json={"content": content})
    if ree5.status_code == 200:
        print(f"Succesfully sent to channel with ID {channelid5}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)


