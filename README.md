# msmadds-Linux_Server_Automation
Getting information from the linux servers

Script: Getting_info_using_paramiko.py 
The script is given a range of VLAN(IP address), and it will iterate through all the IPs, and use OS library to ping each IP. If an IP is available by ping it will use Paramiko library to ssh into the servers and run a list/or a single linux command and store the output in a file and it will name that file with the IP address. Helpful script for when you have a lot of servers that you need to pull info from.

Script: Linux_uninstall_python_pkgs.py
The scripts can be used when you require to uninstall all the /some of the libraries already installed in your linux machine. It uses OS library to sed the "sudo pip uninstall <pkg name>". Return response 0 if the uninstall was succesful. The script depend on another file that in it you can storenthe output of "pip freeze", and it will read this file and extract just the name of the package.
Sample of the 'pip freeze' output expected:
ipython==8.11.0
itsdangerous==2.1.2
jedi==0.18.2
Jinja2==3.1.3
jsonpickle==3.0.4
junos-eznc==2.7.1
lxml==5.2.2
markdown-it-py==2.2.0
