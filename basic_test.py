import os

def open_terminal():
    if os.name == 'posix':  # Linux
        os.system('gnome-terminal')  # You may need to adjust this command based on your Linux distribution
    elif os.name == 'nt':  # Windows
        os.system('cmd')

if __name__ == "__main__":
    open_terminal()
