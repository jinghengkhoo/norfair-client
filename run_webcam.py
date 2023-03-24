import requests
import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    cv2.imwrite("temp.png", frame)
    with open("temp.png", 'rb') as f:
        res = requests.post('http://20.98.212.250:8001/api/run',
                    files={'upload': f},
                    data={'id': '1'},
                    )
        print(res.content)