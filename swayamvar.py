import random
import string 

def generateRandoms(n):
    persons = []
    for i in range(n):
        r = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        obj ={
            "name" : r
        }
        persons.append(obj)
    print(persons)
    return persons

def getRound1Scores(persons):
    for person in persons:
        person['round1'] = {}
        person['round1']['Family_Personal_Profile'] = random.randint(0,100)
        person['round1']['Aptitude_Test_Business_Acumen'] = random.randint(0,100)
        person['round1']['Value_System_Check'] = random.randint(0,100)
    return persons
def getRound2Scores(persons):
    for person in persons:
        person['round2'] = {}
        person['round2']['Personality'] = random.randint(0,100)
        person['round2']['Values_Empathy'] = random.randint(0,100)
        person['round2']['Business_Family_Tacticality'] = random.randint(0,100)
    return persons
def getRound3Scores(persons):
    for person in persons:
        person['round3'] = {}
        person['round3']['Parents'] = random.randint(0,20)
        person['round3']['Sibling'] = random.randint(0,20)
        person['round3']['Rahul'] = random.randint(0,60)
    return persons
def finalChoice(persons):
    if(len(persons)>0):
        return persons[random.randint(0,len(persons)-1)]
    else:
        return {"name" : "NA"}

def swayamvar(candidates):
    print("Begin......")
    round1Scores = getRound1Scores(candidates)
    # print("After Round1 scores......", round1Scores)
    qualifiedRound1 =[]
    for candidate in round1Scores:
        # print(candidate)
        total = candidate['round1']['Family_Personal_Profile'] + candidate['round1']['Aptitude_Test_Business_Acumen'] + candidate['round1']['Value_System_Check']
        candidate['total1'] = total
        if(candidate['round1']['Family_Personal_Profile']> 15 and candidate['round1']['Aptitude_Test_Business_Acumen']>15 and candidate['round1']['Value_System_Check']> 15 and int(total/3) > 15):
           qualifiedRound1.append(candidate)
    print("After Round1 test....",len(qualifiedRound1))
    def get_my_key1(obj):
        return obj['total1']
    qualifiedRound1.sort(key=get_my_key1, reverse=True)
    # print(qualifiedRound1)
    print("round1 complete..............................")

    r1range = len(qualifiedRound1) if(len(qualifiedRound1) <=7) else 7
    round2Scores = getRound2Scores(qualifiedRound1[:r1range]) 
    print("Round2 begin......")
    qualifiedRound2 =[]
    for candidate in round2Scores:
        # print(candidate)
        total = candidate['round2']['Personality'] + candidate['round2']['Values_Empathy'] + candidate['round2']['Business_Family_Tacticality']
        candidate['total2'] = total
        if(candidate['round2']['Personality']> 15 and candidate['round2']['Values_Empathy']>15 and candidate['round2']['Business_Family_Tacticality']> 15 and int(total/3) > 15):
           qualifiedRound2.append(candidate)
    print("After Round2 test....",len(qualifiedRound2))
    def get_my_key2(obj):
        return obj['total2']
    qualifiedRound2.sort(key=get_my_key2, reverse=True)
    # print(qualifiedRound2)
    print("round2 complete..............................")

    r2range = len(qualifiedRound2) if(len(qualifiedRound2) <=5) else 5
    round3Scores = getRound3Scores(qualifiedRound2[:r2range]) 
    print("Round3 begin......")
    qualifiedRound3 =[]
    for candidate in round3Scores:
        # print(candidate)
        total = candidate['round3']['Parents'] + candidate['round3']['Sibling'] + candidate['round3']['Rahul']
        candidate['total3'] = total
    qualifiedRound3 = round3Scores
    print("After Round3 test....",len(qualifiedRound3))
    def get_my_key3(obj):
        return obj['total3']
    qualifiedRound3.sort(key=get_my_key3, reverse=True)
    # print(qualifiedRound3)
    print("round3 complete..............................")
    r3range = len(qualifiedRound3) if(len(qualifiedRound3) <=3) else 3
    winner = finalChoice(qualifiedRound3[:r3range])
    return winner['name']

pers = generateRandoms(5)
print(swayamvar(pers))
