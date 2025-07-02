import keyboard
import time

from capture import capture_screen
from ocr import extract_text

print('Press s to capture, q to quit')
while True:
  if keyboard.is_pressed('q'):
    break
  if keyboard.is_pressed('s'):
    #path = capture_screen()
    #text = extract_text(path)
    text = extract_text('./screenshots/jpn.png')
    while keyboard.is_pressed('s'):
      time.sleep(0.1)
  time.sleep(0.05)
print('Loop ended')