dataset = {
    "action" : ["sultan",'dangal','kgf','uri','baahubali','hulk',
        'ironman','spiderman','superman',"avengers","thor"],
    "comedy" : ["zero","dhamaal","hera pheri","golmaal"],
    "horror" : ['the nun',"it","Exorcism","conjuring"],
    "scifi" : ["ironman","spiderman","hulk","gravity","interstellar"],
    "biopic" : ["sultan","dangal","ms dhoni"]
    }

user = {"sultan",'ironman','the nun','it','zero','dhamaal','golmaal'}

#score = {"action":0,"comedy":0,"horror":0,"scifi":0,"biopic":0}
score = {}
for key in dataset:
    score[key] = 0

#print(score)
for key in dataset:
    data = set(dataset[key])
    numer = data.intersection(user)
    print("{} : {}".format(key,numer))
    denom = data.union(user)

    s = len(numer) / len(denom)
    score[key] = s


category = max(score.items(), key=lambda x : x[1])
#print(category[0])

movies = dataset[category[0]]
rec = set(movies) - user
print("Recommended",rec)
