# 2 ways to run a Python file (AKA module)
# 1. directly
# e.g. python main.py
# special __name__ that stores "__main__"
# 2. by importing it in another module
# e.g. main.py has a statement: import helloworld
# __name__ stores "hello_world" (name of module)
print("helloworld.__name__:", __name__)

def run():
    print("hello from run()")

if __name__ == "__main__":
    run()