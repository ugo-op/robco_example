import socket
import time
import json
from addresses import CAMERA_ADDRESS

class CameraSensor:
    def __init__(self, CAMERA_ADDRESS, delay=2):
        self.delay = delay
        self.server_address = CAMERA_ADDRESS
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.server_address)
        self.server.listen(1)
        print(f"[CameraSensor] Listening on {self.host}:{self.port}")

    def send_data(self):
        while True:
            print("[CameraSensor] Waiting for client...")
            conn, client_addr = self.server.accept()
            print(f"[CameraSensor] Client connected: {client_addr}")

            while True:
                # For simplicity, send mock "image data" as JSON
                data = {
                    "frame_id": int(time.time()),
                    "image_path": f"/mock_images/frame_{int(time.time())}.jpg"
                }
                try:
                    conn.sendall((json.dumps(data) + "\n").encode())
                except (BrokenPipeError, ConnectionResetError):
                    print("[CameraSensor] Client disconnected")
                    break
                time.sleep(self.delay)
