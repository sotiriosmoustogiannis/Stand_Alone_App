import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import pandas as pd
import re
import time
from datasketch import MinHash, MinHashLSHForest




HEIGHT = 700
WIDTH = 800

root = tk.Tk()

def preprocess(text):
    text = re.sub(r'[^\\w\\s]','',text)
    tokens = text.lower()
    tokens = tokens.split()
    return tokens


def get_forest(perms):
        filename = filedialog.askopenfilename(title="Open File")
        print(filename)    
        db = pd.read_csv(filename)

        db['text'] = db['title'].astype(str)  + ' ' +  db['abstract'].astype(str)

        start_time = time.time()

        minhash = []

        for text in db['text']:
                tokens = preprocess(text)
                m = MinHash(num_perm=perms)
                for s in tokens:
                        m.update(s.encode('utf8'))
                minhash.append(m)
        
        global forest
        forest = MinHashLSHForest(num_perm=perms)

        for i,m in enumerate(minhash):
                forest.add(i,m)
        
        forest.index()

        print('It took %s seconds to build forest.' %(time.time()-start_time))

        return forest
'''
def predict(text, database, perms, num_results, forest):
    start_time = time.time()
    
    print('fdg')

    tokens = preprocess(text)
    m = MinHash(num_perm=perms)
    for s in tokens:
        m.update(s.encode('utf8'))
        
    idx_array = np.array(forest.query(m, num_results))
    if len(idx_array) == 0:
        return None # if your query is empty, return none
    
    result = database.iloc[idx_array]['ServiceName']
    
    print('It took %s seconds to query forest.' %(time.time()-start_time))
    
    print(result)

    return result
'''

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

comboExample = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample1 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample2 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample3 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample4 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample5 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample6 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample7 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample8 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])


comboExample9 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

comboExample10 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "BestPractices",
                                    "Latency",
                                    "Documentation",
                                    "ServiceName",
                                    "WSDLAddress"])

label = tk.Label(frame, text="Store Name: ")
label.grid(row=0, column=0)

entry = tk.Entry(frame, bg='gray')
entry.grid(row=0, column=1)

label = tk.Label(frame, text="Property 1: ")
label.grid(row=1, column=0)

comboExample.grid(row=1, column=1)

label = tk.Label(frame, text="Property 2: ")
label.grid(row=2, column=0)

comboExample1.grid(row=2, column=1)

label = tk.Label(frame, text="Property 3: ")
label.grid(row=3, column=0)

comboExample2.grid(row=3, column=1)

label = tk.Label(frame, text="Property 4: ")
label.grid(row=4, column=0)

comboExample3.grid(row=4, column=1)

label = tk.Label(frame, text="Property 5: ")
label.grid(row=5, column=0)

comboExample4.grid(row=5, column=1)

label = tk.Label(frame, text="Property 6: ")
label.grid(row=6, column=0)

comboExample5.grid(row=6, column=1)

label = tk.Label(frame, text="Property 7: ")
label.grid(row=7, column=0)

comboExample6.grid(row=7, column=1)

label = tk.Label(frame, text="Property 8: ")
label.grid(row=8, column=0)

comboExample7.grid(row=8, column=1)

label = tk.Label(frame, text="Property 9: ")
label.grid(row=9, column=0)

comboExample8.grid(row=9, column=1)

label = tk.Label(frame, text="Property 10: ")
label.grid(row=10, column=0)

comboExample9.grid(row=10, column=1)

label = tk.Label(frame, text="Property 11: ")
label.grid(row=11, column=0)

comboExample10.grid(row=11, column=1)


#Number of Permutations
permutations = 256

#Number of Recommendations to return
num_recommendations = 3


#frame.filename = filedialog.askopenfilename(title='Select a file', filetypes=(("csv files", "*.csv"),("all files", "*.*")))
#print(frame.filename)



operations = 'flight'





button1 = tk.Button(frame, text = "forest", bg ='gray', fg='red', command=get_forest(permutations))
button1.grid(row=12, column=0)

button2 = tk.Button(frame, text = "Open file", bg ='gray', fg='red')
button2.grid(row=13, column=0)

#button3 = tk.Button(frame, text = "Result", bg ='gray', fg='red', command=predict(operations, db, permutations, num_recommendations, forest))
#button3.grid(row=14, column=0)


root.mainloop()