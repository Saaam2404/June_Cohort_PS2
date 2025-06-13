from Speech_to_Text import Voice
vc=Voice()
text=vc.speech_converter()
if text:
    print(text)
else:
    print("Try Again")