# pip install keyboard
import keyboard
# pip install mss
import mss
import mss.tools

def captureScreen():
  with mss.mss() as sct:
    # screen area to capture
    monitor = {
      "top": 160,
      "left": 160,
      "width": 600,
      "height": 600
    }
    # grab image
    img = sct.grab(monitor)
    output = "img.png".format(**monitor)
    # save image
    mss.tools.to_png(img.rgb, img.size, output=output)
    print(output)

print('loop started, s to screenshot, q to exit')
while True:
  if keyboard.is_pressed('q'):
    break
  if keyboard.is_pressed('s'):
    captureScreen()
  continue
print('loop ended')