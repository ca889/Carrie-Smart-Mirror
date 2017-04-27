
from tkinter import *
import locale
import threading
import time
import requests
import json
import contextmanager
import traceback
import feedparser


from PIL import Image, ImageTk
from contextlib importcontextmanager

location = treading.Lock()

country = 'us'
time = 12
date_format = "%b %d, %Y" #format for the date
country_for_times = 'us'


#text sizes
really_big_text = 94
big_text = 48
text = 28
tiny_text = 18



@contextmanager
def set_up_location(name):
    with location:
        setLocation = locale.setLocation(locale.LC_ALL)
        try:
            yield locale.setLocation(locale.LC_ALL, name)
        finally:
            locale.setLocation(locale.LC_ALL,setLocation)




class Time(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.time = ' '
        self.timeLbl = Label(self, font=('Helvetica', large_text_size), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)

        self.day = ''
        self.dayLbl = Label(self, text=self.day, font=('Helvetica', tiny_text), fg="white", bg="black")

        self.date = ''
        self.dateLbl = Label(self, text=self.date, font=('Helvetica', tiny_text), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.change_time()


    def change_time(self):
        with set_up_location(country):
            if time == 12:
                timeB = time.strftime('%I:%M %p')
            else:
                timeB = time.strftime('%H:%M')

            dayB = time.strftime('%A')
            dateB = time.strftime(date_format)

            if timeB != self.time:
                self.time = timeB
                self.timeLbl.config(text=timeB)
            if dayB != self.day:
                self.day = dayB
                self.dayLbl.config(text=dayB)
            if dateB != self.date:
                self.date = dateB
                self.dateLbl.config(text=dateB)

            self.timeLbl.after(200, self.change_time)


class Times_Headlines(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'Times Headlines' 
        self.timesLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.timesLbl.pack(side=TOP, anchor=W)
        self.timesHeadlines = Frame(self, bg="black")
        self.timesHeadlines.pack(side=TOP)
        self.contain_headlines()

    def contain_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if country_for_times == None:
                headlines_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % country_for_times

            f = feedparser.parse(headlines_url)

            for post in f.entries[0:5]:
                headline = NewsHeadline(self.headlinesContainer, post.title)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            print "Error: %s. No News." % e

        self.after(600000, self.contain_headlines)


class HeadlinesTimes(Frame):
    def __init__(self, parent, event=""):
        Frame.__init__(self, parent, bg='black')

        self.pLbl = Label(self, bg='black', pic=photo)
        self.pLbl.pic = ph
        self.picLbl.pack(side=LEFT, anchor=N)

        pic = Image.open("assets/Newspaper.png")
        pic = pic.resize((25, 25), Image.ANTIALIAS)
        pic = pic.convert('RGB')
        ph = ImageTk.PhotoImage(pic)

        self.e= event
        self.eLbl = Label(self, text=self.e, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.eLbl.pack(side=LEFT, anchor=N)


