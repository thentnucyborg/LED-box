import time

import matplotlib.patches as patches
import matplotlib.pyplot as plt


class TwoDPlot:
    def __init__(self, byte_array):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.hex_array = self.byte_to_hex(byte_array)
        self.render()

    def render(self):
        self.ax.clear()
        x_pos = 0.6
        y_pos = 0.6
        x_size = 0.8
        y_size = 0.8
        k = 0
        for i in range(len(self.hex_array)):
            p = patches.Rectangle((x_pos, y_pos), x_size, y_size, facecolor=self.hex_array[i], edgecolor="black",
                                  linewidth=2)
            self.ax.add_patch(p)
            if k == 9:
                y_pos += y_size + 0.2
                x_pos = 0.6
                k = 0
            else:
                x_pos += x_size + 0.2
                k += 1
        plt.ylim([0, 7])
        plt.xlim([0, 11])
        plt.draw()
        plt.pause(0.00000001)

    def byte_to_hex(self, byte_array):
        hex_array = byte_array.hex()
        output = [0] * 60
        for i in range(0, int(len(hex_array)), 6):
            hex_string = '#'
            for j in range(6):
                hex_string += hex_array[i + j]
            output[int(i / 6)] = hex_string
        return output


if __name__ == '__main__':
    test_array = [bytearray([255, 0, 0] * 60), bytearray([0, 255, 0] * 60), bytearray([0, 0, 255] * 60)]
    # start loop
    for byte_array in test_array:
        TwoDPlot(byte_array)
        time.sleep(1)
