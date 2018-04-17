from Tkinter import Tk, StringVar
import tkMessageBox
import ttk
from Tkinter import *
from HTMLParser import HTMLParser
import urllib

## THIS PYTHON CODE IS WRITTEN IN PYTHON 2.7.12, PLEASE CONVERT IT TO PYTHON 3 USING ONLINE CONVERTER FIRST IF YOU'RE
## USING PYTHON 3.x BECAUSE A LOT OF LIBRARY HAS BEEN CHANGED SINCE PYTHON 3 CAME OUT. THANK YOU. -warned by Hidayat-
## saya dah bagi amaran, jangan kata saya tak payung kalau tiba-tiba tak boleh nak "run" koding saya...

#### -- (1) DECLARATIONS -- ###
##---------------Declare the container
root = Tk()                                                     ## Declare GUI object
winwidth = 620                                                  ## Declare window width
winheight = 310                                                 ## Declare window height
screenwidth = root.winfo_screenwidth()                          ## Get current display screen width
screenheight = root.winfo_screenheight()                        ## Get current display screen height
coorx = (screenwidth/2) - (winwidth/2)                          ## Calculate x-coordinate for center position
coory = (screenheight/2) - (winheight/2)                        ## Calculate y-coordinate for center position
root.title("Ringgit Malaysia to Foreign Currency Converter")               ## Declare main title
root.geometry('%dx%d+%d+%d' % (winwidth,winheight,coorx,coory)) ## Ask python to display window at specified size and position
root.configure(background='grey')                               ## Declare main background

##[1]---------------Declare the frames inside container
TopMainFrame = Frame(root, width=620, height=60, bg="grey", bd=8)
TopMainFrame.pack(side=TOP)
CenterMainFrame = Frame(root, width=620, height=150, bg="white", bd=8, relief="ridge")
CenterMainFrame.pack(side=TOP, expand=TRUE)
BottomMainFrame = Frame(root, width=620, height=100, bg="grey", bd=8, relief="ridge")
BottomMainFrame.pack(side=BOTTOM)

##[1]---------------Declare values needed to use
uservalue = StringVar()    ## To store value of country selected
convertvalue = DoubleVar() ## Value of money to be convert
resultvalue = DoubleVar()  ## Store result of converted money
convertonline = StringVar()## Value for passing money value
convertonline = '0'        ## Set default value
##global towardcon           ## Value for passing currency value
##towardcon = "MYR"          ## Set default value
##global currencyused        ## Value for passing currency used
##currencyused = StringVar() ## Set default value

#### -- (2) DEFINITIONS -- ####
##[2]---------------Define convert resultvalue function
def conCurrency():
    if (convertonline =='0'):
      if(uservalue.get()=="Select country or region"):
        tkMessageBox.showinfo("Select country first!","Please select country or region to convert first.\nThank you.")
      elif(uservalue.get()=="Brunei"):
        convert1=float(convertvalue.get() * 0.33)
        convert2 = "B$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Cambodia"):
        convert1=float(convertvalue.get() * 994)
        convert2 = str(convert1) + " " + u'\u17db'
        resultvalue.set(convert2)
      elif(uservalue.get()=="China"):
        convert1=float(convertvalue.get() * 1.62)
        convert2 = u'\u00a5' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="East Timor"):
        convert1=float(convertvalue.get() * 0.24)
        convert2 = "$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Hong Kong"):
        convert1=float(convertvalue.get() * 1.88)
        convert2 = "HK$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="India"):
        convert1=float(convertvalue.get() * 16.17)
        convert2 = u'\u20b9'+" " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Indonesia"):
        convert1=float(convertvalue.get() * 3168)
        convert2 = "Rp. " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Japan"):
        convert1=float(convertvalue.get() * 25)
        convert2 = u'\u00a5' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Kuwait"):
        convert1=float(convertvalue.get() * 0.073)
        convert2 = str(convert1) + " " + u'\u0643' + "." + u'\u062f'
        resultvalue.set(convert2)
      elif(uservalue.get()=="Laos"):
        convert1=float(convertvalue.get() * 1966)
        convert2 = u'\u20ad' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Macao"):
        convert1=float(convertvalue.get() * 1.94)
        convert2 = "MOP$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Myanmar"):
        convert1=float(convertvalue.get() * 301)
        convert2 = "K " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Philippines"):
        convert1=float(convertvalue.get() * 11.66)
        convert2 = u'\u20b1'+" " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Saudi Arabia"):
        convert1=float(convertvalue.get() * 0.91)
        convert2 = str(convert1) + " " + u'\ufdfc'
        resultvalue.set(convert2)
      elif(uservalue.get()=="Singapore"):
        convert1=float(convertvalue.get() * 0.33)
        convert2 = "S$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="South Korea"):
        convert1=float(convertvalue.get() * 268)
        convert2 = u'\u20a9' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Taiwan"):
        convert1=float(convertvalue.get() * 7.6)
        convert2 = str(convert1) + " " + u'\u5713'
        resultvalue.set(convert2)
      elif(uservalue.get()=="Thailand"):
        convert1=float(convertvalue.get() * 8.4)
        convert2 = u'\u0e3f' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="United Arab Emirates"):
        convert1=float(convertvalue.get() * 0.89)
        convert2 = str(convert1) + " " + u'\u062f' + "." + u'\u0673'
        resultvalue.set(convert2)
      elif(uservalue.get()=="United Kingdom"):
        convert1=float(convertvalue.get() * 0.19)
        convert2 = u'\u00a3' + " " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="United States of America"):
        convert1=float(convertvalue.get() * 0.24)
        convert2 = "$ " + str(convert1)
        resultvalue.set(convert2)
      elif(uservalue.get()=="Vietnam"):
        convert1=float(convertvalue.get() * 5407)
        convert2 = u'\u20ab' + " " + str(convert1)
        resultvalue.set(convert2)
    elif (convertonline =='1'):
      global towardcon, currencyused
      if(uservalue.get()=="Select country or region"):
        tkMessageBox.showinfo("Select country first!","Please select country or region to convert first.\nThank you.")
      elif(uservalue.get()=="Brunei"):
        towardcon='BND'
        currencyused = 'B$ '
        onlineConvert()
      elif(uservalue.get()=="Cambodia"):
        towardcon = 'KHR'
        currencyused = " " + u'\u17db'
        onlineConvert()
      elif(uservalue.get()=="China"):
        towardcon = 'CNY'
        currencyused = u'\u00a5'+" "
        onlineConvert()
      elif(uservalue.get()=="East Timor"):
        towardcon = 'USD'
        currencyused =  "$ "
        onlineConvert()
      elif(uservalue.get()=="Hong Kong"):
        towardcon = 'HKD'
        currencyused = "HK$ "
        onlineConvert()
      elif(uservalue.get()=="India"):
        towardcon = 'INR'
        currencyused = u'\u20b9'+" " 
        onlineConvert()
      elif(uservalue.get()=="Indonesia"):
        towardcon = 'IDR'
        currencyused = "Rp. "
        onlineConvert()
      elif(uservalue.get()=="Japan"):
        towardcon = 'JPY'
        currencyused = u'\u00a5'+" "
        onlineConvert()
      elif(uservalue.get()=="Kuwait"):
        towardcon = 'KWD'
        currencyused = " " + u'\u0643' + "." + u'\u062f'
        onlineConvert()
      elif(uservalue.get()=="Laos"):
        towardcon = 'LAK'
        currencyused = u'\u20ad'+" "
        onlineConvert()
      elif(uservalue.get()=="Macao"):
        towardcon = 'MOP'
        currencyused = "MOP$ "
        onlineConvert()
      elif(uservalue.get()=="Myanmar"):
        towardcon = 'MMK'
        currencyused = "K "
        onlineConvert()
      elif(uservalue.get()=="Philippines"):
        towardcon = 'PHP'
        currencyused = u'\u20b1'+" " 
        onlineConvert()
      elif(uservalue.get()=="Saudi Arabia"):
        towardcon = 'SAR'
        currencyused = " " + u'\ufdfc'
        onlineConvert()
      elif(uservalue.get()=="Singapore"):
        towardcon = 'SGD'
        currencyused = "S$ " 
        onlineConvert()
      elif(uservalue.get()=="South Korea"):
        towardcon = 'KRW'
        currencyused = u'\u20a9' + " "
        onlineConvert()
      elif(uservalue.get()=="Taiwan"):
        towardcon = 'TWD'
        currencyused = " " + u'\u5713'
        onlineConvert()
      elif(uservalue.get()=="Thailand"):
        towardcon = 'THB'
        currencyused = u'\u0e3f' + " "
        onlineConvert()
      elif(uservalue.get()=="United Arab Emirates"):
        towardcon = 'AED'
        currencyused = " " + u'\u062f' + "." + u'\u0673'
        onlineConvert()
      elif(uservalue.get()=="United Kingdom"):
        towardcon = 'GBP'
        currencyused = u'\u00a3' + " "
        onlineConvert()
      elif(uservalue.get()=="United States of America"):
        towardcon = 'USD'
        currencyused = "$ "
        onlineConvert()
      elif(uservalue.get()=="Vietnam"):
        towardcon = 'VND'
        currencyused = u'\u20ab' + " "
        onlineConvert()

##[2]---------------Define link parser to convert rich page website into just HTML
class LinksParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'span':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'class' and value == 'bld': 
        break
    else:
      return
    self.recording = 1

  def handle_endtag(self, tag):
    if tag == 'span' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)
      separator = ' '
      text = self.data[0]
      text2 = text.split(separator, 1)[0]
      if(currencyused==" "+u'\u17db')or(currencyused==" "+u'\u5713')or(currencyused==" " + u'\ufdfc')or(currencyused==" "+u'\u0643'+"."+u'\u062f')or(currencyused==" "+u'\u062f'+"."+u'\u0673'):
        text3=text2+currencyused
      else:
        text3=currencyused+text2
      resultvalue.set(text3)

##[2]---------------Define function for online conversion using google
def onlineConvert():
    try:
        p = LinksParser()
        f = urllib.urlopen("https://www.google.com/finance/converter?a="+str(convertvalue.get())+"&from=MYR&to="+str(towardcon))
        html = f.read()
        p.feed(html)
        p.close()
    except Exception as e:
        tkMessageBox.showinfo("No internet","This program can't connect to fetch conversion. Please make sure you're connected to the internet and try again.") 

##[2]---------------Define ask box when user click offline button
def ClickOffline():
    AskOffline=tkMessageBox.askyesno("Switch to Offline mode","Do you want to switch back to offline mode?\n\n"+
                                     "Offline mode conversion might not be accurate, it is only for refference.")
    if AskOffline>0:
        MakeItOffline()
        return

##[2]---------------Define what to do for offline button action
def MakeItOffline():
    global convertonline
    convertonline ='0'
    btnOnline['state']='normal'
    btnOffline['state']='disabled'

##[2]---------------Define ask box when user click online button
def ClickOnline():
    AskOnline=tkMessageBox.askyesno("Switch to Online mode","Do you want to switch to online mode?\n\n"+
                                     "Online mode requires internet connection, please ensure you're connected to the internet.\n\n"+
                                     "The program might freeze for a while when it is fetching conversion especially on slow internet, "+
                                     "so please be patient and wait this program fetch the conversion.")
    if AskOnline>0:
        MakeItOnline()
        return

##[2]---------------Define what to do for online button action
def MakeItOnline():
    global convertonline
    convertonline='1'
    btnOnline['state']="disabled"
    btnOffline['state']="normal"

##[2]---------------Define what to do for info button action
def ShowInfo():
    tkMessageBox.showinfo("RCS1105H Python Mini Project","CSC305 - PROGRAMMING PARADIGMS - MINI PROJECT\n"+
                          "Ringgit Malaysia to Foreign Currency Converter\n"+
                          "Version: 3.2 (r160925)\n\n"+
                          "Group: RCS1105H\n\n"+
                          "Members:\n"+
                          "         Ainaa Nasuha\n"+
                          "         Nazatul Shahira\n"+
                          "         Muhammad Saiful Asyraf\n"+
                          "         Muhammad Nur Hidayat\n\n\n"+
                          "This python programme was created from the scratch by referring official documentation. "+
                          "Whenever we are stuck, we will look the problem in StackOverflow, so thanks them too! ^_^\n\n"+
                          "(C) 2016 Hidayat, Asyraf, Ainaa, Nazatul. Part of rights reserved.\n"+
                          "Google currency data fetched in online mode is copyrighted by (C) Google, inc. "+
                          "and we believe its usage falls under fair use since it is published online.")

##[2]---------------Define what to do for exit button action
def AskExit():
    AskExit=tkMessageBox.askyesno("Exit System","Do you want to quit?")
    if AskExit>0:
        root.destroy()
        return

##[2]---------------Define what to do for reset button action
def Reset():
    uservalue.set("Select country or region")
    convertvalue.set("0.0")
    resultvalue.set("0.0")

#### -- (3) MAIN CLASS OF THE PROGRAM -- ####
##[3]---------------Put buttons into top frames
btnOnline = Button(TopMainFrame, state='normal', text='Online Convert', padx=2, pady=2, bd=3, bg="grey", fg="black",
                   activebackground="grey", font=('impact', 20, 'normal'), width=16, height=1, command=ClickOnline, relief="raise")
btnOnline.grid(row=0,column=0)
btnOffline = Button(TopMainFrame, state='disabled', text='Offline Convert', padx=2, pady=2, bd=3, bg="grey", fg="black",
                    activebackground="grey", font=('impact', 20, 'normal'), width=16, height=1, command=ClickOffline, relief="raise")
btnOffline.grid(row=0,column=1)
btnInfo = Button(TopMainFrame, text='Info', padx=2, pady=2, bd=3, bg="grey", fg="black",
                    activebackground="grey", font=('impact', 20, 'normal'), width=6, height=1, command=ShowInfo, relief="raise")
btnInfo.grid(row=0,column=2)

##[3]---------------Put text into center frame
lblRinggit= Label (CenterMainFrame,font=('arial',16,'bold'), text='Ringgit Malaysia RM', padx=2, pady=2, bd=1, fg="black", bg="white", width=20)
lblRinggit.grid(row=0,column=0)

##[3]---------------Put user input textbox into center frame
EntCurrency = Entry(CenterMainFrame,font=('arial',16,'bold'), textvariable=convertvalue, bd=1, fg="orange", width=22, justify='center')
EntCurrency.grid(row=0,column=1)

##[3]---------------Put drop down combobox into center frame
box = ttk.Combobox(CenterMainFrame,textvariable=uservalue, state='readonly',font=('arial',16,'bold'),width=22)
box['values'] = ('Select country or region','Brunei','Cambodia','China','East Timor','Hong Kong','India','Indonesia','Japan','Kuwait','Laos','Macao','Myanmar',
                 'Philippines','Saudi Arabia','Singapore','South Korea','Taiwan','Thailand','United Arab Emirates','United Kingdom','United States of America','Vietnam')
box.current(0)
box.grid(row=1, column=0)

##[3]---------------Put the converted currency text into the center frame
lblCurrency = Label (CenterMainFrame,font=('arial',16,'bold'), textvariable=resultvalue, bd=1, width=20, bg='white', fg="green", padx=2, pady=2, relief='sunken')
lblCurrency.grid(row=1,column=1)

##[3]---------------Put the buttons into bottom frame
btnConvert = Button(BottomMainFrame, text='Convert', padx=2, pady=2, bd=3, bg="white", fg="black", activebackground="grey",
                    font=('impact', 20, 'normal'), width=12, height=1, command=conCurrency, relief="raise").grid(row=0,column=1)
btnReset = Button(BottomMainFrame, text='Reset', padx=2, pady=2, bd=3, bg="white", fg="black", activebackground="grey",
                  font=('impact', 20, 'normal'), width=12, height=1, command=Reset, relief="raise").grid(row=0,column=2)
btnExit = Button(BottomMainFrame, text='Exit', padx=2, pady=2, bd=3, bg="white", fg="black", activebackground="grey",
                 font=('impact', 20, 'normal'), width=12, height=1, command=AskExit, relief="raise").grid(row=0,column=3)

##[3]---------------Make sure program GUI continues to run unless exited
root.mainloop()
