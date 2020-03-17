import requests
import sys

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

headers = {
    "Content-Type":"application/xml",
    "Authorization":"KakaoAK a4ffd5bd23a62f567e198e5f37dd4f98",
}

def make_data(x):
    data = """
    <speak>
    <voice>%s</voice>
    </speak>
    """ % x
    
    return data.encode()
while True:
    cmd = input("please do say: ") 
    data = make_data(cmd)   
    r = requests.post(url, data=data, headers=headers)
    with open("audio.mp3", "wb") as f:
        f.write(r.content) 
