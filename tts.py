import pyttsx3

# Initialise engine
engine = pyttsx3.init()

# Set tts properties
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate + 0)
engine.setProperty('volume', volume + 0)

def tts(text):
  try:
    # Speak text using TTS engine
    engine.say(text)
    engine.runAndWait()
    print(f"Spoken: {text}")
  except Exception as e:
    print(f"TTS failed: {e}")
