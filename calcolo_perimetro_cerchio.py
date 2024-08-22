#calcolo perimetro 
import math

quadrato = 4
rettangolo =2
p=3.14
x= 2 
r=2 

scelta_calcolo = int(input("premi 1 per quadrato, premi 2 rettangolo, premi 3 per triangolo,4  "))
if scelta_calcolo == 1 :
    print (f"il perimetro {quadrato}*{4} è = {quadrato*4}")

elif scelta_calcolo == 2 :
    h=int(input("inserisci altezza h : "))
    print(f"il perimetro {rettangolo}*{h} = {rettangolo*h}")

elif scelta_calcolo == 3 :
    r=float(input("inserisci il raggio :"))
    print(f"il perimetro del cerchio {x}*{p}*{r} e' = {x*p*r}")

elif scelta_calcolo == 4:
    print("questo terminale si autodistruggera' in 3...2...1")


    


 
          
   
