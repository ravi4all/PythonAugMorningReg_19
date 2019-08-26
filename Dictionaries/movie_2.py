dataset = {
    "action" : ["sultan",'dangal','kgf','uri','baahubali','hulk',
        'ironman','spiderman','superman',"avengers","thor"],
    "comedy" : ["zero","dhamaal","hera pheri","golmaal"],
    "horror" : ['the nun',"it","Exorcism","conjuring"],
    "scifi" : ["ironman","spiderman","hulk","gravity","interstellar"],
    "biopic" : ["sultan","dangal","ms dhoni"]
    }

user_1 = {"sultan",'ironman','the nun','it','zero','dhamaal','golmaal'}
user_2 = {"golmaal","dhamaal","dangal","sultan","baahubali","hulk","gravity"}
#score = {"action":0,"comedy":0,"horror":0,"scifi":0,"biopic":0}
score = {}
for key in dataset:
    score[key] = 0

simMovies = user_1.intersection(user_2)

#print(score)
for key in dataset:
    data = set(dataset[key])
    numer = data.intersection(simMovies)
    print("{} : {}".format(key,numer))
    denom = data.union(simMovies)

    s = len(numer) / len(denom)
    score[key] = s

print(score)

category = max(score.items(), key=lambda x : x[1])
#print(category[0])
movies = dataset[category[0]]

cat_1 = user_1.intersection(movies)
# print(cat_1)

cat_2 = user_2.intersection(movies)
# print(cat_2)

rec = cat_1 - cat_2
print(rec)