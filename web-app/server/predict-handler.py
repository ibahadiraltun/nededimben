import socket
import pickle
import sys
import os

def block_print(): sys.stdout = open(os.devnull, 'w')
def enable_print(): sys.stdout = sys.__stdout__

block_print()

def start_client():
  print('start client')
  port = 5050
  s = socket.socket()
  s.connect(('127.0.0.1', port)) 
  print('connection clien on port 5050')
  
  message = ' '.join(sys.argv[1:])
  print('message', message)
  s.send(message.encode('utf-8'))
  print('sending')
  data = pickle.loads(s.recv(1024))
  print('data')

  enable_print()
  print('[[\"off\", [{}, {}]], [\"cw\", [{}, {}]], [\"sa\", [{}, {}, {}]]]'.format(
    data[0][0], data[0][1], data[1][0], data[1][1], data[2][0], data[2][1], data[2][2])
  )
  block_print()
  
  s.close()

if __name__ == '__main__':
  start_client()
