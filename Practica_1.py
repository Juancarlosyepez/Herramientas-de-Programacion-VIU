# EJERCICIO 1 con strings, Identificador válido----------------------------

import re

def FirstChar(s):
    if s[0].isdigit() == True:
        valor = False
    else:
        reg_exp = "\w+$"
        valor = re.match(reg_exp, s) is not None
    print(valor)

FirstChar('paciente001')
FirstChar('P001')
FirstChar('1Pac')
FirstChar('_001')
FirstChar(':p001')


# EJERCICIO 2 con strings, Porcentaje de vocales -------------------------

def porcentVocal(s):
    
    vocales = 'aeiouAEIOU'
    nvocales = len([c for c in s if c in vocales])
    if len(s) != 0:
        porcentaje = round(nvocales/len(s)*100,1)
    else:
        porcentaje = 'ingrese cadena'
    print(porcentaje)
    
porcentVocal('Hola')
porcentVocal('Acacia')
porcentVocal('Brrrrrrr')
porcentVocal('aAe')


# EJERCICIO 3 con strings, Nuevo string---------------------------------------

def nuevo_string(s,n):
    vocales = 'aeiouAEIOU'
    nueva_cadena = ""
    for x in s:
        indice = vocales.find(x)
        if indice != -1:
            nueva_cadena +=  x*n
        else:
            nueva_cadena += x
    print(f"'{nueva_cadena}'")

nuevo_string('Charleston',2)
nuevo_string('RDT11',1)
nuevo_string('H2O',3)

# EJERCICIO 4 con strings, Notas de pie de página------------------------------------

def notas_al_pie(s):
    subcaracter = '*'
    nueva_nota = ""
    n = 0
    for c in s:
        indice = subcaracter.find(c)
        if indice != -1:
            n += 1
            nueva_nota +=  "(" + str(n) + ")"
        else:
            nueva_nota += c
    print(f"'{nueva_nota}'")

notas_al_pie('Esta es la primera nota*; y esta la segunda*.')
notas_al_pie('Esta frase no tiene notas. Esta otra tampoco.')
notas_al_pie('*,*. *.')
notas_al_pie('*')
notas_al_pie('')

# EJERCICIO 5 con strings, Calcula código a partir de un nombre ingresado con letras del alfabeto----------------------------------------------

def codigo(s):
    separador = " "
    name_list = s.split(separador) # la cadena de texto se convierte a lista
    slist =[]
    string = s.replace(' ','') # se eliminó los espacios de la cadena s
    nletras = len(string)       # calcula la longitud o numero de caracteres de la cadena
    if string.isalpha(): # evalua si el nombre está compuesto solo con letras del alfabeto
        for c in name_list:
            ini = c[0].upper() # convertira en mayusculas el primer caracter en caso se ingrese con minuscula
            slist.append(ini) # se adiciona en una lista las iniciales de cada palabra
        new_string ="".join(slist) + str(nletras) # convierte en cadena la lista de las iniciales
    else:
        new_string = ""
    print(f"'{new_string}'")

codigo('Mireia Belmonte Garcia')
codigo('Bruce Frederick Joseph Springsteen')
codigo('')
codigo('Gerard Piqué Bernabéu')
codigo('Sergio Ramos García')

# EJERCICIO 6 con strings, Contador de hidrógenos---------------------------------------------------

def contar_hidrogenos(s):

    indice = s.find("H") # busca el indice de la H en la cadena
    if indice >= 0: #valida si existe H en la cadena, si este es -1 quiere decir que no encontro H
        try:
            int(s[indice+1:indice+2]) #valida si es numero entero el caracter delante de la H
            nhidrogenos = s[indice+1:indice+2] # extrae el digito entero delante de la H
        except ValueError:
            nhidrogenos = 1 # asigna valor de 1 cuando no hay digito entero mayor de uno delante de H
    else:
        nhidrogenos = 0 # asigna 0 cuando no existe H en la cadena
    print(nhidrogenos)

contar_hidrogenos('HIO')
contar_hidrogenos('H2O')
contar_hidrogenos('C2H5O')
contar_hidrogenos('Fe3O4')
contar_hidrogenos('C2OH')

#--------------------------------EJERCICIOS CON LISTAS-----------------------------------------------
#EJERCICIO 7 VALOR MEDIO DE TEMPERATURAS DE UNA LISTA
def mediaTempRang(lst):
    new_lst =[]
    for n in lst:
        if  15 <= n <= 45:
            new_lst.append(n)
    if len(new_lst) > 0:
        mean = round(sum(new_lst)/len(new_lst),2)
    else:
        mean = -1
    print(mean)

lst1 = [34.5, 12.9, 15, 43, 51.4, 23.4]
lst2 = [45.5, 12.9, 15, 32.5, 51.4, 21.2]
lst3 = [14.5, 12.6, 47.8]
lst4 = [15, 16, 14, 50, 17]

mediaTempRang(lst1)
mediaTempRang(lst2)
mediaTempRang(lst3)
mediaTempRang(lst4)

#EJERCICIO 8 detectar la segunda N de la presion del sonido-----------------------------------------

def detect2ndNdB(lst, N):
    from math import log10
  
    def SPL_dB(P):
        SPL_NdB = []
        for n in P:
            NdB = round(20*log10(n/20),2)
            SPL_NdB.append(NdB)
        return SPL_NdB

    SPL_NdB = SPL_dB(lst)
    lst_NdB = []

    for n in SPL_NdB:
        if n >= N:
            lst_NdB.append(n)

    if len(lst_NdB)>=2:
        Seg_NdB = lst_NdB[1]
        indice = SPL_NdB.index(Seg_NdB)
        Seg_P = lst[indice]
    else:
        Seg_P = -1
        # indice = -1

    print(Seg_P)

detect2ndNdB([90, 590, 750, 632, 650, 900, 2000, 789, 545], 30)
detect2ndNdB([90, 590, 750, 632, 650, 900, 2000, 789, 545], 33)
detect2ndNdB([90, 590, 750, 632, 630, 600, 200, 589, 545], 30)
detect2ndNdB([9e3, 1e4, 1.1e5, 2.2e5, 1.3e6, 2.5e6, 3.2e6], 83)
detect2ndNdB([2000, 2450.5, 2500 , 456.7, 1567.8], 42)

#EJERCICIO 9 PRIMOS PITAGORICOS------------------------------------------
def primoPitagoric2(lst):
    
    def es_primo(n):
        if n <= 1: return False
        for d in range(2, n//2+1):
            if n % d == 0: return False  
        return True 
    
    lst_primos = []
    for i in lst:
        if es_primo(i) == True: lst_primos.append(i)
    lst_primos = list(set(lst_primos))    
    

    lst_pitagoric = []
    if len(lst_primos) > 0:
        for p in lst_primos:
            if p % 4 == 1: lst_pitagoric.append(p)

    if len(lst_pitagoric) >= 2:    
        lst_pitagoric.sort()
        Lp = lst_pitagoric[0:2]
    else:
        Lp = -1
    return Lp


print(primoPitagoric2([3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13]))
print(primoPitagoric2([5, 9, 13, 17, 21, 25, 29, 33, 37, 41]))
print(primoPitagoric2([41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81]))
print(primoPitagoric2([3, 4, 5, 6, 7, 8, 9, 10]))
print(primoPitagoric2([81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121]))

#-------------------EJERCICIOS DE LISTAS DE LISTAS ---------------------------

#--EJERCICIO 10 PRIMOS  CONTAR EL NUMERO DE POSITIVOS 

def contar_pos(m):
    pos =[]
    for j in m:
        if len(j)>0:
            for x in j:
                if x>0: pos.append(x)
    print(len(pos))

contar_pos([[1, -2, 3],[-4,5,6],[7,8,-9]])

#---EJERCICIO 11 PRIMOS MAYOR DENSIDAD--------------------------------------------------------------

def mas_denso(Lst):
    try:
        denso =[]
        for j in Lst:
                d = j[1]/j[2]
                denso.append(d)
        Mx_d = max(denso)
        i = denso.index(Mx_d)
        Planeta = Lst[i][0]
    except:
        Planeta = "Ingrese Correctamente"
    print(Planeta)

mas_denso([['Marte', 1, 2],['Tierra',2,3],['Venus',1,3]])
mas_denso([['Marte', 1, 2],['Niviru',2,3],['Venus',1,3],['Tierra',2,2.5]])
mas_denso([['Marte', 1, 2],['Niviru',2,3]])
mas_denso([['Marte', 1, 2]])
mas_denso([['marte']])
mas_denso([[]])
mas_denso([])

#---EJERCICIO 12 PRIMOS  FUTBOL----------------------------

def jugComKm(equipo, x):
        filtro =[]
        for j in equipo:
            if len(j[4:]) != 0:
                d = round(sum(j[4:])/len(j[4:]),2)
            else:
                d = 0
            if  d > x and j[2] == True:
                filtro.append(j[1])
        print(sorted(filtro))
    
lst_equipo = [[3, 'Pique', True, 33, 10.2, 9.0], \
              [4, 'Ramos', True, 34, 11.0, 11.1, 9.8, 8.5], \
              [6, 'Koke', True, 27, 7.5, 9.6, 10.3, 6.5, 5.6], \
              [7, 'Joao',  True, 25, 10.5, 8.4, 9.0, 8.6], \
              [8, 'Saul', True, 24, 9.5, 8.9, 10.0, 9.6], \
              [9, 'Suarez', False, 33, 8.6, 7.5], \
              [10, 'Lionel', False, 33, 10.0, 11.1, 9.8, 8.5,10.1], \
              [19, 'Odriozola', True, 25, 9.5], \
              [14, 'Araujo', False, 21, 8.9, 9.5], \
              [15, 'Valverde', False, 22, 9.9, 10.2], \
              [16, 'Pedri', True, 18, 10.5, 11, 9.5, 10.6], \
              [22, 'Hermoso', False, 23, 10, 7.5, 6.6], \
              [23, 'Iago', True, 33, 11.1, 9.0, 9.3, 8.8], \
              [24, 'Juank', True, 43], \
              [25,]]

jugComKm(lst_equipo, 10)
jugComKm(lst_equipo, 10.2)
jugComKm(lst_equipo, 10.5)
jugComKm(lst_equipo, 9.5)
jugComKm(lst_equipo, 9.4)


  
