#!/usr/bin/env python3

import argparse

def hello():
  print("Hello World!")

class Hello(object):
  def __init__(self, name='world'):
    self.name = name

  def hello(self):
    print("Hello %s!" % self.name)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Hello greeter')
  parser.add_argument('--name', default="World", help='Name to greet')
  args = parser.parse_args()
  hello()
  h = Hello(args.name)
  h.hello()
