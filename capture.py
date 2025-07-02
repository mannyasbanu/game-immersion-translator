import mss
import mss.tools
import datetime
import os

# Import configurations
from config import MONITOR, OUTPUT_DIR

def capture_screen():
  # Create directory unless it exists
  os.makedirs(OUTPUT_DIR, exist_ok=True)
  # Run context manager
  with mss.mss() as sct:
    # Capture screen
    img = sct.grab(MONITOR)
    # Record timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Save image
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    mss.tools.to_png(img.rgb, img.size, output=filepath)
    print(f"Screenshot saved: {filepath}")
    # Return filepath for OCR
    return filepath
