# proof of concept: a very simple algorithm generates complex sound creations.

import wave
import math
import struct

output = wave.open('test.wav', 'w')

output.setnchannels(2)
output.setsampwidth(2)
output.setframerate(44100)

x, y = 1.0, 0.0
dx, dy = 0.0, 1.0

for i in xrange(5000000):
    dx -= x / (abs(x) + abs(y))
    dy -= y / (abs(x) + abs(y))
    x += dx
    y += dy
    if i % 5000 == 0:
        print i, x, y, dx, dy
    output.writeframes(struct.pack('h', int(x)))
    output.writeframes(struct.pack('h', int(y)))
    
output.close()
