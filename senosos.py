
import math

choose = 0

catetoposto = 0
catetadjacente = 0
hipotenusa = 0
sen = 0
cos = 0
tg = 0
cotg = 0
sec = 0
cossec = 0

fim = False

def escolher():
    global choose
    while choose == 0:
        r = input("Comando> (cateto oposto, cateto adjacente, hipotenusa, seno, cosseno, tangente, cotangente, secante, cossecante, status, executar sistema) r=")
        if r == "cateto oposto":
            choose = 1
        if r == "cateto adjacente":
            choose = 2
        if r == "hipotenusa":
            choose = 3
        if r == "seno":
            choose = 4
        if r == "cosseno":
            choose = 5
        if r == "tangente":
            choose = 6
        if r == "cotangente":
            choose = 7
        if r == "secante":
            choose = 8
        if r == "cossecante":
            choose = 9
        if r == "status":
            choose = 10
        if r == "executar sistema":
            choose = 11
        if r == "limpar":
            choose = 12
        else:
            print('ok')
while fim == False:
    escolher()
    if choose == 1:
        catetoposto = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 2:
        catetadjacente = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 3:
        hipotenusa = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 4:
        sen = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 5:
        cos = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 6:
        tg = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 7:
        cotg = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 8:
        sec = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 9:
        cossec = (float(input("Ofereça o valor: ")))
        r = 0
        choose = 0
    if choose == 10:

        print("Status: ")
        print(" ")
        print("Cateto oposto: "+str(catetoposto))
        print("Cateto adjacente: "+str(catetadjacente))
        print("Hipotenusa: "+str(hipotenusa))
        print("Seno: "+str(sen))
        print("Cosseno: "+str(cos))
        print("Tangente: "+str(tg))
        print("Cotangente: "+str(cotg))
        print("Secante: "+str(sec))
        print("Cossecante: "+str(cossec))
        r = 0
        choose = 0

    while choose == 11:
        if catetoposto != 0:
            r = 0
            choose = 0
            
        else:
            if sen and hipotenusa != 0:
                catetoposto = round(sen*hipotenusa, 4)
                r = 0
                choose = 0
            if hipotenusa and catetadjacente != 0:
                catetoposto = round(math.sqrt((hipotenusa**2)-(catetadjacente**2)), 4)
                r = 0
                choose = 0

        if catetadjacente != 0:
            r = 0
            choose = 0
            
        else:
            if cos and hipotenusa != 0:
                catetadjacente = round(sen*hipotenusa, 4)
                r = 0
                choose = 0
            if hipotenusa and catetoposto != 0:
                catetadjacente = round(math.sqrt((hipotenusa**2)-(catetoposto**2)), 4)
                r = 0
                choose = 0

        if hipotenusa != 0:
            r = 0
            choose = 0

        else:
            if catetoposto and catetadjacente != 0:
                hipotenusa = round(math.sqrt((catetadjacente**2)+(catetoposto**2)), 4)
        
        if sen != 0:
            r = 0
            choose = 0
        
        else:
            if catetoposto and hipotenusa != 0:
                sen = round(catetoposto/hipotenusa, 4)
                r = 0
                choose = 0
        
        if cos != 0:
            r = 0
            choose = 0

        else:
            if catetadjacente and hipotenusa != 0:
                cos = round(catetadjacente/hipotenusa, 4)
                r = 0
                choose = 0
        
        if tg != 0:
            r = 0
            choose = 0

        else:
            if catetadjacente and catetoposto != 0:
                tg = round(catetoposto/catetadjacente, 4)
                r = 0
                choose = 0
            if sen and cos != 0:
                tg = round(sen/cos, 4)
                r = 0
                choose = 0
            
        if sec != 0:
            r = 0
            choose = 0
        
        else:
            if cos !=0:
                sec = round(1/cos, 4)
                r = 0
                choose = 0

        if cossec != 0:
            r = 0
            choose = 0
        
        else:
            if sen !=0:
                cossec = round(1/sen, 4)
                r = 0
                choose = 0

        if cotg != 0:
            r = 0
            choose = 0
        
        else:
            if tg != 0:
                cotg = round(1/tg, 4)
                r = 0
                choose = 0
    
    if choose == 12:
        catetoposto = 0
        catetadjacente = 0
        hipotenusa = 0
        sen = 0
        cos = 0
        tg = 0
        cotg = 0
        sec = 0
        cossec = 0
        print("")
        print("Todos os parâmetros limpos!")
        print("")
        r = 0
        choose = 0
