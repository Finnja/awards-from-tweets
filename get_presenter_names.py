file = open("goldenglobes.tab")
import nltk
from nameparser.parser import HumanName
import csv
from nltk.corpus import stopwords
import string

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


pkw = ['present','presenting','presented','presenter','presenters']
akw = ['award','best']

def pkw_search(kwList, tweet):
    for kw in kwList:
        if kw in tweet:
            return True
    
    return False

def akw_search(kwList, tweet):
    for kw in kwList:
        if kw not in tweet:
            return False

    return True

def presenter_names():
    dic ={}
    while 1:
        line = file.readline()
        count = 0
        if pkw_search(pkw,line) and akw_search(akw,line):
            for name in get_human_names(line):
                    if name not in dic:
                        dic[name] =1
                    else:
                        dic[name]+=1         
        if not line:
            break
    return dic

res = presenter_names()
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

if __name__ == '__main__':
    print(presenter_names())
        
