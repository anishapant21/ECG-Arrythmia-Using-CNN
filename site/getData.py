import requests
import random
import numpy as np
import pandas as pd


from flask import Flask, render_template, request
app=Flask(__name__)



import biosppy
import matplotlib.pyplot as plt
from biosppy.signals import ecg

#keras
import keras
from keras.models import load_model

#load model
model=load_model('/home/anisha/Desktop/ECG/site/my_model.h5')
#with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
 #       model = load_model('/home/anisha/Desktop/ECG/site/my_model.h5')
print('model loaded')


#reading csv data
data=pd.read_csv("/home/anisha/Desktop/ECG/site/Testdata22.csv", delimiter='\t')
data_raw=data.iloc[:,0]
r_peak=biosppy.signals.ecg.christov_segmenter(signal=data_raw, sampling_rate=200)[0] #changed
r_list=r_peak
r_peak_size=len(r_list)
print("the peak size is", r_peak_size)
r_new=r_list[0:1]

#data segmentation
data_fin = np.array(data_raw)
signals = []
count = 1
peaks =  biosppy.signals.ecg.christov_segmenter(signal=data_fin, sampling_rate = 200)[0] #changed
print(peaks)
def segment(signal_MLII, beat_loc):
    window=180
    count=1
    x=beat_loc-window
    y=beat_loc+window
    print(x, y)
    samp=signal_MLII[x:y]
    '''for i in ann_Sample[2,-2]:
            x=ann_Sample[i]-window
            y=ann_sample[i]+window
            samp=temp[x:y]
            
    return samp'''
    return samp
for i in peaks:
    segmentation=segment(data_fin, i)
    if len(segmentation)==360:
        signals.append(segmentation)

print("the length of signal is")
print(len(signals))

raw_sig=np.vstack(signals)
print("raw signal is ready")

result=[]
test_no_scaled=raw_sig.reshape(r_peak_size-2, 360, 1) #changed
predict_this_no=model.predict_classes(test_no_scaled)
result=predict_this_no[0:r_peak_size]
print("The prediction of the given ecg signal is")
print(result)
print(len(result))




#reading csv data
#data=pd.read_csv("/home/anisha/Desktop/ECG-Heart-mate/SampleECG_converted.csv", delimiter='\t')
#data_raw=data.iloc[:,2]
ram=len(data_raw)
print(ram)
print("kay the thing you want prints after this")
peaks_number=len(peaks)

#converting peaks into list
peaks_list=peaks.tolist()
print(peaks_list)
print("length of peaks list is")
print(len(peaks_list))
print("converted")

#making final result
result_final=[]
initialResult=8
for i in range(ram):
    if i in peaks_list:
        p_loc=peaks_list.index(i)-3 #khai k ho k ho thaxaina -1 thiyo hai
        print(p_loc)
        res=int(result[p_loc])
        result_final.append(res)
        initialResult=res
    else:
        result_final.append(initialResult)


print(result_final)
print(type(result_final))
print("im 249", result_final[249])
print("i am 250", result_final[250])


'''for i in range(ram):
    for j in peaks_list:
        if i==j:
            print("i am i")
            print(i)
            print("i am j")
            print(j)
            p_loc=peaks_list.index(i)
            #p_loc=np.where(peaks== j)
            print("yes baby i am working")
            print(p_loc)
            #p_loc=peaks.index(j)

            res=result[p_loc]
            print("the resssssssssssssssult is")
            result_final.append(res)
            print(res)
            continue
            
        else:
            res=0
            result_final.append(res)
            #print("i am extea result for")
            #print(i)
            #print("the result")
            #print(res)  
    #print("i am going in for", i)
    #print("result is", res)
    data={"value":data_raw[i], "name":"Anisha", "age":random.randint(40,50), "sample_number":i, "result":result_final[i]}
    #print("i did")
    reponse=requests.post('http://127.0.0.1:5000/api/postdata', json=data)'''
print("data length i am", ram)
print("result length i am", len(result_final))
for i in range(ram):
    '''if(result_final[i]==4):
        print("here i am")
        continue'''

    data={"value":data_raw[i], "name":"Anisha", "age":random.randint(40,50), "sample_number":i, "result":result_final[i]}
    #data={"value":data_raw[i], "name":"Anisha", "age":random.randint(40,50), "sample_number":i}
    print("i did", i)
    reponse=requests.post('http://127.0.0.1:5000/api/postdata', json=data)




#for i in range(100):
 #   data={"value":random.randint(10,20), "name": "Anisha", "age":random.randint(40, 50)}
  #  reponse=requests.post('http://127.0.0.1:5000/api/postdata', json=data)