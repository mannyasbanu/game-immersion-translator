# game-immersion-translator
A program for translating in game subtitles using a hotkey when playing with language immersion.
My goal is to translate on-screen subtitles when playing games like Persona with Japanese audio and subtitles by pressing a hotkey for difficult or uknown phrases. This avoids the hassle of looking up translations manually, while maintaining complete language immersion.

Program Flow
- Hotkey pressed
- capture.py -> grab screen, save png
- ocr.py -> read png, find characters, output text
- translate.py -> translate Japanese to English
- tts.py -> speak out translation