import pysynth

# Reminders for using psynth:
# 1. Always refresh before running the code to make sure a new wav file is generated
# 2. Do not click on the wav file until the program is finished running (you'll see an orange arrow in the console when it completes)

'''
User inputs note and duration.

b    quarter -> append (b, 4) to song list
'''

song = []

durations = {"whole": 1, "quarter": 4, "half": 2, "eigth": 8, "sixteenth": 16, "dotted quarter": -4, "dotted half": -2, "dotted eigth": -8, "dotted sixteenth": -16}

while True:
  note = input("Give the note and write stop if you want to quit: ")
  if note == "stop":
    break
  duration = input("Give the duration and write stop if you want to quit: ")
  if duration == "stop":
    break
  song.append((note, durations[duration]))

pysynth.make_wav(song, fn=("song.wav"))

