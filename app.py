import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
def create_plot(txtpath):
    FMgrace = 1000 
    ADgrace = 1000
    with open(txtpath,'r') as file:
        scores = file.readlines()
    scores = [float(score) for score in scores]
    
    benignSample = np.log(scores[FMgrace+ADgrace+1:10000])
    logProbs = norm.logsf(np.log(scores), np.mean(benignSample), np.std(benignSample))

    plt.figure(figsize=(10,5))
    fig = plt.scatter(range(FMgrace+ADgrace+1,len(scores)),scores[FMgrace+ADgrace+1:],s=0.6,c=logProbs[FMgrace+ADgrace+1:],cmap='RdYlGn')
    plt.yscale("log")
    plt.title("Anomaly Scores from Kitsune's Execution Phase")
    plt.ylabel("RMSE (log scaled)")
    plt.xlabel("Time elapsed [min]")
    figbar=plt.colorbar()       
    figbar.ax.set_ylabel('Log Probability\n ', rotation=270)
    return fig
for path in os.listdir('anomaly_scores'):
    st.pyplot(create_plot('anomaly_scores'+path))
    
             
