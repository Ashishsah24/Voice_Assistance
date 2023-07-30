import gtts
import playsound
text = "Hello, My name is Ashish Sah."
sound = gtts.gTTS(text, lang='en')
sound.save("Welcome.mp3")
playsound.playsound("Welcome.mp3")