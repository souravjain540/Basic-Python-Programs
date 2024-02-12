from tkinter import *
from tkinter import filedialog
import pandas as pd
import os
from pathlib import Path
import numpy as np

download_folder = str(os.path.join(Path.home(), "Downloads"))


def openFile():
    filepath = filedialog.askopenfilename(initialdir="",
                                          title="Open .csv file",
                                          filetypes=((".csv file","*.csv"),
                                          ("All files","*.*")))
    file = open(filepath, 'r')
    file.close()
    window.destroy()

    window2 = Tk()

    def dropNa():
        df = pd.read_csv(filepath)
        df = df.dropna()
        window2.destroy()
        # print(df.head())

        df.to_csv(('csv_drop_null_values.csv'), index=False)

    def fillMean():
        df = pd.read_csv(filepath)
        df = df.fillna(df.mean())
        window2.destroy()
        # print(df.head())

        df.to_csv(('csv_fill_mean_values.csv'), index=False)

    def fillMedian():
        df = pd.read_csv(filepath)
        df = df.fillna(df.median())
        window2.destroy()
        # print(df.head())

        df.to_csv(('csv_fill_m_values.csv'), index=False)

    def fillMin():
        df = pd.read_csv(filepath)
        df = df.select_dtypes(include=np.number).fillna(df.min())
        window2.destroy()
        # print(df.head())
        
        df.to_csv(('csv_fill_min_values.csv'), index=False)

    def fillMax():
        df = pd.read_csv(filepath)

        df = df.fillna(df.max())
        window2.destroy()
        # print(df.head())
        
        df.to_csv(('csv_fill_max_values.csv'), index=False)

    dropna = Button(text="Drop NA Values", command=dropNa)
    fill_mean = Button(text="Fill with Mean Values", command=fillMean)
    fill_median = Button(text="Fill with Median Values", command=fillMedian)
    fill_min = Button(text="Fill with Min Values", command=fillMin)
    fill_max = Button(text="Fill with Max Values", command=fillMax)

    dropna.pack()
    fill_mean.pack()
    fill_median.pack()
    fill_min.pack()
    fill_max.pack()
    window2.mainloop()


window = Tk()
button = Button(text="Open", command=openFile)

button.pack()
window.mainloop()
