from tkinter import *
import requests
from PIL import Image,ImageTk

root = Tk()
root.title="Weather app"
root.iconbitmap('cloud.ico')
root.geometry("600x500")

#key        0a744892b4ced47eb364fbf536f17b0ef5dabd1bdaab488b7f071ddb1c32c597
#API url    https://api.ambeedata.com

def get_weather(city):
    global response
    global lat
    global lng
    API_KEY='c25b45f26f5169bb6d8a352674ddc5f880c7c83ed055c4ea8db4d8d140acf7dd'
    url='https://api.ambeedata.com/forecast/pollen/by-place'
    querystring = {"place":city}
    headers = {
    'x-api-key': API_KEY,
    'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #params={'APPID':weather_key,'q':city,'unit':'imperial'}
    #response=requests.get(url,params)
    #print(response.json())
    #weather=response.json()
    #a=response.json()
    #print(querystring)
    #print(response)
    
    
    data=response.text
    
    if(data[12:19] == 'success'):
        i=27
        while data[i]!=',':
            i+=1
        lat=data[27:i] 
        j=i
        while data[j+7]!=',':
            j+=1
        lng=data[i+7:j]
        
        lat_lng(API_KEY,city)

"""       
def lat_lng():
    API_KEY='69703cce11205fb7da3c926d05f6872f8a4f1fa819c02324688c8019dab133ae'
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
    querystring = {"lat":lat,"lng":lng}
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
"""

def lat_lng(API_KEY,place):
    global data
    
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
    querystring = {"lat":lat,"lng":lng}
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
        }
    data = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.txt)
    
    weather=data.json()
    city=place
    condition=weather['data']['summary']
    temp=weather['data']['temperature']
    result_lbl['text']='City:%s \nCondition:%s \nTemperature%f: '%(city,condition,temp)
   
"""   
def formmat(weather):
    global final_str
    try:
        city=place
        condition=weather['data']['summary']
        temp=weather['data']['temperature']
        final_str='City: '+city+'\nCondition: '+condition+'\nTemperature: '+temp
    except:
        final_str='Problem retriving information'
        
    return final_str

"""

img=Image.open('./Sky.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=Label(root, image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

title=Label(bg_lbl,text="Enter name of place",fg='red',bg='sky blue',font=('times new roman',18))
title.place(x=80,y=18)

frame_one=Frame(root,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=Entry(frame_one,font=('times new roman',25),width=20)
txt_box.grid(row=0,column=0,sticky='w')

btn =Button(frame_one,text='Weather',fg="green",font=('times new roman',16,'bold'),command = lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=5)

frame_two=Frame(root,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result_lbl=Label(frame_two, font=40,bg='white')
result_lbl.place(relwidth=1,relheight=1)


root.mainloop()