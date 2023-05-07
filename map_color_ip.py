import matplotlib.pyplot as plt
import pandas as pd
def filter_fig(fig,colors):
    scatter_color = fig.to_rgba(colors)
    indexs= []
    for rgba in scatter_color:
        if rgba[0] >= rgba[1]:
            indexs.append(True)
        else:
            indexs.append(False)

    return indexs

def filter_packets(tsv_path,indexs):
    df = pd.read_csv(tsv_path,sep = '\t')
