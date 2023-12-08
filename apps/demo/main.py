import platform
from apps.demo.lib import DemoClass

def version():
  print(f"python version: {platform.python_version()}")

if __name__ == '__main__':
  version()
  d = DemoClass()
  print(d.demo())
  print("Hello, World!!")
