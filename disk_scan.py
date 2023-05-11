import socket
from subprocess import check_output
from itertools import zip_longest

class DiskScan():

    def localdisk(hostname):
        kname = check_output(("lsblk", "-io", "KNAME"))
        print(kname)

DiskScan.localdisk(hostname = socket.gethostname())