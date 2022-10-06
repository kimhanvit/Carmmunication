import speech_recognition as sr


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
r = sr.Recognizer()
with sr.Microphone() as source:
    print("마이크를 사용하여 듣기 시작!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        #said = r.recognize_google(audio, language="ko-KR")
        said = r.recognize_google_cloud(audio, language="ko-KR", credentials_json= JSON)
        print("구글 인식 : {}".format(said))

    except sr.UnknownValueError as ve:
        print("구글 인식 불가 : {}".format(ve))
    except sr.RequestError as re:
        print("구글 오류 : {}".format(re))