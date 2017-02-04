
file = open("goldenglobes.tab")
import nltk
from nameparser.parser import HumanName
n = 13
'''
1.Best Motion Picture - Drama*
"Moonlight" *WINNER

wrong 2.Best Motion Picture - Musical or Comedy
"La La Land" *WINNER

3.Best Performance by an Actress in a Motion Picture - Drama*
Isabelle Huppert - "Elle" *WINNER

4.Best Performance by an Actor in a Motion Picture - Drama*
Casey Affleck - "Manchester by the Sea" *WINNER

5.Best Actor in a Motion Picture - Musical or Comedy*
Ryan Gosling - "La La Land" *WINNER

6.Best Actress in a Motion Picture - Musical or Comedy*
Emma Stone - "La La Land" *WINNER

7.Best Supporting Actor in a Motion Picture*
Aaron Taylor-Johnson - "Nocturnal Animals" *WINNER

8.Best Supporting Actress in a Motion Picture*
Viola Davis - "Fences" *WINNER

9.Best Animated Feature Film*
"Zootopia" *WINNER

10.Best Director*
Damien Chazelle - "La La Land" *WINNER

11.Best Screenplay*
Damien Chazelle - "La La Land" *WINNER

12.Best Original Score
"La La Land" *WINNER

wrong 13.Best Original Song
"City of Stars" - "La La Land" *WINNER

14.Best Foreign Language Film
"Elle" - (France) *WINNER
'''

def nomin(n):
    if n==1:
        return ["Moonlight", "Hell or High Water", "Lion","Manchester by the Sea", "Hacksaw Ridge"]
    if n==2:
        return ["La La Land","20th Century Women", "Deadpool","Florence Foster Jenkins","Sing Street"]
    if n==9:
        return ["Zootopia", "Moana", "My Life as a Zucchini", "Sing", "Kubo and the Two Strings"]
    if n==12:
        return ["La La Land", "Moonlight", "Arrival", "Lion", "Hidden Figures"]
    if n==13:
        return ["La La Land","Trolls","Sing","Gold","Moana"]
    if n==14:
        return ["Elle", "Divines", "Neruda", "The Salesman", "Toni Erdmann"]

def splitaward(n):
    awardlist = []
    if n==1:
        awardlist = ["best","drama"]
    if n==2:
        awardlist = ["best", "musical","comedy"]
    if n==3:
        awardlist = ["best", "drama", "actress"]
    if n==4:
        awardlist = ["best", "drama", "actor"]
    if n==5:
        awardlist = ["best", "musical","comedy", "actor"]
    if n==6:
        awardlist = ["best", "musical","comedy", "actress"]
    if n==7:
        awardlist = ["best", "supporting","actor"]
    if n==8:
        awardlist = ["best","supporting","actress"]
    if n==9:
        awardlist = ["best","animated"]
    if n==10:
        awardlist = ["best","director"]
    if n==11:
        awardlist = ["best","screenplay"]
    if n==12:
        awardlist = ["best","original","score"]
    if n==13:
        awardlist = ["song"]
    if n==14:
        awardlist = ["best","foreign"]
    return awardlist


def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list) 

def parseaward_name(n):
    dic ={}
    awardlist = splitaward(n)
    while 1:
        line = file.readline()
        count = 0
        total = len(awardlist)
        for w in awardlist:
            if w in line.lower() and "TV" not in line:
                count += 1
        if count/total > 0.7:
            for name in get_human_names(line):
                    if name not in dic:
                        dic[name] =1
                    else:
                        dic[name]+=1            
        if not line:
            break
    return dic

def parseaward_movie(n):
    dic ={}
    awardlist = splitaward(n)
    print awardlist
    while 1:
        line = file.readline()
        count = 0
        total = len(awardlist)
        for movie in nomin(n):
            if movie.lower() in line:
                for word in awardlist:
                    if word in line.lower():
                        count+=1
                if (count*1.0)/total > 0.6:
                    if movie not in dic:
                        dic[movie] =1
                    else:
                        dic[movie] += 1           
        if not line:
            break
    return dic
def get_res(n):
    if n in [1,2,9,12,13,14]:
        return parseaward_movie(n)
    else:
        return parseaward_name(n)


res = get_res(n)
res = sorted(res, key = lambda name: res[name], reverse = True)
def filter(dict):
    forbiddenlist = ["Best","Actor","Actress","Drama","Golden","Globe","Motion","Best"]
    i = 0
    while i < len(dict):
        j=0
        while j <len(forbiddenlist):    
            if forbiddenlist[j] in dict[i]:
                break
            j+=1
        if j >= len(forbiddenlist):
            return i
        i+=1
index = filter(res)
print res