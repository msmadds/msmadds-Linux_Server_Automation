import paramiko
from paramiko import ssh_exception
import os
import  getpass

#give the script a full vlan range, and the script test to see if an IP is availabe by ping, in that range
#and for the IP that is available  by ping to ssh into the Linux server and run the linux command to get the info on that machine 




def get_info(hostname, password, username, port, commands):
    """ The function to check the  """
    for x in range(0, 255, 1):#range of the IP you want to start checking
        y = str(x)
        response = check_ip_availability(hostname+y)
        if response == 0:
            host = hostname + y
            try:
                #open the ssh connection 
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host,port,username,password)
                for command in commands:
                    stdin,stdout,stderr = ssh.exec_command(command)
                    lines = stdout.readlines()
                    with open(host+'.txt', 'a') as f: #open the file to store the output, naming the  file  by using the hostname
                        f.write('*'*30 + f"{command}" + "*"*30)
                        f.write('\n')
                        for line in lines:
                            f.write(line)
                            
            except ssh_exception.AuthenticationException: 
                #capture the paramiko authentication exception
                print("Authentication failed, check credentials")
                
def  check_ip_availability(hostname):
        
    #check if the the IP  is available by ping
    response = os.system("ping -c 1 " + hostname + "> /Users/User/Documents/AUTOMATION/output.txt" ) 
     #if the IP is available the response of the ping will be 0, so the below block will be executed
    return response
    

def main():
    #main function
    port = 22
    username = input("Input the username")
    password = getpass.getpass()
    commands =['cat /etc/debian_version', 'cat /etc/passwd', 'ls']
    hostname = "xx.xx.xx." #input the three octacte of your IP 
    get_info(hostname, password, username, port, commands)
    
    
if __name__ == "__main__":
    main()
