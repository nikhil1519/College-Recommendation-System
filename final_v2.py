from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import os

df1 = pd.read_csv('Final_data.csv', sep=',', encoding='cp1252')

nb=[4,9,13,14,15,25,32,35,41,42,44,46,48,49,51,52,58,61,68,71,73,80,81,83,85,87,88,91,92,94,11,17,47,50,59,74,90,21,33,62,65,77,78,79,86,23,1,29,37,54,56,60,63]

def countOccurrence(a):
    k = {}
    for j in a:
        if j in k:
            k[j] +=1
        else:
            k[j] =1
    return k

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("index_new.html")

@app.route('/registration')
def upload_file():
    return render_template('index_new.html')


@app.route('/check', methods = ['GET', 'POST'])
def upload_1():
    if request.method == 'POST':

        communitycode=int(request.form['Community'])
        rank=int(request.form['Rank'])
        aggmark=float(request.form['Cut_off'])
        branchcode=int(request.form['Branch'])
        #Type=int(request.form['Type'])
        df1 = pd.read_csv('Final_data.csv', sep=',', encoding='cp1252')


        # if (branchcode==100):
        #     df2=df1
        #     X=df1.iloc[:,1:5]
        #     y=df1.iloc[:,6:]
        #     nbrs = NearestNeighbors(n_neighbors=30, algorithm='ball_tree').fit(X)
        #     distances, indices = nbrs.kneighbors([[communitycode,rank,aggmark,branchcode]])
        #     a=[]
        #     ind=list(indices[0])
        #     for i in range(len(ind)):
        #         a.append(y.iloc[indices[0][i],0])
        #     final=countOccurrence(a)
        #     f1 = sorted(final.items(), key=lambda x:x[1],reverse=True)
        #     f2=f1[:10]
        #     f3=[]
        #     for i in f2:
        #         f3.append(i[0])
        #     f3
        #     return render_template("reg_1.html",result=f3)
        
        if(branchcode in nb):
            df2=df1[(df1['BC'] == branchcode)]
            X=df2.iloc[:,1:5]
            #print(X)
            y=df2.iloc[:,6:]
            #print(y)
            lc=list(y['Name of the College'])
            #print(lc)
            output = []
            for x in lc:
                if x not in output:
                    output.append(x)
            c=output[:10]
            return render_template("reg_1.html",result=c)

        else:
            df1=df1[(df1['BC'] == branchcode)]
            X=df1.iloc[:,1:5]
            y=df1.iloc[:,6:]
            nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X)
            distances, indices = nbrs.kneighbors([[communitycode,rank,aggmark,branchcode]])
            a=[]
            ind=list(indices[0])
            for i in range(len(ind)):
                a.append(y.iloc[indices[0][i],0])
            final=countOccurrence(a)
            f1 = sorted(final.items(), key=lambda x:x[1],reverse=True)
            f2=f1[:10]
            f3=[]
            for i in f2:
                f3.append(i[0])
            f3
            return render_template("reg_1.html",result=f3)
        

if __name__ == '__main__':
    # app.run(debug=True)
    # port = int(os.environ.get('PORT',5000))
    app.run(debug=True, port=5000)