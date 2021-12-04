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
    # uid, fn = line.split()
    print(fn)
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            line,
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
            print(jres['text'])
            text = text + " " + jres['text']
    jres = json.loads(rec.FinalResult())
    text = text + " " + jres['text']
    output_sound = {'text': text}

    tr4w = TextRank4Keyword()
    tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN', 'VERB'], window_size=4, lower=False)

    print("show keywords")
    output_sound['keywords'] = tr4w.get_keywords(1.0)
    print(output_sound['keywords'])

    print("show entries")
    persons = []
    locations = []
    organizations = []
    entries = tr4w.get_ents()
    for ent in entries:
        print(ent.text, ent.label_)
        if ent.label_ == "PER":
            persons.append(ent.text)
        if ent.label_ == "LOC":
            locations.append(ent.text)
        if ent.label_ == "ORG":
            organizations.append(ent.text)

    output_sound['persons'] = persons
    output_sound['locations'] = locations
    output_sound['organizations'] = organizations

    filename_output = line + '.json'
    with open(filename_output, 'w', encoding='utf-8') as f:
        json.dump(output_sound, f, ensure_ascii=False, indent=4)
    return "ok"


def main():
    p = Pool(8)
    prev = datetime.datetime.now()
    texts = p.map(recognize, open(sys.argv[1]).readlines())

    # print ("\n".join(texts))
    # now = datetime.datetime.now()
    # time = now - prev
    # print(str(time)) 

main()
