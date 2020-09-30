import pyautogui, win32api

state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)
while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    if a != state_left:
        state_left = a
        if a < 0:
            f=open("positions.txt", "a")
            f.write(str(pyautogui.position())+"\n")
            f.close()
    if b != state_right:
        state_right = b
        if b < 0:
            break