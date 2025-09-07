import socket
import time
import json
from addresses import DISTANCE_ADDRESS

class DistanceAdapter:
    def __init__(self,DISTANCE_ADDRESS):
        self.server_address = DISTANCE_ADDRESS
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.server_address)
        self.buffer = b""
        self.latest_data = {}

    def _receive_data(self):
        # read from socket and handle multiple lines
        chunk = self.client.recv(1024)
        if not chunk:
            raise ConnectionError("Sensor disconnected")
        self.buffer += chunk
        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            try:
                self.latest_data = json.loads(line.decode())
            except json.JSONDecodeError:
                print("[Adapter] Failed to decode JSON:", line)

    def read_distance(self):
        self._receive_data()
        return self.latest_data.get("distance")
    
    