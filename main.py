from rdkit import Chem
from rdkit.Chem import Descriptors
import random
import csv
import random
import string
with open('/Users/lydiawanek/Desktop/NO DELETE/fonts/bitter-testt.csv', newline ='') as f:
    reader = csv.reader(f)
    data = list(reader)
    f.close()


inital_pop = [''.join(x) for x in data]
first = []
second = []
p1 = []
for i in range(100):
   x = random.choice(inital_pop)
   first.append(x[:len(x) // 2])
   second.append(x[len(x) // 2:])
   tot = second + first
   p1.append(random.choice(tot) + random.choice(tot))
p2 = []
for x in p1:
   valid_ate = Chem.MolFromSmiles(x)
   if valid_ate is None:
       print('invalid')
   else:
    print('valid')
    p2.append(x)
gen1 = []
not_fit = []
meeps = []
print('length =', len(p2))
for x in p2:
    smilesstring = Chem.MolFromSmiles(x)
    logp = Descriptors.MolLogP(smilesstring)
    weight = Descriptors.ExactMolWt(smilesstring)
    donors = Descriptors.NumHDonors(smilesstring)
    acceptors = Descriptors.NumHAcceptors(smilesstring)
    score = 0
for smilesstring in p2:
    if logp <= 5:
        score +=5
    if weight <= 500:
        score += 5
    if donors <= 5:
        score += 5
    if acceptors <= 10:
        score += 5
    print(score)

for smilesstring in p2:
    if score > 20:
        gen1.append(smilesstring)
    if score < 12:
        not_fit.append(smilesstring)
print('not fit', not_fit)


f = random.choice(gen1)
def mutate(individual):
   hola = random.choice(f)
   return f.replace(hola, random.choice(string.ascii_letters), 1)
mutate(f)

for idx, item in enumerate(gen1):
   if f in item:
      gen1[idx] = mutate(f)
validgen = []
print(gen1)
from rdkit import Chem
from rdkit.Chem import Descriptors
import random
import csv
import random
import string

with open('/Users/lydiawanek/Desktop/NO DELETE/fonts/bitter-testt.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    f.close()

inital_pop = [''.join(x) for x in data]
first = []
second = []
p1 = []
for i in range(100):
    x = random.choice(inital_pop)
    first.append(x[:len(x) // 2])
    second.append(x[len(x) // 2:])
    tot = second + first
    p1.append(random.choice(tot) + random.choice(tot))
p2 = []
for x in p1:
    valid_ate = Chem.MolFromSmiles(x)
    if valid_ate is None:
        print('invalid')
    else:
        print('valid')
        p2.append(x)
gen1 = []
not_fit = []
meeps = []
print('length =', len(p2))
for x in p2:
    smilesstring = Chem.MolFromSmiles(x)
    logp = Descriptors.MolLogP(smilesstring)
    weight = Descriptors.ExactMolWt(smilesstring)
    donors = Descriptors.NumHDonors(smilesstring)
    acceptors = Descriptors.NumHAcceptors(smilesstring)
    score = 0
for smilesstring in p2:
    if logp <= 5:
        score += 5
    if weight <= 500:
        score += 5
    if donors <= 5:
        score += 5
    if acceptors <= 10:
        score += 5
    print(score)

for smilesstring in p2:
    if score > 20:
        gen1.append(smilesstring)
    if score < 12:
        not_fit.append(smilesstring)
print('not fit', not_fit)

f = random.choice(gen1)


def mutate(individual):
    hola = random.choice(f)
    return f.replace(hola, random.choice(string.ascii_letters), 1)


mutate(f)

for idx, item in enumerate(gen1):
    if f in item:
        gen1[idx] = mutate(f)
validgen = []
print(gen1)
