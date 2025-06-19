import speech_recognition as sr

class Voice:
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.microphone=sr.Microphone()
    
    def speech_converter(self):
        try:
            with self.microphone as source:
                print(".......Speak Something.......")
                speech=self.recognizer.record(source,duration=15)
                text=self.recognizer.recognize_google(speech)
                return text
        except sr.UnknownValueError:
            return None
        except sr.WaitTimeoutError:
            return None
        except OSError:
            return None
        except Exception:
            return None
