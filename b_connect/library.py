import pandas as pd
import numpy as np
import random

notes = np.arange(0,20.25,0.25)

notes = notes.tolist()

print(type(notes[1]))

mention = ['Tres_faible','Faible','Insuffisant','Mediocre','Passable','Assez_bien','Bien','Tres_Bien','Excellent','Parfait']

mentions = [i.upper() for i in mention]

print(mentions)

grade = {m:i+1 for i,m in enumerate(mentions)}

print(grade)

def generate_notes(mention):
    if mention == 1 :
        print("a")
