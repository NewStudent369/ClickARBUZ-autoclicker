import random
import time
import datetime
import requests
from colorama import Fore, Style
import pyautogui
import keyboard
import colorama


colorama.init()
getPrizeValue = 'https://api.gattogame.site/pet.getPrizeValue'
getPrize = "https://api.gattogame.site/pet.getPrize"
feed     = "https://api.gattogame.site/pet.feed"
play     = "https://api.gattogame.site/pet.play"


id=['6611419b083ca1111f639b86','6615bbef61022cc01b4788cf','66175dc8a8a5eaa20250bd41','661d0e6732d09bb5dab2d068']

authMap={
    '66175dc8a8a5eaa20250bd41':"Bearer query_id=AAGHwSFWAAAAAIfBIVbUfThT&user=%7B%22id%22%3A1445052807%2C%22first_name%22%3A%22yyyyy%22%2C%22last_name%22%3A%22ttttttt%22%2C%22username%22%3A%22ytw521jxy%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1713228019&hash=7b8b3de0dac0088bbeac47653094ef92dc3897c83e082450e4157df04e75fdcf",
    '661d0e6732d09bb5dab2d068':"Bearer query_id=AAGHwSFWAAAAAIfBIVbUfThT&user=%7B%22id%22%3A1445052807%2C%22first_name%22%3A%22yyyyy%22%2C%22last_name%22%3A%22ttttttt%22%2C%22username%22%3A%22ytw521jxy%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1713228019&hash=7b8b3de0dac0088bbeac47653094ef92dc3897c83e082450e4157df04e75fdcf",
    '6611419b083ca1111f639b86':"Bearer query_id=AAE73apfAAAAADvdql9W4bvK&user=%7B%22id%22%3A1605033275%2C%22first_name%22%3A%22%E4%B8%8D%E6%9C%8D%E6%89%93%E6%88%91%E5%95%8A%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22jiangmoumou%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1713228440&hash=5860e7f9a5dee10e5760639ae0228dfd20fc4c1336c67a587ecbed57eb076d67",
    '6615bbef61022cc01b4788cf':"Bearer query_id=AAE73apfAAAAADvdql9W4bvK&user=%7B%22id%22%3A1605033275%2C%22first_name%22%3A%22%E4%B8%8D%E6%9C%8D%E6%89%93%E6%88%91%E5%95%8A%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22jiangmoumou%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1713228440&hash=5860e7f9a5dee10e5760639ae0228dfd20fc4c1336c67a587ecbed57eb076d67"
}


def feeds():
    for i in id:
        try:
            headers1 = {
                'Content-Type': 'application/json',
                'Authorization': authMap.get(i),
                "Origin": "https://frontend.gattogame.site",
                "Referer": "https://frontend.gattogame.site/",
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
            }
            data = {
                "id": i
            }
            feedResponse = requests.post(url=feed, headers=headers1, json=data)
            feedResponseJson = feedResponse.json()
            if feedResponse.status_code == 200:
                print(f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLACK_EX}({datetime.datetime.now()}){Fore.LIGHTWHITE_EX} {Fore.LIGHTBLUE_EX}{i}:投喂成功{Fore.LIGHTYELLOW_EX}]')
            time.sleep(5)
        except Exception as e:
            print(f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLACK_EX}({datetime.datetime.now()}){Fore.LIGHTWHITE_EX} {Fore.LIGHTRED_EX}{i}:投喂失败{Fore.LIGHTRED_EX}]')
            time.sleep(10)


def getPrizes():
    for i in id:
        headers1 = {
            'Content-Type': 'application/json',
            'Authorization': authMap[i],
            "Origin": "https://frontend.gattogame.site",
            "Referer": "https://frontend.gattogame.site/",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
        }
        data = {
            "id": i
        }
        trycnt=0
        while True:
            try:
                apiMeResponse = requests.post(getPrizeValue, headers=headers1, json=data)
                apiMeResponseJson = apiMeResponse.json()
                if apiMeResponse.status_code == 200:
                    if apiMeResponseJson["value"] == 100:
                        time.sleep(5)
                        getPrizeResponse = requests.post(getPrize, headers=headers1, json=data)
                        agetPrizeResponseJson = getPrizeResponse.json()
                        if getPrizeResponse.status_code == 200:
                            print(f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLACK_EX}({datetime.datetime.now()}){Fore.LIGHTWHITE_EX} {Fore.LIGHTBLUE_EX}{i}:游戏打开奖励成功{Fore.LIGHTYELLOW_EX}]')
                    else:
                        break
                trycnt=0
            except Exception as e:
                trycnt+=1
                if trycnt > 10:
                    break
                time.sleep(10)
        time.sleep(5)


def plays():
    for i in id:
        headers1 = {
            'Content-Type': 'application/json',
            'Authorization': authMap[i],
            "Origin": "https://frontend.gattogame.site",
            "Referer": "https://frontend.gattogame.site/",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
        }
        data={
            "id":i
        }
        try:
            playResponse = requests.post(play, headers=headers1, json=data)
            playResponseJson = playResponse.json()
            if playResponse.status_code == 200:
                print(f'{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLACK_EX}({datetime.datetime.now()}){Fore.LIGHTWHITE_EX} {Fore.LIGHTBLUE_EX}{i}:游戏成功{Fore.LIGHTYELLOW_EX}]')
            time.sleep(5)
        except:
            time.sleep(5)



feedcnt = 0
getcnt = 0

exceps=0

while True:
    feeds()
    time.sleep(120)
    getcnt+=1
    if getcnt > 20:
        getPrizes()
        getcnt = 0
    feedcnt+=1
    if feedcnt > 60:
        try:
            plays()
            feedcnt = 0
        except:
            pass
