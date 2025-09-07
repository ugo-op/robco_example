from adapters.camera_adapter import CameraAdapter
from adapters.distance_adapter import DistanceAdapter
from adapters.joint_angle_adapter import JointAngleAdapter
from sensors.joint_angle_sensor import JointAngleSensor
from addresses import CAMERA_ADDRESS, DISTANCE_ADDRESS, JOINT_ANGLE_SENSOR_ADDRESS
import math

# 2R Planer Robot Interface
LINK_1_LENGTH = 0.5
LINK_2_LENGTH = 0.5



class RobotInterface:
    def __init__(self):
        pass
        # self.distance_adap = DistanceAdapter(DISTANCE_ADDRESS)
        
    def start_angle_sensor(self):
        sensor = JointAngleSensor(JOINT_ANGLE_SENSOR_ADDRESS)
        sensor.run()
        
    def get_joint_angles(self):
        self.joint_angle_adap = JointAngleAdapter(JOINT_ANGLE_SENSOR_ADDRESS)
        return self.joint_angle_adap.read_angles()
    
    def get_end_effector_position(self):
        # Forward kinematics
        theta_1, theta_2 = self.get_joint_angles()
        x_pos = (LINK_1_LENGTH * math.cos(theta_1)) + (LINK_2_LENGTH * math.cos(theta_1 + theta_2))
        y_pos = (LINK_1_LENGTH * math.sin(theta_1)) + (LINK_2_LENGTH * math.sin(theta_1 + theta_2))
        return x_pos, y_pos

    def get_distance(self):
        # redundant, for verification
        return self.distance_adap.read_distance()
    
