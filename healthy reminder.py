print("\t\t welcome, your health is crucial. Use this software to keep yourself aware during long on screen hours")
import timeit
import time
from pygame import mixer
from datetime import datetime
initial=time.time()
initial1=time.time()
future=initial+1645.6
future2=initial1+2400
def water():
  global initial
  global future
  mixer.init()
  mixer.music.load ('C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3')
  mixer.music.play(1)
  num=input(" Reminder drink water: ")
  if num=='drank':
    mixer.music.stop()
    initial=time.time()
    future=initial+1645.6

def exercise():
    global initial1
    global future2
    mixer.init()
    mixer.music.load('C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3')
    mixer.music.play(1)
    num = input(" Reminder eye exercise: ")

    if num == 'exercise':
        mixer.music.stop()
        initial1 = time.time()
        future2 = initial1 + 2400

def log():
    with open("timer.txt","a") as f :
        z=input("Enter water or exercise: ")
        f.write(f"{datetime.now()}:{z}")
        f.write("\n")


while True:
  # while time.time()<future:
   #   pass



   if time.time()>future:
      water()
      log()



   if time.time()>=future2:
       exercise()
       log()




