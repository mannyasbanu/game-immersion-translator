import keyboard
import time

from capture import capture_screen
from ocr import extract_text
from translate import translate_text
from tts import tts

print('Press s to capture, q to quit')
# Program loop
while True:
  # Exit when q pressed
  if keyboard.is_pressed('q'):
    break
  if keyboard.is_pressed('s'):
    # Translate Japanese onscreen text to English TTS
    path = capture_screen()
    text = extract_text(path)
    english = translate_text(text)
    tts(english)
    # Prevent key hold down
    while keyboard.is_pressed('s'):
      time.sleep(0.1)
  time.sleep(0.05)
print('Program ended')