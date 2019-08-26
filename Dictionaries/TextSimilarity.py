# 1. Tokenization
# 2. Remove Stopwords
# 3. Stemming
# 4. Vectorization

text_1 = "Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly."
text_2 = "Machine learning (ML) is a category of algorithm that allows software applications to become more accurate in predicting outcomes without being explicitly programmed. The basic premise of machine learning is to build algorithms that can receive input data and use statistical analysis to predict an output while updating outputs as new data becomes available. The processes involved in machine learning are similar to that of data mining and predictive modeling. Both require searching through data to look for patterns and adjusting program actions accordingly. Many people are familiar with machine learning from shopping on the internet and being served ads related to their purchase."

token_1 = text_1.lower().split()
token_2 = text_2.lower().split()

punct = [',','.']
for p in punct:
    for i in range(len(token_1)):
        if token_1[i].endswith(p):
            token_1[i] = token_1[i].replace(p,'')

for p in punct:
    for i in range(len(token_2)):
        if token_2[i].endswith(p):
            token_2[i] = token_2[i].replace(p,'')

# sim = set(token_1).intersection(token_2)
# print(sim)

stopwords = ['is','am','are','the','that','which','what','it','of','on','in','by','be','a',
             'those','these','as','an','can','and','from','with','for','to','without','use']

wordsList_1 = []
for word in token_1:
    if word not in stopwords:
        wordsList_1.append(word)

wordsList_2 = []
for word in token_2:
    if word not in stopwords:
        wordsList_2.append(word)

sim = set(wordsList_1).intersection(wordsList_2)
union = set(wordsList_1).union(wordsList_2)

j = len(sim) / len(union)
print("Sim is",j*100)