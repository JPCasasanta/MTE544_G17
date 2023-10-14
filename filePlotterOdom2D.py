# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
from utilities import FileReader
import math

def plot_errors(filename, title):
    
    headers, values=FileReader(filename).read_file() 

    x_list = []
    y_list = []

    for value in values:
        
        x = value[0]
        y = value[1]

        x_list.append(x)
        y_list.append(y)
    
    plt.plot(x_list, y_list)
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Odometry Data for " + title)
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
