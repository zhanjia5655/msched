import  zerorpc
import threading
from .config import CONNECTIONURL
from utils import getlogger

logger = getlogger(__name__,'C:/Users/zhanjia/PycharmProjects/msched/agent.cmd.log')

class ConnectionManage:
    def __init__(self):
        self.client =zerorpc.Client()
        self.event= threading.Event()
    def start(self,timeout=None):
        self.client.connect(CONNECTIONURL)
        while not self.event.wait(timeout):
            pass
    def shutdown(self):
        self.event.set()
        self.client.close()


