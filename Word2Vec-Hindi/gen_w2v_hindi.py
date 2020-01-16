# Help taken From : https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92
from __future__ import unicode_literals
import numpy as np
from gensim.models import Word2Vec
import io
import json

# list of 500000 monolingu data
fin_hi = open('monolingual.hi','r') 
fin_hin_list = []

# select first 5000 sentence.
z=0
for line in fin_hi :
	z=z+1
	if z==5000:
		break
	fin_hin_list.append(line)

size=input("Input size of w2v vector size:\n") # Example: 80, 100, 120, 150

file1 = 'delexicalsed_utter_hindi.json'  #file for list of delexiclise sentence
file2 = 'hindi_wordtovec-'+size+'.txt'   # file where w2v will be saved.
fin_json=open(file1,'r')
fout_w2v=open(file2,'a')

# load input json file of delexicalised hindi utterances
y = json.load(fin_json)

# merge the 5000 monolingual data with the delexicalsed utterances
total_sentence = y + fin_hin_list

sentences = []
for s in total_sentence:
	sentences.append(s.split())

'''
Default:
	size = 100 # The number of dimensions of the embeddings
	min_count = 5 # minimum count of words to consider when training the model; words with occurrence less than this count will be ignored.
	sg = 0 # CBOW(0) or skip gram(1).
'''

model = Word2Vec(sentences, size=150,min_count=1,sg=1)
print("Total sentences processed: ",len(total_sentence))

# summarize the loaded model
print(model)

# Print w2v vector for 'SLOT_NAME' as an Example.
print(model['SLOT_NAME'])

# Write w2v in a .txt file
words = list(model.wv.vocab)
for w in words:	
	vec = w
	for num in model[w]:   #model[w] is list of number represent vector
		vec = vec + ' ' +str(num)
	vec = vec + '\n' 
	fout_w2v.write(vec)


'''
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)'''