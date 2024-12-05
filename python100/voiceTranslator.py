import googletrans
import speech_recognition
import gtts
import playsound
import LooseVersion

recognizer= speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")

    voice = recognizer.listen(source)
    text = recognizer.recognize_google_cloud(voice,language='fr')
    print(text)
#print(googletrans.LANGUAGES)

translator = googletrans.Translator()
translation = translator.translate(text,dest='fr')
print(translation)

