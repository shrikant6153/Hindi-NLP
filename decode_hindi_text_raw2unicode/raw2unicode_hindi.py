import json
import os
import random

fin_raw_hindi = open('delexicalsed_utter_raw.json','r')
data_raw_hindi = json.load(fin_raw_hindi)

print ("Data size: " ,len(data_raw_hindi))

fout_decoded_hindi = open('delexicalsed_utter_hindi.json','w')
json.dump(data_raw_hindi,fout_decoded_hindi,ensure_ascii=False,indent=4)

print ("New File with Hindi Text generated...")
