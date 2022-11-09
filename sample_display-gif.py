#-*- coding:utf-8 -*-
import speech_recognition as sr
from PIL import Image, ImageSequence
import pyautogui 
from time import sleep
## import os
import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

JSON = '''
    {
  "type": "service_account",
  "project_id": "car-mmunication",
  "private_key_id": "2d7cfdc5afe3dbaac6255bd246d5817f65017134",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJhzRiMQm0e8Xr\\nyH22NIBYn8/psQUEPJYUGjhhJ9f+Fke/rDpjkh6Hebu3JuFFvCnv5JRw5qEOjBEW\\nOU58O84EDyv1ya0ZE5t6HYQkNBS+SyhwVIFYC8o1g0LHyToBfdVa8POjpSCaor3M\\n0CkDUqQyT0jJpjW7MdY/twWv8iI8Jc7ir8ecLy6405TjEDFdsItNrm7bFocYD0Yt\\nqm77plfuCkgsJd0SsiWnmWOh0+mlXQw+TYroIeOJQsee11UCy3S9LwogoF5/Eq5h\\n7ennJplz5kW2VD4svXMCzJdEuLTNMoKWaYgzVnjVo1scQfwFzUFgFxb/tf/3OqPW\\nHZRhxMwBAgMBAAECggEAAk28gTUKMhxQseykotXps+ALZNW5I7UCMMa8jcAoy/bO\\nItueZQx8ZlqNIexJgQrqizUFWfjWiJLJadDFlaerJ9wF8EUtQh8TNPUyhHJtXHm1\\nKhTBNlpkjGUmRbl5lp8TkDq2yKnznAKC7mnG8KRVcnctcxNzQ+MVzdXzASTT4Ns3\\nLzc4y2+BM6mb+7f1FvT32SGUHwpBN/hPEm5J0ABnLLUcSd9DKUjpMxZ97P/YXRKZ\\nsXbVLoBfUAZmBlHY8ba6IQSOgFlIQIXzK3W0w9l+bZvZSmtcdGtw9Okbb7GsSLI8\\nVq0s7evrFtJEFDuIgEucPO5AytmcWMqgMM3D0b27RQKBgQDvKWznvzHzVP24DC13\\nJzzJoU+6Kfu9KdDe5npnXNb0wwBt/VOuh6EI89/fPwPxz3Cr8v8MXA8y5u98CRpd\\nuQzZyg8ZuyTAuKEWM2xuJRMd05pswpbBFTyFrq8WRex/3TAzREk31kOUt2cxzDok\\nvoORIufZOSsE4BAWwFdqSm0JLQKBgQDXt3ts+WdKD51Tj4me9KJU0YXdvkCDA+Hi\\npIrLBQfQRqMzZR6//2GGOc060Qb2r03dFedmDRr4znANGFYRswEbSN4Me+fFRrU5\\nLhY+Nlfv6avsIi3sblGxOCQDxXiLREVGcvGU5Ypr2mJ31y1MkHahYJKfdJAkUX1+\\nKKtZOr6qpQKBgDw99wy5AGAGvJIrnxgwbgNr+qUuBhcz/UToUVTP8eVdaTJLaVTB\\nHTMgGvgk611xnzPw1YXLepibyx83O8j33+DMINmeZjeVSh5JfbqQ5CvTLUbQDSE9\\ntC0IP1og6t2aXZXMUZUbB5LiT8AfbVXsFz/rxvLUj51+ww64DEzdynFRAoGAOWrZ\\nK3RnDcuCMM+v7eNnofPzEcamHTlXUqBBYTCBl+p1XiS4PpqXNscD3XftxpN6wjIm\\nWX97gmZQZOvpXOSskrqef+wrENN1QTcHLKACYBVucXfXiWsDy4wJ6gcRwt/1IH9P\\n1jYS1gpW01cu84YwTVwLKu43v7MBGCdzFFkSjxECgYBPpo/XddT9CWqxSyW1rmxK\\neLRtMqYv9eOolGvaEp2s5VzxCNr+Xcxa23BIevOQi0CJvL4ivt/MBVxRaymnvtQo\\nUErIHk2JEnXxMzSWFnIxNhM7LuCfYNpkt3WWbWDGq6hw0sDCpuTbsguzCSzLM1kq\\nGOTb6sCrj6hLKw8BHVaOog==\\n-----END PRIVATE KEY-----\\n",
  "client_email": "testapi@car-mmunication.iam.gserviceaccount.com",
  "client_id": "115145102092070035279",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/testapi%40car-mmunication.iam.gserviceaccount.com"
}
'''
def read_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # source threshold 조정
        audio = r.listen(source)
        try:
            said = r.recognize_google_cloud(audio, language="ko-KR", credentials_json= JSON)

            return said
        except sr.UnknownValueError:
            return print("구글 인식 불가")
        except sr.RequestError as re:
            return print("구글 오류 : {}".format(re))

def display(img_name):
    im = Image.open(f'/home/hanvit/Carmmunication/source/{img_name}')
    im.show()
    ## os.system(f"xdg-open /home/hanvit/Carmmunication/source/{img_name}")
    pyautogui.press('f11', presses=2, interval=0.5)
    sleep(10)
    pyautogui.press('esc', presses=2, interval=0.5)

def display_gif(img_name):
    im = Image.open(f'/home/hanvit/Carmmunication/source/{img_name}')
    index = 1
    for frame in ImageSequence.Iterator(im):
        frame.save("frame%d.png" % index)
        index += 1
    '''
     root = Tk()

    #frame
    frameCnt = 15
    frames = [PhotoImage(file=f'/home/hanvit/Carmmunication/source/{img_name}',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(500, update, ind)

    # fullscreen
    # F11: fullscreen toggle, Esc : exit fullscreen mode 
    root.attributes("-fullscreen", True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                        not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    #window center position
    positionRight = root.winfo_screenwidth()/2 
    positionDown = root.winfo_screenheight()/2

    #set image
    label = Label(root, bg='black')
    label.place(x=positionRight,y=positionDown,anchor=CENTER)
    root.after(0, update, 0)

    #background color
    root.configure(bg='black')

    return root.mainloop()
    '''
   

#### main 
while True:
    print("음성인식을 시작합니다.")

    voice = read_voice()

    hotwords_1 = ['고마워 ', '감사합니다 ', '감사 ', '땡큐 ', '고마워요 '] # 감사합니다
    hotwords_2 = ['미안해 ', '죄송합니다 ', '죄송 ', '미안합니다 ', '미안 ', '쏘리 '] # 죄송합니다
    hotwords_3 = ['조심해 ', '조심 ' , '조심하세요 '] # 전방 주의 
    hotwords_4 = ['가세요 '] # 먼저 가세요!!
    hotwords_5 = ['갈게요 ','양보 '] # 먼저 갈게요 ~
    hotwords_6 = ['차선 변경 ','차선 '] #차선 변경 
    hotwords_7 = ['비상 ', '응급 ', '응급 상황 ', '도와줘 ', '도와 주세요 ', '살려줘 ', '살려 주세요 '] # 응급상황
    img_list = ['1.gif', 'sorry.gif', 'warning.gif', 'youfirst.gif', 'mefirst.gif','lanechange.gif','emergency.gif']
    print(voice)

    if voice in hotwords_1 :
        display_gif(img_list[0])
        break
    elif voice in hotwords_2:
        display(img_list[1])
        break
    elif voice in hotwords_3:
        display(img_list[2])
        break
    elif voice in hotwords_4:
        display(img_list[3])
        break
    elif voice in hotwords_5:
        display(img_list[4])
        break
    elif voice in hotwords_6:
        display(img_list[5])
        break
    elif voice in hotwords_7:
        display(img_list[6])
        break
    else:
        print(f"{voice}는 등록되어 있는 단축어가 아닙니다.")
