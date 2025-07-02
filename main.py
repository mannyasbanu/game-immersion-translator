import keyboard
import time

from capture import capture_screen

print('loop started, s to screenshot, q to exit')
while True:
  if keyboard.is_pressed('q'):
    break
  if keyboard.is_pressed('s'):
    path = capture_screen()
    while keyboard.is_pressed('s'):
      time.sleep(0.1)
  time.sleep(0.05)
print('loop ended')