import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from robot_interface import LINK_1_LENGTH, LINK_2_LENGTH

class TwoRVisualizer:
    def __init__(self, adapter, LINK_1_LENGTH, LINK_2_LENGTH):
        self.adapter = adapter
        self.l1 = LINK_1_LENGTH
        self.l2 = LINK_2_LENGTH

        # Matplotlib setup
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(- (LINK_1_LENGTH + LINK_2_LENGTH), (LINK_1_LENGTH + LINK_2_LENGTH))
        self.ax.set_ylim(- (LINK_1_LENGTH + LINK_2_LENGTH), (LINK_1_LENGTH + LINK_2_LENGTH))
        self.line, = self.ax.plot([], [], "o-", lw=3)

    def fk(self, theta1, theta2):
        x1 = self.l1 * math.cos(theta1)
        y1 = self.l1 * math.sin(theta1)
        x2 = x1 + self.l2 * math.cos(theta1 + theta2)
        y2 = y1 + self.l2 * math.sin(theta1 + theta2)
        return (0, x1, x2), (0, y1, y2)

    def update(self, frame):
        theta1, theta2 = self.adapter.read_angles()
        xs, ys = self.fk(theta1, theta2)
        self.line.set_data(xs, ys)
        return self.line,

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=100, blit=True)
        plt.show()


