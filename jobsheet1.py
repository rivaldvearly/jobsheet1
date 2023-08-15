import random
from guess import cek

jawaban = random.randint(1, 2)

tebakan = int(input('tebak angkja dari  1 s.d 2:'))

if cek(tebakan, jawaban):
    print("jawaban kamu benar!")
else:
    print("jawaban kamu salah!")
