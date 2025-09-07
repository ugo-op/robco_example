import socket
import json

class CameraAdapter:
    def __init__(self, host="127.0.0.1", port=5552):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.buffer = b""
        self.latest_data = {}

    def _receive_data(self):
        chunk = self.client.recv(1024)
        if not chunk:
            raise ConnectionError("Camera sensor disconnected")
        self.buffer += chunk
        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            try:
                self.latest_data = json.loads(line.decode())
            except json.JSONDecodeError:
                print("[CameraAdapter] Failed to parse JSON:", line)

    def get_latest_frame(self):
        self._receive_data()
        return self.latest_data
