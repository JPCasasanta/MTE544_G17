# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
import math

def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file() 

    slice=values[30]

    angle_min=slice[0]
    angle_max=slice[1]
    angle_increment=slice[2]
    range_min=slice[3]
    range_max=slice[4]
    time=slice[5]

    x_list = []
    y_list = []

    angle = angle_min
    for i in range(6, len(slice)):
        
        range_cur = slice[i]
        if (range_cur <= range_max and range_cur >= range_min):
            x = range_cur * math.cos(angle)
            y = range_cur * math.sin(angle)
            x_list.append(x)
            y_list.append(y)

        angle = angle + angle_increment

    
    plt.plot(x_list, y_list)
        
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend()
    plt.grid()
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)
