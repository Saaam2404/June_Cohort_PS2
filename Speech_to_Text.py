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
            #print("Speech was not clear!!")
            #print("Try again!!")
            return None
        except sr.WaitTimeoutError:
            #print("Time over....You did not speak anything")
            return None
        except OSError:
            #print("Microphone not found!!")
            return None
        except Exception:
            #print("Something unexpected happened!!")
            return None
