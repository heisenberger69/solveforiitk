import speech_recognition as sr


def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = sr.listen(source)

    try:
        text = sr.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError as e:
        print(f"Request error: {e}")

    return ""


recognized_text = recognize_speech_from_mic()
print("Recognized text:", recognized_text)
