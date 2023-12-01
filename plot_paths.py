import matplotlib.pyplot as plt
from utilities import FileReader

def plot_paths(files):
    
    for file in files:

        headers, values = FileReader(file).read_file()
            
        time_list=[]
        
        plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
        plt.set_title("state space")

    plt.show()
    
    

if __name__=="__main__":
    names = ["manhattan.csv", "euclidean.csv"]
    plot_paths(names)
