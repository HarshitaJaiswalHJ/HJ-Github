import tkinter as ttk
import pandas as pd

app=ttk.Tk()
app.title('Recommendation System')
app.geometry('400x400')

cols=['user_id', 'movie_id', 'rating', 'timestamp']
df=pd.read_csv('u.data', sep='\t', names=cols).drop('timestamp',axis=1)
item_cols=['movie_id','title'] + [str(i) for i in range (22)]
df1=pd.read_csv('u.item', sep='|',  encoding="ISO-8859-1",names= item_cols)
movie=pd.merge(df,df1,on='movie_id')

result=ttk.Variable(app)
box=ttk.Listbox(app, height=10)
for row, val in movie.iterrows():
    print(val['title'])
    box.insert(row+1, val['title'])
box.place(x=10,y=10)

def get_movie():
    pass
ttk.Button(app, text='Find Recommendations', font=('Arial', 22), Command=get_movie).place(x=200, y=50)
ttk.Label(app, textvariable=result, font=('Arial',22), Command=get_movie).place(x=200, y=50)

