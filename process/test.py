import socket
from process.config import service
import subprocess

host = socket.gethostname()
servicelist = service.get('bdp01.sa.cn')
print(servicelist)


def service_state(service):
    cmd = "ps -ef | grep %s |grep -v grep |  wc -l" % (service)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    code, err = process.communicate()
    return code


for service in servicelist:
    state = int(service_state(service).strip())
    print(state)
    if state == 0:
        print("equal")
    else:
        print("no")