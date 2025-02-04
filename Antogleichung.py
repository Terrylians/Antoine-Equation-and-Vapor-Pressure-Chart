import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('Antoine.csv',sep=';')
print('Wasser (0-99) : H20, Wasser (99-374) H20s')
formula=input('Bitte geben Sie die Formel ein: ')

name=formula
formula_value=df.loc[df['Formula']==formula]

while formula_value.empty:
        print('Die Formel ist nicht in der Liste')
        formula=input('Bitte geben Sie die Formel ein: ')
        formula_value=df.loc[df['Formula']==formula]
        name=formula

compound_name=formula_value['Compound Name'].values[0]
formula_name=formula_value['Formula'].values[0]
A=formula_value['A'].values[0]
B=formula_value['B'].values[0]
C=formula_value['C'].values[0]
Tmin=formula_value['TMIN'].values[0]
Tmax=formula_value['TMAX'].values[0]
def Antoine(T,A,B,C):
            P=10**(A-B/(T+C))
            return P

def savefigure():
    inputtingvalue=input("Möchten Sie die Druckkurve speichern ?(J/N)")
    if inputtingvalue=='J':
                 
                 print('Die Druckkurve wurde als Druckkurve.pdf gespeichert')

    else:
        plt.close()
   

def Druckkurvemmhg ():

    xs=np.linspace(Tmin,Tmax,100)
    ys=Antoine(xs,A,B,C)
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in mmHg')
    plt.title('Dampfdruckurve von '+name) 
    plt.show()
    savefigure()
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in mmHg')
    plt.title('Dampfdruckurve von '+name) 
    plt.savefig('Druckkurve.pdf',format='pdf')
    plt.close()

def DruckkurvePa():
    xs=np.linspace(Tmin,Tmax,100)
    ys=Antoine(xs,A,B,C)
    ys=ys*133.322
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in Pa')
    plt.title('Dampfdruckurve von '+name) 
    plt.show()
    savefigure()
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in Pa')
    plt.title('Dampfdruckurve von '+name) 
    plt.savefig('Druckkurve.pdf',format='pdf')
    plt.close()

def DruckkurveBar():
    xs=np.linspace(Tmin,Tmax,100)
    ys=Antoine(xs,A,B,C)
    ys=ys*133.322
    ys=ys/100000
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in Bar')
    plt.title('Dampfdruckurve von '+name) 
    plt.show()
    savefigure()
    plt.plot(xs,ys,'r')
    plt.grid()
    plt.xlabel('Temperatur in °C')
    plt.ylabel('Druck in Bar')
    plt.title('Dampfdruckurve von '+name) 
    plt.savefig('Druckkurve.pdf',format='pdf')
    plt.close()

def eingabe():

    option=input("Welche Operation ? (1. Antoinerechner (1), 2. Druckkurve(2)) ")
    if option=='1':
        Antoinerechner()
    elif option=='2':
        Auswahldruckkurve()

def Auswahldruckkurve():
     auswahl=input('Bitte geben Sie die Druckeinheit ein: (1. mmHg - ºC (1)) (2. Pa - ºC (2)) (3. Bar - ºC (3)) ')
     if auswahl == '1':
         Druckkurvemmhg()
     elif auswahl == '2':
            DruckkurvePa()
     elif auswahl == '3':
            DruckkurveBar()
    

def Antoinerechner():
    
    
    print("Antoine Konstanten: \nA=",A,"\nB=",B,"\nC=",C)
    def Pascal(mmhg):
        pa=mmhg*133.322
        return pa
    def Bar(pa):
        bar=pa/100000
        return bar
    print('Der Temperaturbereich ist' + str(Tmin) + '°C bis ' + str(Tmax) + '°C')
    T=float(input('Bitte geben Sie die Temperatur ein: '))

    def Auswahlrechnerdruckkurve():
        eingang=input('Bitte geben Sie die Druckeinheit ein: (1. mmHg - ºC (1)) (2. Pa - ºC (2)) (3. Bar - ºC (3)) ')
        if eingang == '1':

            xs=np.linspace(Tmin,Tmax,100)
            ys=Antoine(xs,A,B,C)
            marker=Antoine(T,A,B,C)
            plt.plot(xs,ys,'r')
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.title('Dampfdruckurve von '+name) 
            plt.ylabel('Druck in mmHg')
            plt.grid()
            plt.show()
            print('Der Dampfdruck beträgt',Antoine(T,A,B,C),'mmHg')
            savefigure()
            plt.plot(xs,ys,'r')
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.title('Dampfdruckurve von '+name) 
            plt.ylabel('Druck in mmHg')
            plt.grid()
            plt.savefig('Druckkurve.pdf',format='pdf')
            plt.close()


            print('Der Dampfdruck beträgt',P,'mmHg')
        elif eingang == '2':
            xs=np.linspace(Tmin,Tmax,100)
            ys=Pascal(Antoine(xs,A,B,C))
            marker=Pascal(Antoine(T,A,B,C))
            plt.plot(xs,ys,'r')
            plt.title('Dampfdruckurve von '+name) 
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.ylabel('Druck in Pa')
            plt.grid()
            plt.show()
            print('Der Dampfdruck beträgt',Pascal(P),'Pa')
            savefigure()
            plt.plot(xs,ys,'r')
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.title('Dampfdruckurve von '+name) 
            plt.ylabel('Druck in Pa')
            plt.grid()
            plt.show()
            plt.savefig('Druckkurve.pdf',format='pdf')
            plt.close()
            
        elif eingang == '3':
            xs=np.linspace(Tmin,Tmax,100)
            ys=Bar(Antoine(xs,A,B,C))
            marker=Bar(Antoine(T,A,B,C))
            plt.plot(xs,ys,'r')
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.ylabel('Druck in Bar')
            plt.title('Dampfdruckurve von '+name) 
            plt.grid()
            plt.show()
            print('Der Dampfdruck beträgt',Bar(Pascal(P)),'Bar')
            savefigure()
            plt.plot(xs,ys,'r')
            plt.plot(T,marker,'bo',ms=5,label='Dampfdruck')
            plt.xlabel('Temperatur in °C')
            plt.ylabel('Druck in Bar')
            plt.title('Dampfdruckurve von '+name) 
            plt.grid()
            plt.show()
            plt.savefig('Druckkurve.pdf',format='pdf')
            plt.close()

  
    while True:
        if T<=Tmin or T>=Tmax:
            print('Die Temperatur liegt außerhalb des Temperaturbereichs')
            print('Der Temperaturbereich ist' + str(Tmin) + '°C bis ' + str(Tmax) + '°C')
            T=float(input('Bitte geben Sie die Temperatur ein: '))
            
        elif Tmin<T<Tmax:
            P=Antoine(T,A,B,C)
            Auswahlrechnerdruckkurve()
            print("Name :",compound_name, "Formula :", formula_name)
            break



    