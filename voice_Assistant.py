import gtts
import playsound

def text_to_audio(text, language='en', output_file='output.mp3'):
    # Create a gTTS object with the text and language
    sound = gtts.gTTS(text=text, lang=language)    
    # Save the audio to the specified file
    sound.save(output_file)
    print(f"Text converted to audio and saved as '{output_file}'.")
    # Play the audio
    playsound.playsound(output_file)

if __name__ == "__main__":
    # Enter the text below
    input_text = input("Enter the Text")
    # Call the function to convert the text to audio and play it
    text_to_audio(input_text)
