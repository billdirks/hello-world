#!/usr/bin/env python3

def hello():
  print("Hello World!")

class Hello(object):
  def __init__(self, name='world'):
    self.name = name

  def hello(self):
    print("Hello %s!" % self.name)

if __name__ == '__main__':
  hello()
  h = Hello('George')
  h.hello()
