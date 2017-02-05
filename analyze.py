
file = open("goldenglobes.tab")
import nltk
from nameparser.parser import HumanName
dic={}
award="Best performance by Actress in a TV series - Drama"
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

while 1:
    line = file.readline()
    if award in line:
        for name in get_human_names(line):
            if name not in dic:
                dic[name] =1
            else:
                dic[name]+=1
            
    if not line:
        break
    pass

file.close()
dic = sorted(dic, key = lambda name: dic[name], reverse = True)
print dic[0]

