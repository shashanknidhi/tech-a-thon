import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
import os
FMgrace = 1000 
ADgrace = 1000
def create_plot(txtpath):
    FMgrace = 1000 
    ADgrace = 1000
    with open(txtpath,'r') as file:
        scores = file.readlines()
    scores = [float(score) for score in scores]
    print('scores',len(scores))
    benignSample = np.log(scores[FMgrace+ADgrace+1:10000])
    logProbs = norm.logsf(np.log(scores), np.mean(benignSample), np.std(benignSample))
    colors = logProbs[FMgrace+ADgrace+1:]
    print('colors',len(colors))
    plt.figure(figsize=(10,5))
    fig = plt.scatter(range(FMgrace+ADgrace+1,len(scores)),scores[FMgrace+ADgrace+1:],s=0.6,c=colors,cmap='RdYlGn')
    plt.yscale("log")
    plt.title("Anomaly Scores from Kitsune's Execution Phase")
    plt.ylabel("RMSE (log scaled)")
    plt.xlabel("Time elapsed [min]")
    figbar=plt.colorbar()       
    figbar.ax.set_ylabel('Log Probability\n ', rotation=270)
    return fig,colors
def filter_fig(fig,colors):
    scatter_color = fig.to_rgba(colors)
    indexs= []
    for rgba in scatter_color:
        if rgba[0] >= rgba[1]:
            indexs.append(True)
        else:
            indexs.append(False)
    print('indexs',len(indexs))
    return indexs

def filter_packets(tsv_path,indexs):
    df = pd.read_csv(tsv_path,sep = '\t')
    df = df.iloc[FMgrace+ADgrace+1:]
    print('df',len(df))
    print('indexs',len(indexs))
    df = df[indexs]
    df.to_csv(tsv_path+'.csv')
    return df
for path in os.listdir('anomaly_scores'):
    temppath = 'anomaly_scores/'+path
    fig,colors = create_plot(temppath)
    indexs = filter_fig(fig,colors)
    df = filter_packets('captures/'+path.rstrip('.')[0]+'.pcapng.tsv',indexs)


