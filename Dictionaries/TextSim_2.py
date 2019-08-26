def textProcessing(sentence):
    token = sentence.lower().split()
    punct = [',', '.']
    for p in punct:
        for i in range(len(token)):
            if token[i].endswith(p):
                token[i] = token[i].replace(p, '')

    stopwords = ['is', 'am', 'are', 'the', 'that', 'which', 'what', 'it', 'of', 'on', 'in', 'by', 'be', 'a',
                 'those', 'these', 'as', 'an', 'can', 'and', 'from', 'with', 'for', 'to', 'without', 'use']

    wordsList = []
    for word in token:
        if word not in stopwords:
            wordsList.append(word)

    return wordsList

def similarity(str_1,str_2):
    wordsList_1 = textProcessing(str_1)
    wordsList_2 = textProcessing(str_2)

    sim = set(wordsList_1).intersection(wordsList_2)
    union = set(wordsList_1).union(wordsList_2)

    j = len(sim) / len(union)

    final_sim = round(j * 100,2)
    return final_sim


text_1 = "Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly."
text_2 = "Machine learning (ML) is a category of algorithm that allows software applications to become more accurate in predicting outcomes without being explicitly programmed. The basic premise of machine learning is to build algorithms that can receive input data and use statistical analysis to predict an output while updating outputs as new data becomes available. The processes involved in machine learning are similar to that of data mining and predictive modeling. Both require searching through data to look for patterns and adjusting program actions accordingly. Many people are familiar with machine learning from shopping on the internet and being served ads related to their purchase."
sim = similarity(text_1,text_2)
print("Sim is",sim)
