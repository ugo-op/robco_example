# joint_angle_sensor.py
import socket
import json
import time
import math
from addresses import JOINT_ANGLE_SENSOR_ADDRESS



class JointAngleSensor:
    def __init__(self, JOINT_ANGLE_SENSOR_ADDRESS):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(JOINT_ANGLE_SENSOR_ADDRESS)
        self.server.listen(1)
        print(f"[JointAngleSensor] Listening on {JOINT_ANGLE_SENSOR_ADDRESS}...")
        self.conn, _ = self.server.accept()
        print("[JointAngleSensor] Client connected!")

    # def run(self):
    #     while True:
    #         try:
    #             theta1 = float(input("Enter theta1 (radians): "))
    #             theta2 = float(input("Enter theta2 (radians): "))
    #             data = {"theta1": theta1, "theta2": theta2}
    #             self.conn.sendall((json.dumps(data) + "\n").encode())
    #         except Exception as e:
    #             print("Error:", e)
    #             break
            
    def run(self):
        t = 0.0
        while True:
            theta1 = math.sin(t)          # joint 1 oscillates
            theta2 = math.cos(t/2)        # joint 2 moves slower
            data = {"theta1": theta1, "theta2": theta2}
            self.conn.sendall((json.dumps(data) + "\n").encode())
            time.sleep(0.1)
            t += 0.1
