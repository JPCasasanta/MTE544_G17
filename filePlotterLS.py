# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
import math

def plot_errors(filename, title):
    
    headers, values=FileReader(filename).read_file() 

    #arbitrarily choose the laser scan data at row 30 to plot in 2D
    slice=values[30]

    #extract information to process laser data
    angle_min=slice[0]
    angle_max=slice[1]
    angle_increment=slice[2]
    range_min=slice[3]
    range_max=slice[4]
    time=slice[5]

    x_list = []
    y_list = []

    #start at the initial laser scan angle, convert each detected distance at each angle into cartesian coordinates
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
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Laser Scan Data Snapshot for " + title)
    #plt.legend()
    plt.grid()
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    parser.add_argument('--title', nargs=1, required=True)
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename, args.title[0])
