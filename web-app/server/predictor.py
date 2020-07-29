import ktrain
import pandas as pd
import sys
import os
import socket
import pickle

def block_print(): sys.stdout = open(os.devnull, 'w')
def enable_print(): sys.stdout = sys.__stdout__

model_off = ktrain.load_predictor('../pred/ft5m_off/')
model_cw = ktrain.load_predictor('../pred/ft5m_cw')
model_sa = ktrain.load_predictor('../pred/ft5m_sa')

def start_server():
  port = 5050
  s = socket.socket()
  s.bind(('', port))
  
  print('listening port ', port)
  s.listen(5)
  block_print()
  while True:
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    data = c.recv(1024).decode('utf-8')
    if not data: break
    data = get_predictions(data)
    c.send(pickle.dumps(data))
  s.close()


def get_predictions(text):
  probs_off = model_off.predict_proba(text)
  probs_cw = model_cw.predict_proba(text)
  probs_sa = model_sa.predict_proba(text)

  predictions = [
    probs_off,
    probs_cw,
    probs_sa
    # "off": {
    #   "neg": str(probs_off[0]),
    #   "pos": str(probs_off[1])
    # },
    # "cw": {
    #   "neg": str(probs_cw[0]),
    #   "pos": str(probs_cw[1])
    # }
  ]

  return predictions

if __name__ == '__main__':
  start_server()
