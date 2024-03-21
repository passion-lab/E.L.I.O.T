# PACKAGES

# - Initializing Packages
import pyttsx3  # for TTS
from speech_recognition import Microphone, Recognizer

# - Addons


# INITIALIZATIONS

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # gets a list of installed voices
engine.setProperty('voice', voices[0].id)  # voices[0] for Microsoft David
engine.setProperty('rate', 180)  # speaking rate at words per minute


# FUNCTIONS
# - Initializing Functions


def speak(text: str) -> bool:
    """
    Prints and speaks a given text by striping the former or later spaces (if available).
    :param text: Texts for saying aloud
    :return: True (if spoken) / False (if not any to speak)
    """

    _text = text.strip()

    if _text:
        engine.say(_text)
        print(_text)
        engine.runAndWait()
        return True

    else:
        return False


def listen() -> str | None:
    with Microphone() as source:
        print("Listening ...")
        Recognizer().pause_threshold = 0.5
        _voice = Recognizer().listen(source, 0)

    try:
        print("Recognizing ...")
        query = Recognizer().recognize_google(_voice, language='en-in')
        print(f">_ {query}\n")

    except Exception as e:
        print("Sorry, say that again please ...")
        return None

    return query


if __name__ == '__main__':

    while True:
        try:
            prompt = listen().lower()
        except AttributeError:
            continue
