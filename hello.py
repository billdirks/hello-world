#!/usr/bin/env python3

import argparse

class Hello(object):
  def __init__(self, name='world'):
    self._name = name

  def hello(self):
    print("Hello %s!" % self._name)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Hello greeter')
  parser.add_argument('--name', default="World", help='Name to greet')
  args = parser.parse_args()
  h = Hello(args.name)
  h.hello()
