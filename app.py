import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Main function
def main():
    speak("Hello, I am your simple voice assistant. How can I help you today?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "thank you" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
