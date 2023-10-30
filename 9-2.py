""" import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)


#1 서버에 접속하기 위한 소켓을 생성한다.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 서버에 접속을 시도한다.
clientSocket.connect(ADDR)
print('connect is success') """

""" import socket
import sys

import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))

clientSocket.close() """

""" import socket
import sys

import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))

clientSocket.close() """
""" 
# 속성 출력

class Person :
    name = "python"
    age = 23
    number = "01012345678"
    
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number) """

""" class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce()) """

""" # 클래스 초기화
class Person :
    def __init__ (self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        
        
p = Person("Hello", 24, "01087654321")
p1 = Person("he", 21, "0108")
p2 = Person("hee", 24, "87654321")

print(p.name)
print(p1.name)
print(p2.name) """

""" def __init__ (self, name, age, number):
     self.name = name
     self.age = age
     self.number = number
     Person.count +=1
     
classmethod
def getCount(cls) :
    return cls.count

p = Person("hello", 24, "01087654321")
print(p.name)
print(p.getCount)
p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.getCount)
p2 = Person("hee", 24, "0287654321")
print(p2.name)
print(p2.getCount) """