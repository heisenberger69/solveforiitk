import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()
def textfromspeech():

    with m as source: r.adjust_for_ambient_noise(source)

    print("Say something!")
    with m as source: audio = r.listen(source,timeout = 3)

    value = r.recognize_google(audio)
    return value




