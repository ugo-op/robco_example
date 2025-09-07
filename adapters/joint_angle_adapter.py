
# joint_angle_adapter.py
import socket
import json
from addresses import JOINT_ANGLE_SENSOR_ADDRESS


class JointAngleAdapter:
    def __init__(self, JOINT_ANGLE_SENSOR_ADDRESS):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(JOINT_ANGLE_SENSOR_ADDRESS)
        self.buffer = b""
        self.latest_data = {}

    def _receive_data(self):
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

    def read_angles(self):
        self._receive_data()
        return (self.latest_data.get("theta1"), self.latest_data.get("theta2"))

