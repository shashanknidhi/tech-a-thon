from Kitsune import Kitsune
import numpy as np
import time
import os
from scipy.stats import norm
if os.path.exists('anomaly_scores'):
    if len(os.listdir('anomaly_scores')) > 0:
        #remove all files in captures folder
        files = ['anomaly_scores/'+f for f in os.listdir('anomaly_scores')]
        for f in files:
            os.remove(f)
else:
    os.mkdir('anomaly_scores')
for path in os.listdir('captures'):
    if path[-4:] == '.tsv':
        os.remove('captures/'+path)
if os.path.exists('output'):
    if len(os.listdir('output')) > 0:
        #remove all files in captures folder
        files = ['output/'+f for f in os.listdir('output')]
        for f in files:
            os.remove(f)
else:
    os.mkdir('output')
for temp_path in os.listdir('captures'):
    path = 'captures/'+temp_path
    packet_limit = np.Inf #the number of packets to process

    # KitNET params:
    maxAE = 10 #maximum size for any autoencoder in the ensemble layer
    FMgrace = 1000 #the number of instances taken to learn the feature mapping (the ensemble's architecture)
    ADgrace = 1000 #the number of instances used to train the anomaly detector (ensemble itself)

    # Build Kitsune
    K = Kitsune(path,packet_limit,maxAE,FMgrace,ADgrace)

    print("Running Kitsune:")
    RMSEs = []
    i = 0
    start = time.time()
    # Here we process (train/execute) each individual packet.
    # In this way, each observation is discarded after performing process() method.
    while True:
        i+=1
        if i % 1000 == 0:
            print(i)
        rmse = K.proc_next_packet()
        if rmse == -1:
            break
        RMSEs.append(rmse)
    stop = time.time()
    print("Complete. Time elapsed: "+ str(stop - start))

    score_path = 'anomaly_scores/'+temp_path.rsplit('.',1)[0]+'.txt'
    with open(score_path, 'w') as f:
        for score in RMSEs:
            f.write(str(score) + "\n")

    # Here we demonstrate how one can fit the RMSE scores to a log-normal distribution (useful for finding/setting a cutoff threshold \phi)
    benignSample = np.log(RMSEs[FMgrace+ADgrace+1:10000])
    logProbs = norm.logsf(np.log(RMSEs), np.mean(benignSample), np.std(benignSample))

    # plot the RMSE anomaly scores
    # print("Plotting results")
    from matplotlib import pyplot as plt
    from matplotlib import cm
    plt.figure(figsize=(10,5))
    fig = plt.scatter(range(FMgrace+ADgrace+1,len(RMSEs)),RMSEs[FMgrace+ADgrace+1:],s=0.6,c=logProbs[FMgrace+ADgrace+1:],cmap='RdYlGn')
    plt.yscale("log")
    plt.title("Anomaly Scores from Kitsune's Execution Phase")
    plt.ylabel("RMSE (log scaled)")
    plt.xlabel("Time elapsed [min]")
    # figbar=plt.colorbar()       
    # figbar.ax.set_ylabel('Log Probability\n ', rotation=270)
    plt.savefig('output/'+str(i)+'.png')
