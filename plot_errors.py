import matplotlib.pyplot as plt
from utilities import FileReader

def plot_errors_Kalman():
    headers, values=FileReader("robotPose.csv").read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    
    
    fig, axes = plt.subplots(2,1, figsize=(14,6))


    axes[0].plot([lin[len(headers) - 5] for lin in values], [lin[len(headers) - 4] for lin in values])
    axes[0].set_title("state space")
    axes[0].grid()

    
    axes[1].set_title("each individual state")
    for i in range(0, len(headers) - 1):
        axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i])

    axes[1].legend()
    axes[1].grid()

    plt.show()
    
    fig, axes = plt.subplots(2,1, figsize=(14,6))

    axes[0].set_title("a_x Comparison")
    axes[0].plot(time_list, [lin[0] for lin in values], label= headers[0])
    axes[0].plot(time_list, [lin[2] for lin in values], label= headers[2])
    axes[0].legend()
    axes[0].grid()


    
    axes[1].set_title("a_y Comparison")
    axes[1].plot(time_list, [lin[1] for lin in values], label= headers[1])
    axes[1].plot(time_list, [lin[3] for lin in values], label= headers[3])
    axes[1].legend()
    axes[1].grid()

    plt.show()


    fig, axes = plt.subplots(2,1, figsize=(14,6))


    axes[0].set_title("w Comparison")
    axes[0].plot(time_list, [lin[5] for lin in values], label= headers[5])
    axes[0].plot(time_list, [lin[9] for lin in values], label= headers[9])
    axes[0].legend()
    axes[0].grid()



    axes[1].set_title("v Comparison")
    axes[1].plot(time_list, [lin[4] for lin in values], label= headers[4])
    axes[1].plot(time_list, [lin[8] for lin in values], label= headers[8])
    axes[1].legend()
    axes[1].grid()


    plt.show()

def plot_errors():
    
    headers, values=FileReader("raw_path.csv").read_file()
    #headers, values=FileReader("./robotPoses/manhattan_close_robotPose.csv").read_file()

    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    fig, axes = plt.subplots(2,1, figsize=(14,6))


    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].set_title("state space")
    axes[0].grid()


    for i in range(0, len(headers) -1):
        axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i])

    axes[1].legend()
    axes[1].grid()

    plt.show()
    
    

if __name__=="__main__":
    plot_errors()
    #plot_errors_Kalman()