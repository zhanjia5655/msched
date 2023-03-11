
import zerorpc
MASTERURL='tcp://127.0.0.1:9000'
class Master:
    def hello(self,msg):
        return msg
server=zerorpc.Server(Master())
server.bind(MASTERURL)
server.run() #主线程上跑 start 启动一个新子线程