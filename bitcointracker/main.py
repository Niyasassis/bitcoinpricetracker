import requests
import tkinter as tk
from datetime import datetime

# function for fetch api

def tracker():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    responce = requests.get(url).json()
    # print(responce)
    price = responce["USD"] 
    time = datetime.now().strftime('%I:%M:%S:%p')

    labelPrice.config(text= f'${price}' )
    labelTime.config(text=f"Updated at : {time}")
    
    # updating in each second


    canvas.after(1000,tracker)





canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Price Tracker")
f1 = ('poppins',24,'bold')
f2 = ('poppins',12,'bold')
f3= ('poppins',18,'normal')

label = tk.Label(canvas,text="Bitcoin Rate",font=f1)
label.pack(pady = 20)

labelPrice= tk.Label(canvas,font= f2)
labelPrice.pack(pady = 20)

labelTime= tk.Label(canvas,font= f1)
labelTime.pack(pady = 20)

tracker()
canvas.mainloop()