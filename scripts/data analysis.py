# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:27:11 2022

@author: zhihan
"""
import pandas as pd
import numpy as np
data1=np.array([-0.000319,-1.583039,12.561680,-1.214529,-1.826635,-2.022114,-1.303155,-1.111317,-1.216962,-1.667803,18.065426,-1.114686,-1.483755,-1.438855,-1.783155,-1.605825,-0.707923,-1.344875,-1.789305,-1.608325,0.000000])
data2=np.array([-0.002835,-5.462295,-4.402728,-2.237097,-1.730729,16.618343,-2.278690,-7.054229,-2.007001,20.414758,-0.297866,-1.637287,-2.923498,4.057158,-1.997066,-1.645832,-2.491402,34.898345,-1.417731,-1.670719,0.000000])
df1 = pd.DataFrame(data1,columns=["value"])
df2 = pd.DataFrame(data2,columns=["value"])
pro_df1 = df1[df1['value']<0]
pro_df2 = df2[df2['value']<0]
mean1 = pro_df1['value'].mean()
mean2 = pro_df2['value'].mean()
sigma1 = pro_df1['value'].std()
sigma2 = pro_df2['value'].std()
final_mean1=pro_df1[(pro_df1['value']<(mean1+3*sigma1)) & (pro_df1['value']>(mean1-3*sigma1))].mean()
final_mean2=pro_df2[(pro_df2['value']<(mean2+3*sigma2)) & (pro_df2['value']>(mean2-3*sigma2))].mean()
print("一档数据的离群值有{}个".format(df1.count().value-pro_df1.count().value))
print("二档数据的离群值有{}个".format(df2.count().value-pro_df2.count().value))
print("二者均值分别为{},{}".format(final_mean1.value,final_mean2.value))
print("相差{}倍".format(final_mean2.value/final_mean1.value))
