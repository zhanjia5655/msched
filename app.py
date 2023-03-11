import  zerorpc
import threading
client=zerorpc.Client()
client.connect('tcp://127.0.0.1:9000')
e=threading.Event()
# while True:
#     res=client.hello('zhanjia')
#     print(res,type(res))
#     e.wait(3)

print('~~~~~~~~~~~~~~~ \n')
print('~~~~~~~~~~~~~~~ \n')
# client.close()

