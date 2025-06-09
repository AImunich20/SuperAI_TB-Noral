from PIL import Image
import requests
import io

image_path = "/home/maybe/Downloads/TB/1003.png"
image = Image.open(image_path).convert("RGB")
image.thumbnail((1024, 1024))
buffer = io.BytesIO()
image.save(buffer, format="JPEG", quality=85)
buffer.seek(0)

url = "https://classify.roboflow.com/cxr-for-tb/1?api_key=zvbGS82oe5o2F7vG6dv8"
response = requests.post(url, files={"file": buffer})

if response.status_code == 200:
    result = response.json()
    print(result)
    print(f"ผลวิเคราะห์: {result['top']} (ความมั่นใจ: {result['confidence']*100:.2f}%)")
else:
    print(f"error : {response.status_code} - {response.text}")
