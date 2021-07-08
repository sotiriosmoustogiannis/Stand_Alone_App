import tkinter as tk
from tkinter import Message, ttk
from tkinter import font
from tkinter import filedialog
import tkinter
import numpy as np
import pandas as pd
import re
import time
from datasketch import MinHash, MinHashLSHForest

# variables that define the size of the window form
HEIGHT = 900
WIDTH = 800

# variables for get_forest and predict functions
permutations = 256
# number of result
num_recommendations = 10
# search field 
# TODO dynamic search at django project)
operations = 'googlesearchservice'

# a function that the get_forest and the predict functions use to make all words in lower case 
def preprocess(text):
    tokens = text.lower()
    tokens = tokens.split()
    return tokens

# open the file you want
def openfile():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(title="Open file",filetypes=filetypes)
    print(filename)

    global db

    #fortwsh dedomenwn
    db = pd.read_csv(filename)

    return db

# TODO save the file(forest) with the name of the store name
def get_forest(db,perms,*args):
    
    print(args[0],args[1])

    #dhmiourgia db[text] gia  thn diaxerhsh
    # depending on the fields that the user will select to make the process  
    db['text']=''
    usedfieds = []
    for i in range(11):
        # the combobox fields must not be null and must not save the same values into the db[text] field
        if args[i]!='' and args[i] not in usedfieds:   
            usedfieds.append(args[i])
            print(usedfieds)
            db['text'] += db[args[i]].astype(str) + ' '
    start_time = time.time()

    minhash = []
    print(db['text'])

    for text in db['text']:
        tokens = preprocess(text)
#        print(tokens)
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

def predict(text, database, perms, num_results, forest):
    start_time = time.time()

    print(start_time)

    tokens = preprocess(text)
    m = MinHash(num_perm=perms)
    for s in tokens:
        m.update(s.encode('utf8'))

    idx_array = np.array(forest.query(m, num_results))
    if len(idx_array) == 0:
        return None # if your query is empty, return none

    result = database.iloc[idx_array]['Service Name'] 

    print('It took %s seconds to build forest.' %(time.time()-start_time))

    print(result)

    return result

root = tk.Tk()

# define the frame (size, color)
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)


# the field choices that user can select to process
# TODO Ask the professor if is right to have certain choises or the user has to select
comboExample = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample1 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample2 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample3 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample4 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample5 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample6 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample7 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample8 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample9 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])

comboExample10 = ttk.Combobox(frame, 
                            values=[
                                    "Response Time", 
                                    "Availability",
                                    "Throughput",
                                    "Successability",
                                    "Reliability", 
                                    "Compliance",
                                    "Best Practices",
                                    "Latency",
                                    "Documentation",
                                    "Service Name",
                                    "WSDL Address"])


# text of labels, comboexample taken values, button functions
labeln = tk.Label(frame, text="Store Name: ")
labeln.grid(row=0, column=0)

entry = tk.Entry(frame, bg='gray')
entry.grid(row=0, column=1)

label = tk.Label(frame, text="Open your CSV file")
label.grid(row=1,column=0)

button3 = tk.Button(frame, text = "open file", bg ='gray', fg='red',command=lambda: openfile())
button3.grid(row=2, column=0)

label = tk.Label(frame, text="Property 1: ")
label.grid(row=3, column=0)

comboExample.grid(row=3, column=1)

label1 = tk.Label(frame, text="Property 2: ")
label1.grid(row=4, column=0)

comboExample1.grid(row=4, column=1)

label2 = tk.Label(frame, text="Property 3: ")
label2.grid(row=5, column=0)

comboExample2.grid(row=5, column=1)

label3 = tk.Label(frame, text="Property 4: ")
label3.grid(row=6, column=0)

comboExample3.grid(row=6, column=1)

label4 = tk.Label(frame, text="Property 5: ")
label4.grid(row=7, column=0)

comboExample4.grid(row=7, column=1)

label5 = tk.Label(frame, text="Property 6: ")
label5.grid(row=8, column=0)

comboExample5.grid(row=8, column=1)

label6 = tk.Label(frame, text="Property 7: ")
label6.grid(row=9, column=0)

comboExample6.grid(row=9, column=1)

label7 = tk.Label(frame, text="Property 8: ")
label7.grid(row=10, column=0)

comboExample7.grid(row=10, column=1)

label8 = tk.Label(frame, text="Property 9: ")
label8.grid(row=11, column=0)

comboExample8.grid(row=11, column=1)

label9 = tk.Label(frame, text="Property 10: ")
label9.grid(row=12, column=0)

comboExample9.grid(row=12, column=1)

label10 = tk.Label(frame, text="Property 11: ")
label10.grid(row=13, column=0)

comboExample10.grid(row=13, column=1)


button1 = tk.Button(frame, text = "forest", bg ='gray', fg='red',command=lambda: get_forest(db, permutations,comboExample.get(),comboExample1.get(),comboExample2.get(),comboExample3.get(),comboExample4.get(),comboExample5.get(),comboExample6.get(),comboExample7.get(),comboExample8.get(),comboExample9.get(),comboExample10.get()))
button1.grid(row=14, column=0)

button2 = tk.Button(frame, text = "result", bg ='gray', fg='red',command=lambda: predict(operations, db, permutations, num_recommendations, forest))
button2.grid(row=15, column=0)



root.mainloop()
