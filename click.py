import random
import time
import datetime
import requests
from colorama import Fore, Style
import pyautogui
import keyboard
import colorama

tm = [0.5, 0.6, 0.7, 0.8]
print("请开始选择点击区域( 按键1左上角+按键2右下角):")
colorama.init()
urlApiMe = 'https://arbuz.betty.games/api/users/me'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #'Baggage': 'sentry-environment=production,sentry-public_key=6e836760e898018c6059dfcdba712802,sentry-trace_id=a45d9e2c1596467cb19be6d72ee4c391',
    'accept-language': 'ru-UA,ru;q=0.9,uk-UA;q=0.8,uk;q=0.7,ru-RU;q=0.6,en-US;q=0.5,en;q=0.4',
    'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="121", Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': 'Android',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
    'X-Telegram-Init-Data': "query_id=AAGHwSFWAAAAAIfBIVaAYLab&user=%7B%22id%22%3A1445052807%2C%22first_name%22%3A%22yyyyy%22%2C%22last_name%22%3A%22ttttttt%22%2C%22username%22%3A%22ytw521jxy%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1712828960&hash=71cdfbdca1f0ed3558be4e7b7e675dafbb9399004bd6d236fdb23a6d5a581311"
}

def getInfo():
    try:
        apiMeResponse = requests.get(urlApiMe, headers=headers, timeout=2)
        apiMeResponseJson = apiMeResponse.json()
        if apiMeResponse.status_code == 200:
            # 不同的字符串/依赖项
            id = apiMeResponseJson.get('id', 'NO DATA')
            fullName = apiMeResponseJson.get('fullName', 'NO DATA')
            username = apiMeResponseJson.get('username', 'NO DATA')
            balance = apiMeResponseJson.get('clicks', 'NO DATA')
            rawEnergy = apiMeResponseJson.get('energy', 'NO DATA')  # 当前能量点数
            pointPerClick = apiMeResponseJson.get('clickBoostSum', 'NO DATA')  # 每次点击获得的西瓜数量
            energyRecoverSpeed = apiMeResponseJson.get('energyBoostSum', 'NO DATA')  # 能量恢复速速/s
            minerBoostSum = apiMeResponseJson.get('minerBoostSum', 'NO DATA')  # 自增速度/s
            researchPoints = apiMeResponseJson.get('researchPoints', 'NO DATA')  # 经验值
            lastClickSeconds = apiMeResponseJson.get('lastClickSeconds', 'NO DATA')  # 经验值
            energyBoostSum = round(apiMeResponseJson.get('energyBoostSum','NO DATA'))  # сколько можно раз кликнуть чтоб энергия съелась (допустим 1 раз клика равен 7 count в дате, то есть можно 7 раз кликнуть и съестся 1 ячейка энергии)
            return rawEnergy,balance
    except:
        print("尝试重新获取信息")
        return 1000




while True:
    if "1" == keyboard.read_key():
        ps=pyautogui.position()
        lx = ps.x
        ly = ps.y
        print("已经采集左上角坐标:"+str(ps.x) + ":" + str(ps.y))
        while True:
            if "2" == keyboard.read_key():
                ps=pyautogui.position()
                rx = ps.x
                ry = ps.y
                print("已经采集右下角坐标:"+str(ps.x) + ":" + str(ps.y))
                break
        break
clicks=0
time.sleep(10)
energy=0
while True:
    if keyboard.is_pressed('3'):
        break
    pointx=random.randint(lx,rx)
    pointy=random.randint(ly,ry)
    pyautogui.click(x=pointx,y=pointy)
    index = random.randint(0, 3)
    tms = tm[index]
    time.sleep(tms)
    clicks+=1
    if clicks > 1500:
        try:
            energy,bal=getInfo()
            print(f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLACK_EX}({datetime.datetime.now()}){Fore.LIGHTWHITE_EX} {Fore.LIGHTBLUE_EX}CLICKED{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} User: {Fore.GREEN}"yt"{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}|{Fore.LIGHTWHITE_EX} Balance: {Fore.GREEN}{bal}{Fore.RED}🍉 {Fore.LIGHTYELLOW_EX}| {Fore.LIGHTWHITE_EX}Energy: {Fore.LIGHTBLUE_EX}{energy}{Fore.LIGHTYELLOW_EX}⚡️')
        except:
            pass
        clicks=0
        time.sleep((2500-energy)*2)

