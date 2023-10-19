import pysynth

# Reminders for using psynth:
# 1. Always refresh before running the code to make sure a new wav file is generated
# 2. Do not click on the wav file until the program is finished running (you'll see an orange arrow in the console when it completes)

# example:
#potter = [('b3', 4), ('e', -4), ('g', 8), ('f#', 4), ('e', 2), ('b', 4), ('a', -2), ('f#', 2)]
#pysynth.make_wav(potter, fn='potter.wav')

# write the code to build your own song below:

avengers = [('e', 1), ('b', 4), ('a', -8), ('g', 16), ('g', 4), ('a', -8), ('b', 16), ('b', 4), ('e', -2), ('b', 4), ('a', -8), ('g', 16), ('g', 4), ('f#', 4), ('e', 1), ('b', 4), ('a', -8), ('g', 16,), ('g', 4), ('a', -8), ('b', 16), ('b', 4), ('e', -2), ('b', 4), ('a', -8), ('g', 16), ('g', 4), ('f#', 4), ('e5', 1), ('b5', 4), ('a5', -8), ('g5', 16), ('g5', 4), ('a5', -8), ('b5', 16), ('b5', 4), ('e5', -2), ('b5', 4), ('a5', -8), ('g5', 16), ('g5', 4), ('f#5', 4), ('e5', 1), ('b5', 4), ('a5', -8), ('g5', 16), ('g5', 4), ('a5', -8), ('b5', 16), ('b5', 4), ('e5', -2), ('b5', 4), ('a5', -8), ('g5', 16), ('g5', 4), ('f#5', 4)]

pysynth.make_wav(avengers, fn='avengers.wav')

