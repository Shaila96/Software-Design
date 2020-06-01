import os

def read_sentences():
  file = open(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
      'data', 'input'), "r+")
  
  return file.readlines()
