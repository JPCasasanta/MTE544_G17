from math import atan2, asin, sqrt

M_PI=3.1415926535

class Logger:
    def __init__(self, filename, headers=["e", "e_dot", "e_int", "stamp"]):
        self.filename = filename

        with open(self.filename, 'w') as file:
            header_str=""

            for header in headers:
                header_str+=header
                header_str+=", "
            
            header_str+="\n"
            
            file.write(header_str)

    #log one row of data in specified file using list of values from callback function
    def log_values(self, values_list):

        with open(self.filename, 'a') as file:
            vals_str=""

            #iterate through list of values from callback function and compile a comma separated string of values for one row
            for value in values_list:
                vals_str += str(value) + ','
            
            vals_str+="\n"
            
            #write row of values to file
            file.write(vals_str)
            

    def save_log(self):
        pass

class FileReader:
    def __init__(self, filename):
        
        self.filename = filename
        
        
    def read_file(self):
        
        read_headers=False

        table=[]
        headers=[]
        with open(self.filename, 'r') as file:
            # Skip the header line

            if not read_headers:
                for line in file:
                    values=line.strip().split(',')

                    for val in values:
                        if val=='':
                            break
                        headers.append(val.strip())

                    read_headers=True
                    break
            
            next(file)
            
            # Read each line and extract values
            for line in file:
                values = line.strip().split(',')
                
                row=[]                
                
                for val in values:
                    if val=='':
                        break
                    row.append(float(val.strip()))

                table.append(row)
        
        return headers, table


# TODO Part 5: Implement the conversion from Quaternion to Euler Angles
#returns angular orientation in z (yaw) from robot orientation quaternion
def euler_from_quaternion(quat):
    """
    Convert quaternion (w in last place) to euler roll, pitch, yaw.
    quat = [x, y, z, w]
    """
    # just unpack yaw
    siny_cosp = 2*(quat.w * quat.z + quat.x * quat.y)
    cosy_cosp = 1 - 2*(quat.y * quat.y + quat.z * quat.z)
    yaw = atan2(siny_cosp, cosy_cosp)

    return yaw


