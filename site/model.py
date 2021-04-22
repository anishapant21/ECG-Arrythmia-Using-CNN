import numpy as np
import pandas as pd
import biosppy
import matplotlib.pyplot as plt
from biosppy.signals import ecg

#keras
from keras.models import load_model

#load model
model=load_model('/home/anisha/Desktop/ECG/site/my_model.h5')
print('model loaded')


#reading csv data
data=pd.read_csv("/home/anisha/Desktop/ECG-Heart-mate/SampleECG_converted.csv", delimiter='\t')
data_raw=data.iloc[:,2]
r_peak=biosppy.signals.ecg.christov_segmenter(signal=data_raw, sampling_rate=1000)[0]
print(r_peak[200])
r_list=r_peak
r_new=r_list[0:1]

    

#data segmentation
data_fin = np.array(data_raw)
signals = []
count = 1
peaks =  biosppy.signals.ecg.christov_segmenter(signal=data_fin, sampling_rate = 1000)[0]
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

print(len(signals))

raw_sig=np.vstack(signals)
print("raw signal is ready")

result=[]
test_no_scaled=raw_sig.reshape(463, 360, 1)
predict_this_no=model.predict_classes(test_no_scaled)
result=predict_this_no[0:462]
print(result)



