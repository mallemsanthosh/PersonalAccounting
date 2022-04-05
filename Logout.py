import sys
import os
class Logout:
    def Logout():
        python = sys.executable
        os.execl(python, python, * sys.argv)