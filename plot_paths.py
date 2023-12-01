import matplotlib.pyplot as plt
from utilities import FileReader

def plot_paths(files):
    
    for file in files:

        headers, values = FileReader(file).read_file()
            
        time_list=[]
        
        plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
        

    plt.title("Manhattan vs Euclidean Path Planning - Far Goal Pose")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(["Manhattan", "Euclidean"])
    plt.grid()
    plt.show()
    
    
    

if __name__=="__main__":
    names = ["./robotPoses/manhattan_exact_raw_path.csv", "./robotPoses/euclid_exact_raw_path.csv"]
    plot_paths(names)
