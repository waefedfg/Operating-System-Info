import os
import platform
import sys
import getpass


print('----------------------------------------------------')
print('Os =', platform.system())
print('Files =', os.listdir())
print('Name of Current User =', getpass.getuser())
print('System version =', sys.version)
print('Your location is', os.getcwd())

