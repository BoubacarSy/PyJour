import os
import json
from os import makedirs

from numpy import append

chemin = "/home/bbcr/PyLearn/PyFile2.json"
with open(chemin,"r") as f:
   # json.dump(list(range(10)),f,indent=4)
    liste = json.load(f)
liste.append(11)

with open(chemin,"w") as f:
    json.dump(liste,f,indent=4)