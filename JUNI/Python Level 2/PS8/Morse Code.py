import pysynth

# Reminders for using psynth:
# 1. Always refresh before running the code to make sure a new wav file is generated
# 2. Do not click on the wav file until the program is finished running (you'll see an orange arrow in the console when it completes)

morseDict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
             "z": "--..", " ": "    "}


# 1. Define a function that takes in a message and converts that message into morse code. (Make sure to put extra spaces inbetween your words.) Using the function, ask the user for a message and print out the translated message.

# 2. Define a function that takes in a message and converts that message into musical morse code. Each dot should be a C for an eighth note, and each dash should be a C for a half note. Rest for a half note inbetween each word and an eighth note between each dot or dash.

def morsemaker():
    msg = input("Give any message: ")
    lmsg = len(msg)
    global morsemsg
    morsemsg = ""
    for i in range(lmsg):
        morsemsg += str(morseDict[msg[i]]) + " "

    print(morsemsg)


morsemaker()

morseDictSounds = {"-": 2, ".": 8, " ": 1}

sounds = []


def MorseSound():
    for i in morsemsg:
        print(i)
        if i == " ":
            note = "r"
        else:
            note = "c"
        sounds.append((note, morseDictSounds[i]))

    pysynth.make_wav(sounds, fn=("song.wav"))


MorseSound()
