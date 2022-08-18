

from tkinter.messagebox import OK


def validation(dataentry):

    hbd= dataentry['HBD(mm/mm)'] #assignier les valeurs d'entrées a nos label
    t= dataentry['t(mm)']
    eh= dataentry['Eh(GPa)']
    d= dataentry['D(mm)']
    pc= dataentry['Pc(kPa)']
    pw= dataentry['Pw(kPa)']
    ps= dataentry['Ps(kPa)']
    sb= dataentry['Sb(mm/mm)']
    df= dataentry['Df(-)']
    tt= dataentry['Tt(mm)']
    stigmad = dataentry['δd/D(%)']
    nustigma= dataentry['γs(N/m³)']
    hmax= dataentry['Hmax(m)']
    hmin= dataentry['Hmin(m)']
    lldf= dataentry['LLDF(-)']
    p= dataentry['P(N)']
    sc= dataentry['Sc(-)']
    Msbmax = dataentry['Msb max(MPa)']
    Msbmin = dataentry['Msb min(MPa)']
    dl= dataentry['DL(-)']
    kx= dataentry['Kx(-)']
    PS = dataentry['PS(kPa)']
    eht= dataentry['Eht(GPa)']
    pss= dataentry['Pss(m)']
    pv= dataentry['Pv(kPa)']


    
    print("""...................simumation...............
    ----
    ----
    Résultat :  """)


    print("1. Confirmer la classe de pression :")
    test = (hbd/1.8)*(2*t*eh/d) * 10**6

    if (pc < test):
        print("Pc = ", pc," < ", test)
        print("OK")
        r1 =  f"Pc = {pc:.2f} kPa < {test:.2f} kPa ; OK"
    else:
        print("Pc = ", pc," > ", test)
        print("Non Valide !")
        r1 =  f"Pc = {pc:.2f} kPa > {test:.2f} kPa ; Non Valide !"
        
        
    
    print("2. Vérification de la pression de travail :")
    
    
    if ( pw <= pc):
        print("Pc =", pc," >= ", pw)
        print("OK")
        r2 =  f"Pc = {pc:.2f} kPa >= {pw:.2f} kPa ;OK"
    else:
        print("Pc =", pc," < ", pw)
        print("Non Valide !")
        r2 =  f"Pc = {pc:.2f} kPa < {pw:.2f} kPa ;Non Valide !"
        
        
    
    print("3. Vérification de la pression de surpression :")
    
    
    if ( ((ps + pw)/1.4) <= pc):
        print( (ps + pw)/1.4 , " <= Pc = ",pc)
        print("OK")
        r3 =  f"Pc = {pc:.2f} kPa >=  {(ps + pw)/1.4:.2f} kPa ;OK"
    else:
        print( (ps + pw)/1.4 , " > Pc = ",pc)
        print("Non Valide !")
        r3 =  f"Pc = {pc:.2f} kPa <  {(ps + pw)/1.4:.2f} kPa ;Non Valide !"
        

    print("4. Vérification de la déflexion maximale admissible :")
    

    delta_ya = (sb * d*d /(1.5 * df * tt))
    print("delta_ya =", delta_ya)


    #test1 = df *(delta_ya/d) * (tt/d) 


    if ( delta_ya * 100 / d >= stigmad ):
        print("Δya/D =",  delta_ya * 100 / d  ," >= ", stigmad)
        print("OK")
        r4 =  f"Δya/D = {delta_ya * 100 / d:.2f} % >= δd/D = {stigmad:.2f} % ;OK"
    else:
        print("Δya/D =", delta_ya * 100 / d  ," < ", stigmad)
        print("Non Valide !")
        r4 =  f"Δ/ya = {delta_ya :.2f} \n\nΔya/D = {delta_ya * 100 / d:.2f} % < δd/D = {stigmad:.2f} % ;Non Valide !"
       
    print("5. Calcul de charge verticale du sol sur le tuyau :")

    wcmax = nustigma * hmax
    wcmin = nustigma * hmin

    print("Wcmax =" , wcmax)
    print("Wcmin =" , wcmin)

    r5 = f'Wcmax = {wcmax:.2f} N/m² \n\nWcmin = {wcmin:.2f} N/m²'
    #Calculer les charges dynamiques
    print("6. Calculer les charges dynamiques :")

    ifmax = 1 + 0.33*((2.44 - hmax)/ 2.44)
    ifmin = 1 + 0.33*((2.44 - hmin)/ 2.44)

    l1max = 0.254 + lldf * hmax
    l1min = 0.254 + lldf * hmin

    hint = (1.83 - 0.5)/ lldf


    if (hmax<= hint):
        l2max = 0.5 + lldf * hmax 
        print("l2max =", l2max)
    else:
        l2max = (0.5 + 1.83 +lldf * hmax)/2 
        print("l2max =", l2max)

    if (hmin >= hint):
        l2min = (0.5 + 1.83 + lldf * hmin)/2
        print("l2min =", l2min)
    else:
        l2min = 0.5 + lldf * hmin
        print("l2min =", l2min)


    wlmax = 1.2 * p * ifmax / (l1max*l2max)
    wlmin = 1.2 * p * ifmin / (l1min * l2min)
    
    print("wlmax =", wlmax)
    print("wlmin =", wlmin)

    r6 = f'Wlmax = {wlmax:.2f} N/m² \n\nWlmin = {wlmin:.2f} N/m²'

    print("7. Détermination module de contrainte du sol composite Ms :")


    msmax = sc * Msbmax
    msmin = sc * Msbmin

    print("msmax =", msmax)
    print("msmin =", msmin)

    r7 = f'Msmax = {msmax:.2f} MPa \n\nMsmin = {msmin:.2f} MPa'


   #"8. Vérification de la déflexion :"
    

    delta_ymax_d = ((dl * wcmax) + wlmax ) * kx / (( 149 * PS) + ( 61000 * msmax)) * 100
    delta_ymin_d = ((dl * wcmin) + wlmin ) * kx / (( 149 * PS + 61000 * msmin)) * 100

    print("ymax_d =",  delta_ymax_d )
    print("ymin_d =",  delta_ymin_d ) 

    if ( delta_ymax_d <= stigmad ):
        print("OK")
        print("ymax/ D ", delta_ymax_d ," <=  ", stigmad)
        r8 = f'ymax / D = {delta_ymax_d:.2f} % <= {stigmad:.2f} %'
        r81 = ";OK"

    else:
        print("ymax / D = ", delta_ymax_d ," >  ", stigmad)
        print("Non Valide !")
        r8 = f'ymax / D = {delta_ymax_d:.2f} % > {stigmad:.2f} %'
        r81 =  ";Non Valide !"
        

    if ( delta_ymin_d <= stigmad  ):
        print("OK")
        print("ymin / D",  delta_ymin_d ," <= ",  stigmad )
        r8 = r8 + "\n\n" + f'ymin / D = {delta_ymin_d:.2f} % <= {stigmad} %'
        r82 = "\n\nOK"

    else:
        print("ymin / D",  delta_ymin_d ," > ",  stigmad )
        print("Non Valide !")      
        r8 =  r8 + "\n\n" + f'ymin / D = {delta_ymin_d:.2f} % > {stigmad} %' 
        r82 =   "\n\nNon Valide !"

    
    
    print("9. Vérifier la charge combinée : ")  
    
    epsilone_pr = ( pw * d ) / (2 * 10**6 *(t * eht))

    epsilone_b = df * ( (stigmad) / 100 ) * ( tt / d )

    rc = 1 - pw / 3000

    print("ε pr", epsilone_pr)	
    print("ε b", epsilone_b)
    print("rc", rc)



    test2 = (1 - ((epsilone_b* rc)/sb)) / 1.8
    test3 = (1 - (epsilone_pr/hbd)) / 1.5

    if ( epsilone_pr / hbd <= test2):
        print("ε pr / hbd =",epsilone_pr / hbd ," <= ", test2 )
        
        print("OK")
        
        r9 = f'ε pr / HBD = {epsilone_pr / hbd:.2f}  <= {test2:.2f}'
        r91 = ";OK"
    else:
        print("ε pr / HBD =",epsilone_pr / hbd ," > ", test2 )
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")
        r9 = f'ε pr / HBD = {epsilone_pr / hbd:.2f}  >  {test2:.2f}'
        r91 =  ";Non Valide !"
        
    if ( ( epsilone_b * rc) /sb <= test3  ):
        
        print("ε b * rc)/sb =", ( epsilone_b* rc) /sb," <= " , test3 )
        print("OK")
        r9 = r9 + "\n\n" + f'ε b * rc / Sb = {( epsilone_b* rc) /sb:.2f}  <= {test3:.2f} '
        r92 = "\n\nOK"

    else:
        print("ε b * rc)/sb =", ( epsilone_b* rc) /sb," > " , test3 )
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")   
        r9 =  r9 + "\n\n" +  f'ε b * rc / Sb = {( epsilone_b* rc) /sb:.2f}  > {test3:.2f} '
        r92 =   "\n\nNon Valide !"                 

    print("10. Vérifier le flambage : ")
    
    rhmax = 11.4 / (11 + d /(1000 * hmax))
    rhmin = 11.4 / (11 + d /(1000 * hmin))

    EI = PS * 0.149 * ( d/2 + (stigmad)/100 * d/2 )**3 * 10**(-6)

    hwmax =  hmax - pss
    hwmin =  hmin - pss

    rwmax = 1 - 0.33 * (hwmax/ hmax)
    rwmin = 1 - 0.33 * (hwmin/ hmin)

    qamax = (1.2 * 0.55)*(EI**0.33)*((0.9* 10**6 * msmax * 0.74)**0.67) * rhmax / (2.5 * (d/2))
    qamin = (1.2 * 0.55)*(EI**0.33)*((0.9* 10**6 * msmin * 0.74)**0.67) * rhmin / (2.5 * (d/2))

    testqmax = (9800* hwmax + rwmax * wcmax + wlmax ) * 10 ** -3 + pv
    testqmin = (9800* hwmin + rwmin * wcmin + wlmin ) * 10 ** -3 + pv 

    #print("hwmax =", hwmax,"\n\nhwmin =",hwmin, "\n\nrwmax =", rwmax,"\n\nrwmin =", rwmin, "\n\nqamax =", qamax, "\n\nqamin =", qamin)

    #1eme vérification
    if ( testqmax <= qamax ) :
        print(testqmax , "<= qamax =", qamax )
        print("OK")
        r10 = f'{testqmax:.2f} kPa <= qamax = {qamax:.2f} kPa '
        r101 = ";OK"


    else:
        print(testqmax , "> qamax =", qamax )
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")
        r10 = f'{testqmax:.2f} kPa > qamax = {qamax:.2f} kPa'
        r101 = ";Non Valide !"

    if ( testqmin <= qamin  ):
        
        print(testqmin , "<= qamin =", qamin)
        print("OK")
        r10 = r10 + "\n\n" + f'{testqmin:.2f} kPa <= qamin = {qamin:.2f} kPa'
        r101 = r101 + "\n\nOK"

    else:
        print(testqmin , "> qamin =", qamin)
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")
        r10 = r10 + "\n\n" + f'{testqmin:.2f} kPa > qamin = {qamin:.2f} kPa'
        r101 = r101 + "\n\nNon Valide !"


    #2eme vérification
    if ( testqmax - pv <= qamax ) :
        print(testqmax , "<= qamax =", qamax )
        r10 = r10 + "\n\n" + f'{testqmax - pv:.2f} kPa <= qamax = {qamax:.2f} kPa'
        r101 = r101 + "\n\nOK"

        print("OK")
    else:
        print(testqmax - pv , "> qamax =", qamax )
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")
        r10 = r10 + "\n\n" + f'{testqmax - pv:.2f} kPa > qamax = {qamax:.2f} kPa'
        r101 = r101 + "\n\nNon Valide !"

    if ( testqmin - pv <= qamin  ):
        
        print(testqmin - pv, "<= qamin =", qamin)
        print("OK")
        r10 = r10 + "\n\n" + f'{testqmin - pv:.2f} kPa <= qamin = {qamin:.2f} kPa'
        r101 = r101 + "\n\nOK"

    else:
        print(testqmin - pv, "> qamin =", qamin)
        print("!!!!!!!!!  Non Valide !!!!!!!!!! \n\n")
        r10 = r10 + "\n\n" + f'{testqmin - pv:.2f} kPa > qamin = {qamin:.2f} kPa'
        r101 = r101 + "\n\nNon Valide !"


    r8 = r8 + r81 + r82
    r9 = r9 + r91 + r92
    r10 = r10 + r101

    return {"1. Confirmer la classe de pression :" : r1,
    "2. Vérification de la pression de travail :" : r2,
    "3. Vérification de la pression de surpression :" : r3,
    "4. Vérification de la déflexion maximale admissible :" : r4,
    "5. Calcul de charge verticale du sol sur le tuyau :" : r5,
    "6. Calculer les charges dynamiques :" : r6,
    "7. Détermination module de contrainte du sol composite Ms :" :r7,
    "8. Vérification de la déflexion :" : r8,
    "9. Vérifier la charge combinée :" :  r9,
    "10. Vérifier le flambage :" : r10,
    
     }





