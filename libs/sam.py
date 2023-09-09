# sam サーバーに画像を送って

import requests
import base64
from pathlib import Path

server_url = 'http://localhost:5000/process_image'  # Change this to the actual server URL
class SamService:
    def __init__(self, image_path):
        with open(image_path, 'rb') as f:
            image_data = f.read()
            self.image_path = image_path
            self.image_base64 = base64.b64encode(image_data).decode()

    def send_image_for_processing(self, box):
        data = {
            'image': self.image_base64,
            "input_box": box,
            'image_stem': Path(self.image_path).stem
            # Include any other data you want to send to the server
        }

        response = requests.post(server_url, json=data)

        if response.status_code == 200:
            result = response.json()['result']
            print('Recognition results:', result['box'])
            return result
        else:
            print('Error:', response.text)