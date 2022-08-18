import json 
import tkinter as tk
from tkinter.constants import NE, NSEW, X
from tkinter import messagebox as mb
from validation import validation

def load_data(e,t):
    e.delete(0,"end")
    e.insert(0 ,t)
    return

vervar = [ 'HBD(mm/mm)' , 't(mm)' , 'Eh(GPa)' , 'D(mm)' , 'Pc(kPa)' , 'Pw(kPa)' , 'Ps(kPa)' , 'Sb(mm/mm)' , 'Df(-)' , 'Tt(mm)' , 
    'δd/D(%)' ,  'γs(N/m³)' , 'Hmax(m)' , 'Hmin(m)' , 'LLDF(-)' , 'P(N)' , 'Sc(-)' ,  'Msb max(MPa)' , 'Msb min(MPa)' , 
        'DL(-)' , 'Kx(-)' , 'PS(kPa)' ,  'Eht(GPa)' , 'Pss(m)' , 'Pv(kPa)'  ]


testvars = [
    '1. Confirmer la classe de pression :',	
    "2. Vérification de la pression de travail :",
    "3. Vérification de la pression de surpression :",
    "4. Vérification de la déflexion maximale admissible :", 
    "5. Calcul de charge verticale du sol sur le tuyau :",
    "6. Calculer les charges dynamiques :",
    "7. Détermination module de contrainte du sol composite Ms :",
    "8. Vérification de la déflexion :",
    "9. Vérifier la charge combinée :",
    "10. Vérifier le flambage :"
       ]

labtext = {}

testg = {}

data = {'HBD(mm/mm)': 0.0065, 't(mm)': 15.5, 'Eh(GPa)': 12.5, 'D(mm)': 908.5, 'Pc(kPa)': 1000, 'Pw(kPa)': 800, 'Ps(kPa)': 375, 
'Sb(mm/mm)': 0.012, 'Df(-)': 5.5, 'Tt(mm)': 16.5, 'δd/D(%)': 5, 
'γs(N/m³)': 18800, 'Hmax(m)': 2.5, 'Hmin(m)': 1.2, 
'LLDF(-)': 1.15, 'P(N)': 90000, 'Sc(-)': 2.3, 
'Msb max(MPa)': 8.4, 'Msb min(MPa)': 7.8, 'DL(-)': 1.05, 
'Kx(-)': 0.1, 'PS(kPa)': 250, 'Eht(GPa)': 12.5, 'Pss(m)': 1, 'Pv(kPa)': 100}


def getvalues():
    global testg , ff2

    ff2.destroy()
    ff2 = tk.Label( f2, width=800, height=580)
    ff2.place(x= 0 , y = 0, anchor='nw')

    for elm in dataentry:    
        try:
            data[elm] = float(dataentry[elm].get())
        except:
            mb.showerror('Attention', 'Veuillez vérifier que les données sont des nombres et non des caractères')
            return
    
    testg = validation(data) #importation de validation
    vtext.destroy()
    rc = 0 #ligne
    r2 = 0
    for elm in testvars: 
        labtext[elm] = tk.Label(ff2, text= elm) #affichage des etapes dans la 1ére columne
        labtext[elm].grid(row = rc, rowspan= 2, column=5, columnspan=4, sticky="nw",ipadx= 15,ipady=2)
        spvalue = testg[elm].split(";") 
        
        for col, sp in enumerate(spvalue):
            
            
           tk.Label( ff2, text= str(sp) ).grid( row = rc, rowspan= 1, column=9 + col*2, columnspan=2, sticky="nw",ipadx= 20,ipady=2 )
        rc+= 1
           







# Construction de la fenêtre
Validation = tk.Tk()
Validation.title ("Vérification des tuyaux enterrés en GRP")
Validation.geometry("850x650+0+0")
Validation.minsize(1200, 680)
Validation.maxsize(1360, 720)
Validation.iconbitmap('C:\\Users\\nael atn\\Desktop\\inspection.ico')


# Construction du conteneur 
f1 = tk.Frame(Validation)
f1.place(x=5,y=15, anchor='nw')

dataentry = {}
datavar = {}

# Construction de l'interface de saisie des données 
col = 0
k=0
for i,j in enumerate(data.keys()):
    if (i == 19):
        col = 3
        k=0

    tk.Label(f1, text=j,pady=5, padx= 5).grid(column=col, row= k)
     
    dataentry[j] = tk.Entry(f1, width=10)
    dataentry[j].grid(column=col+1, row= k, pady = 5, padx=5)



    load_data(dataentry[j], data[j])
    k= k+1

#Création du conteneur résultat
f2 = tk.LabelFrame( Validation, text = ' Résultat '  , width=800, height=580)
f2.place(x= 320 , y = 15, anchor='nw')

ff2 = tk.Label( f2, width=800, height=580)
ff2.place(x= 0 , y = 0, anchor='nw')

#Initialisation du conteneur résultat avec un texte qui contient une instruction pour lance la simulation
vtext = tk.Label(f2, text= 'Appuiez sur simuler pour vérifier', font=('courier',12,'underline') )
vtext.place(x=250, y = 250)

#Création d'un bouton qui permet de lancer la fonction getvalues décrites ci-dessus
sim = tk.Button(f1, text="Simuler !",activebackground='royal blue', command=getvalues )
sim.grid(column=0, columnspan=2, row=i+3, rowspan= 2, pady=9, ipadx=15, ipady=2)


Validation.mainloop()







