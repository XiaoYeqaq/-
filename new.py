import requests
import os
import json
def main():
    zhiye = ['demonhunter', 'druid', 'hunter', 'mage', 'paladin', 'priest', 'rogue', 'shaman', 'warlock', 'warrior']
    for each in zhiye:
        for i in range(1,12):
            data = {'cardClass': each,
                    'p': i,
                    'standard': '1',
                    }
            res = open_url(data)
            image = del_url(res)
            save_data(image)
def open_url(data):
    url = 'https://hs.blizzard.cn/action/cards/query'
    res = requests.post(url=url,data=data)
    return res
def del_url(res):
    image = []
    res_py = res.text
    res_js = json.loads(res_py)
    a = res_js['cards']
    for i in a:
        image.append(i['image'])
    return image
def save_data(image):
    for img in image:
        with open("D:\\测试文件\\" + os.path.basename(img), 'wb') as f:
            f.write(requests.get(img).content)
        print(os.path.basename(img) + "保存成功")
if __name__=='__main__':
    main()