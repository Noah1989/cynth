# just playing around with wave generation...

import wave
import math
import struct

output = wave.open('test.wav', 'w')

output.setnchannels(1)
output.setsampwidth(2)
output.setframerate(44100)

for x in xrange(10000):
    output.writeframes(struct.pack('h', int(math.sin(x/50.0)*32768)))

output.close()
