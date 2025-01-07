import pyautogui
import time
import random
import threading
from tkinter import Tk, Button


def mouseMover():
  global running
  
  while running:
    x = random.randint(0,500)
    y = random.randint(0,500)
        
    pyautogui.moveTo(x,y)
    
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
        
    print('moved at: ' + str(result) + ' (' + str(x) + ', ' + str(y) + ')')
    time.sleep(5)
    
def toggle():
  global running, thred
  
  if running:
    running = False
    toggle_btn.config(text="Activate")
  else:
    running = True
    toggle_btn.config(text="Deactivate")
    thread = threading.Thread(target=mouseMover)
    thread.deamon = True
    thread.start()

ui = Tk()
ui.title("Mouse Mover-inator")
ui.geometry("300x150")

toggle_btn = Button(ui, text="Activate", command=toggle, width=20, height = 2)
toggle_btn.pack(pady=50)

running = False
thread = None

ui.mainloop()