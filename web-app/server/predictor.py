import ktrain
import pandas as pd
import sys
import os
import socket
import pickle

def block_print(): sys.stdout = open(os.devnull, 'w')
def enable_print(): sys.stdout = sys.__stdout__

run_path = str(__file__).split('predictor.py')[0]

model_off = ktrain.load_predictor(run_path + '../../models/fine-tune/ft5m_off/')
model_cw = ktrain.load_predictor(run_path + '../../models/fine-tune/ft5m_cw/')
model_sa = ktrain.load_predictor(run_path + '../../models/fine-tune/ft5m_sa/')

model_off.preproc.model_name = run_path + '../../models/bert/bert-model5M/'
model_cw.preproc.model_name = run_path + '../../models/bert/bert-model5M/'
model_sa.preproc.model_name = run_path + '../../models/bert/bert-model5M/'

def start_server():
  port = 5050
  s = socket.socket()
  s.bind(('', port))
  
  print('Predictor is listening port {}...'.format(port))
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
  ]

  return predictions

if __name__ == '__main__':
  start_server()
