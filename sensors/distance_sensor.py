import socket
import time
import json
from addresses import DISTANCE_ADDRESS


class EndEffectorSensor:
    def __init__(self, DISTANCE_ADDRESS, delay=1):
        self.delay = delay
        self.server_address = DISTANCE_ADDRESS
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.server_address)
        self.server.listen(1)
        print(f"Distance sensor waiting for client on {DISTANCE_ADDRESS}...")
        
        print("Client connected to distance sensor!")

    def send_pos(self):
        while True:
            print("[EndEffectorSensor] Waiting for client...")
            connection, client_address = self.server.accept()
            print(f"[EndEffectorSensor] Client connected: {client_address}")
            
            try:
                while True:
                    data = {
                        "x": 50 + (time.time() % 10),
                        "y": 50 + (time.time() % 10),
                    }
                    connection.sendall((json.dumps(data) + "\n").encode())
                    time.sleep(self.delay)
            except (BrokenPipeError, ConnectionResetError):
                print("[EndEffectorSensor] Client disconnected.")
                connection.close()
