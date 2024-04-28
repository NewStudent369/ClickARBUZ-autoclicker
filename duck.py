import requests
import time


getList = "https://api.quackquack.games/nest/list-reload"
collectUrl = "https://api.quackquack.games/nest/collect"
heatch = "https://api.quackquack.games/nest/hatch"
collectDuck = "https://api.quackquack.games/nest/collect-duck"
removeUrl = "https://api.quackquack.games/duck/remove"

token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY2MzgsInRpbWVzdGFtcCI6MTcxNDI3NTM4OTQ0NywidHlwZSI6MSwiaWF0IjoxNzE0Mjc1Mzg5LCJleHAiOjE3MTQ4ODAxODl9.l6oI8OHgFslzSXFlrndfpmAlKTxxC2hNCh4tgafGFdQ"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Authorization':token,
    'Origin':"https://quackquack-prj.s3.ap-southeast-1.amazonaws.com",
    'Referer':"https://quackquack-prj.s3.ap-southeast-1.amazonaws.com/",
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
}





def getSort():
    moveId = ""
    lasteTyp = 1000
    rsp = requests.get(getList, headers=headers)
    NestLists = rsp.json().get("data").get("duck")
    for list in NestLists:
        id = list.get("id")
        metadata = list.get("metadata")
        head_type = metadata.get("head_type")
        body_type = metadata.get("body_type")
        arm_type = metadata.get("arm_type")
        totTyp = int(arm_type)+int(body_type)+int(head_type)
        if totTyp < lasteTyp:
            lasteTyp = totTyp
            moveId   = id

    return moveId

def remove(id):
    move=[]
    move.append(id)
    if len(move) > 0:
        jsonClt = {
            "ducks": "{\"ducks\"" + ":" + str(move) + "}"
        }
        while True:
            rsp = requests.post(removeUrl, json=jsonClt, headers=headers)
            if rsp.status_code == 200:
                print("移除成功")
                break
            else:
                time.sleep(10)

hav=False
cnt=0

removeId = getSort()
remove(removeId)

while True:
    try:
        while True:
            rsp = requests.get(getList,headers=headers)
            time.sleep(2)
            NestLists=rsp.json().get("data").get("nest")
            for list in NestLists:
                id = list.get("id")
                status = list.get("status")
                egg_config_id = list.get("egg_config_id")
                type_egg = list.get("type_egg")
                if int(status) == 2:
                    cnt+=1
                    print(str(cnt)+"   status:" + str(status), end="     ")
                    jsonClt={
                        "nest_id":id
                    }
                    if int(egg_config_id) <= 4:
                        rsp = requests.post(collectUrl, headers=headers, json=jsonClt)
                        if rsp.status_code == 200:
                            print("收获成功:")
                            time.sleep(2)
                    else:
                        rsp = requests.post(heatch, headers=headers, json=jsonClt)
                        if rsp.status_code == 200:
                            print("孵蛋成功:",end="    ")
                            time.sleep(2)
                            rsp = requests.post(collectDuck, headers=headers, json=jsonClt)
                            if rsp.status_code == 200:
                                print("收获成功:")
                                removeId = getSort()
                                remove(removeId)
                else:
                    if int(status) == 3:
                        print("status:" + str(status), end="     ")
                        rsp = requests.post(collectDuck, headers=headers, json=jsonClt)
                        if rsp.status_code == 200:
                            print("收获成功:")
                            time.sleep(2)
                    else:
                        print("status:" + str(status))
                        time.sleep(5)

                finish_time = list.get("finish_time")
                time_remain = list.get("time_remain")

                updated_time = list.get("updated_time")
            time.sleep(2)
    except:
        time.sleep(10)