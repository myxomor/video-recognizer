#!/usr/bin/env python3

from multiprocessing.dummy import Pool
from vosk import Model, KaldiRecognizer

import sys
import os
import wave
import json
import subprocess
import datetime

model = Model("model")

def recognize(line):
    uid, fn = line.split()
    print(fn)
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            fn,
                            '-ar', '16000' , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)

    rec = KaldiRecognizer(model, 16000)

    text = ""
    print("start process")
    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            jres = json.loads(rec.Result())
            text = text + " " + jres['text']
    jres = json.loads(rec.FinalResult())
    text = text + " " + jres['text']
    return (uid + text)

def main():
    p = Pool(8)
    prev = datetime.datetime.now()
    texts = p.map(recognize, open(sys.argv[1]).readlines())

    print ("\n".join(texts))
    now = datetime.datetime.now()
    time = now - prev
    print(str(time)) 

main()