import requests

print("""
  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$   /$$
 /$$__  $$ /$$__  $$|__  $$__//$$__  $$| $$$ | $$
| $$  \__/| $$  \ $$   | $$  | $$  \ $$| $$$$| $$
|  $$$$$$ | $$$$$$$$   | $$  | $$$$$$$$| $$ $$ $$
 \____  $$| $$__  $$   | $$  | $$__  $$| $$  $$$$
 /$$  \ $$| $$  | $$   | $$  | $$  | $$| $$\  $$$
|  $$$$$$/| $$  | $$   | $$  | $$  | $$| $$ \  $$
 \______/ |__/  |__/   |__/  |__/  |__/|__/  \__/
                                                 
Tiktok Change Password [ v1 ] Free Tool, Copyright claimed
- Telegram : s9tan  | Instagram : @yjxf / @vpns.lost
""")

class SATAN():
    def __init__(self):
        self.session = input('[?] Session ID :')
        self.old_password = input('[?] old password :')
        self.new_password = input('[?] New Password :')
        self.change_password()

    def hack(self,text):
        def encrypt(string):
            encrypted = [hex(ord(c) ^ 5)[2:] for c in string]
            return "".join(encrypted)
        s = encrypt(text)
        return s

    def change_password(self):
        url = "https://api2.musical.ly/passport/password/update/?version_code=12.0.0&pass-region=1&pass-route=1&language=ar&app_name=musical_ly&vid=XX14528E-A953-4857-80F7-4494A171E05C&app_version=12.0.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42121&device_id=6785177577851504133&tz_offset=10800&account_region=&sys_region=SA&aid=1233&residence=SA&screen_width=1125&uoo=1&openudid=5b3a2fbfb73934b2c5918fb2c1c6a7d88cf076d8&os_api=18&ac=WIFI&os_version=14.4&app_language=en&tz_name=Asia/Riyadh&current_region=SA&device_platform=iphone&build_number=120008&device_type=iPhone12,3&iid=7011916372695598854&idfa=00000000-0000-0000-0000-000000001111"
        headers = {
            "Host": "api2.musical.ly",
            "Connection": "close",
            "Content-Length": "84",
            "sdk-version": "1",
            "x-Tt-Token": "010db57c7a068646a3e3b34afef6136fd902b91f087f783f30ab23401bc6fbcce3f4ab4adec3eb016e092b4377052ac9004afa00fee18d416968cb52be0b599847a6ccf55d126fecac1d2a556b836367673af22eba279dda8ef47cd61b9e96a81fc4f-1.0.1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "TikTok 12.0.0 rv:120008 (iPhone; iOS 14.4; ar_SA@calendar=gregorian;numbers=latn) Cronet",
            "Cookie": f"sessionid={self.session};",
            "X-Khronos": "1652439083",
            "X-Pods":"",
            "X-Gorgon": "03614110800030dde699b51fbe74c6b04a86b996c4f976778873"
        }
        data = {
            "current_password": self.hack(self.old_password),
            "mix_mode":"1",
            "password":self.hack(self.new_password)
        }
        r = requests.post(url,headers=headers,data=data)
        if 'Incorrect account or password' in r.text:
            input('[X] Bad session ID or old password')
            exit()
        elif r.json()['message'] == "success":
            print('[+] Done Change Your Password')
            print(f'[+] new session -> {r.json()["data"]["session_key"]}')
            input('')
            exit()
        else:
            print('[X] Error -> ' + r.text)
            input("")
            exit()
SATAN()
