import os
import platform
import sys
import getpass
import socket

print('----------------------------------------------------')
print('Os =', platform.system())
print('Files =', os.listdir())
print('Name of Current User =', getpass.getuser())
print('System version =', sys.version)
print('Your directory path is', os.getcwd())
print('Computer Host =', socket.gethostname())
