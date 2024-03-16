import os
import socket
import subprocess

def getuser():
    return os.getlogin()

def getpcname():
    return socket.gethostname()

def sizecmd():
    return os.get_terminal_size()

def startpath(path):
    return os.startfile(path)

def current_path():
    return os.path.dirname(os.path.abspath(__file__))

def open(path):
    return subprocess.Popen(path)

def delete(path):
    return os.remove(path)
