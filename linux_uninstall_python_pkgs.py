import os

#function that will uninstall the libraries
def package_uninstaller(package):
    with open(package,'r') as f:
        pkgs = f.readlines()
        for pkg in pkgs:
            pkg_ = pkg.split('==')[0] 
            response = os.system(f'sudo pip uninstall {pkg_}')
            print(f'for package {pkg_} response is : {response}')
#main function
def main():
    pip_freeze = 'PIP-FREEZE.txt'
    package_uninstaller(pip_freeze)
    
if __name__ == '__main__':
    main()
