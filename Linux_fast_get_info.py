import paramiko
from paramiko import ssh_exception
import os
import  getpass
import time
import nmap

#Ths part of code is runs faster than the first version by using the nmap library
#give the script a full vlan range, and the script test to see if an IP is availabe by ping, in that range
#and for the IP that is available  by ping to ssh into the Linux server and run the linux command to get the info on that machine 




def get_info(hostname, password, username, port, commands):
    """ The function to check to get the info from the linux server """
    try:
        #open the ssh connection 
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        for command in commands:
            stdin,stdout,stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            try:
                os.makedirs(hostname)
                file_ = hostname + '/'+hostname+'.txt'
                with open(file_, 'a') as f: #open the file to store the output, naming the  file  by using the hostname
                    f.write('*'*30 + f"{command}" + "*"*30)
                    f.write('\n')
                    for line in lines:
                        f.write(line)
            except FileExistsError:
                file_ = hostname + '/'+hostname+'.txt'
                with open(file_, 'a') as f: #open the file to store the output, naming the  file  by using the hostname
                    f.write('*'*30 + f"{command}" + "*"*30)
                    f.write('\n')
                    for line in lines:
                        f.write(line)
                        
                        
                            
    except ssh_exception.AuthenticationException: 
                #capture the paramiko authenti cation exception
                print(f"Authentication failed for {hostname}, check credentials")


def check_ip_availability(hostname):
    nm = nmap.PortScanner()
    nm.scan(hosts = hostname, arguments = '-sn')
    hosts = nm.all_hosts()
    return hosts
    

def main():
    #main function
    start = time.time()
    port = 22 #specify the ssh port if not the default 22
    username = input("Input the username: ")
    password = getpass.getpass()
    #commands =['cat /etc/debian_version', 'cat /etc/passwd', 'ls'] 
    #either have a list of linux commands that you want to run in the above list, or a single command in the below. 
    commands =['cat /etc/passwd']
    hostname = "xx.xx.xx.0/24" #input the range of your IP 
    
    hosts = check_ip_availability(hostname)
    #print(hosts)
    for host in hosts:#range of the IP you want to start checking
        print(host)
        get_info(host, password, username, port, commands)
        
    end= time.time()
    total_time = end - start
    print(str(total_time))
    
    
if __name__ == "__main__":
    main()
