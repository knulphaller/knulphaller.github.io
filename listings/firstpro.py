from tkinter import *
from os import system as system
from subprocess import Popen as open
wind = Tk()
wind.title('First Pro of Mine')
wind.wm_iconbitmap('pyc.ico')
wind.update()
wind.wm_attributes()
wind.minsize()
wind.state('zoomed')

def dxdiag():
	open('dxdiag')

button = Button(text="DirectX Diagnostika Paneli", 
		command=dxdiag)

button.grid()

def calculyator():
	open('calc')

button1 = Button(text='Kalkulyator', 
		command=calculyator)
button1.grid()


def contpanel():
	open('control')

button2 = Button(text='İdarəetmə Paneli',
				 command=contpanel)
button2.grid()

def wordpad():
	open('write')

button3 = Button(text='Wordpad', command=wordpad)
button3.grid()

def updatecenter():
	open('wuapp')

button4 = Button(text='Windows Yenilənmələr Mərkəzi', command=updatecenter)
button4.grid()

def rescuedisk():
	open('recdisc')

button5 = Button(text='Windows Xilasetmə Diski', command=rescuedisk)
button5.grid()

def compmg():
	open('compmgmtlauncher')

button6 = Button(text='Computer Managment', command=compmg)
button6.grid()

def cmd():
	os.system('cmd')

button7 = Button(text='Command Promt', command=cmd)
button7.grid()

def startm():
	open('control.exe /name Microsoft.TaskbarandStartMenu')

button8 = Button(text='Start Menyu Parametrləri', command=startm)
button8.grid()

def newdev():
	open('hdwwiz')

button9 = Button(text='Yeni Device Əlavə et', command=newdev)
button9.grid()

def notepad():
	open('notepad')

button10 = Button(text='Notepad', command=notepad)
button10.grid()

def backup():
	open('sdclt')

button11 = Button(text='Backup and Restore', command=backup)
button11.grid()

def components():
	open('dcomcnfg')

button12 = Button(text='Component Servisi', command=components)
button12.grid()

def netpro():
	open('netproj')

button13 = Button(text='Lokal Proyektora Qoşul', command=netpro)
button13.grid()

def time():
	os.system('timedate.cpl')

button14 = Button(text='Saat və Zaman ayarları', command=time)
button14.grid()

def proj():
	open('displayswitch')

button15 = Button(text='Proyektora Qoşul', command=proj)
button15.grid()

def sisproper():
	open('systempropertiesperformance')

button16 = Button(text='Sistem Performans Parametrləri', command=sisproper)
button16.grid()

def depproper():
	open("systempropertiesdataexecutionprevention")

button17 = Button(text="DEP Parametrləri", command=depproper)
button17.grid()

def chartap():
	open('charmap')

button18 = Button(text='Simvollar cədvəli', command=chartap)
button18.grid()

def cleartune():
	open('cttune')

button19 = Button(text='ClearType Parametrləri', command=cleartune)
button19.grid()

def color():
	open('colorcpl')

button20 = Button(text='Rəng Parametrləri', command=color)
button20.grid()

def devmgr():
	system('devmgmt.msc')

button21 = Button(text='Device Manager', command=devmgr)
button21.grid()

def cleanup():
	open('cleanmgr')

button22 = Button(text='Disklərin təmizlənməsi', command=cleanup)
button22.grid()

def defrag():
	open('dfrgui')

button23 = Button(text='Defragmentasiya', command=defrag)
button23.grid()

def diskman():
	system('diskmgmt.msc')

button24 = Button(text='Disklərin Idarə \nEdilməsi', command=diskman)
button24.grid()

def display():
	open('dpiscaling')

button25 = Button(text='Ekran', command=display)
button25.grid()

def calib():
	open('dccw')

button26 = Button(text='Ekranın Kalibrasiyasi', command=calib)
button26.grid()

def explorer():
	open('iexplore')

button27 = Button(text='Internet Explorer', command=explorer)
button27.grid(row=0, column=2)

def netpar():
	system('inetcpl.cpl')

button28 = Button(text='Internet Parametrləri', command=netpar)
button28.grid(row=1, column=2)
mainloop()
