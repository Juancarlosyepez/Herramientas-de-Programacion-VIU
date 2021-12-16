# *************************DICCIONARIOS**************************************************
# **************FRECUENCIA DE PARES*****************************
import pandas as pd

M = [12, 19, 19, 18, 18, 16, 18, 13, 19, 18, 12, 18, 11, 20, 14, 14, 20, 20, 20, 16, 13, 15, 19, 14, 12]

def dpar(M):
    frecuencia = {}
    Mpares = []
    for numero in M:
        if len(M) > 0 and numero % 2 == 0: # filtra los numeros pares
            Mpares.append(numero)
    for n in Mpares:
        frecuencia.setdefault(n, 0) # Agrega el numero par con valor cero si es que no existe de lo contrario no lo agrega
        frecuencia[n] += 1 # Incrementa en 1 al valor agragado
    print(frecuencia)


dpar(M)
#
# # *********************TEMPERATURAS CIUDADES**************************************************
lst_ciudades = [['Londres', 3.4, 6.3, 10.5, 6.8], ['Oslo', -3.8, -5.0, 5.1, 4.2], ['Berlin', 7.5, 4.1, 12.3, 13.0],
                ['Malaga', 14.7, 12.3, 19.5, 18.4]]
def TempMaxMin(lst):
    lst_temp = []
    lst_ciudad = []
    lst.sort()
    for temp in lst:
        lst_ciudad.append(temp[0]) # extraemos las ciudades en una nueva lista
        lst_temp.append([max(temp[1:]), min(temp[1:])]) #extrameos las temperaturas max y min en nueva lista
    d = dict(zip(lst_ciudad, lst_temp)) # convertimos un diccionario a partir de dos listas
    print(d)


TempMaxMin(lst_ciudades)


# # ***********************TEMPERATURAS NEVADA*************************************************
#
dCi = {'Manchester': 1.1, 'Madrid': -8.9, 'Gava': 4, 'Pobla de Segur': -5.6, 'Lleida': -3.2, 'Elche': 2.1, 'Burgos': -6.0, 'Sant Boi': 4.5}
dPe = {'Pepe': 'Manchester', 'Lionel': 'Gava', 'Mike': 'Sant Boi', 'Puyol': 'Pobla de Segur', 'Jaime': 'Elche', 'Sergi': 'Lleida' ,'Ernesto': 'Madrid', 'Carlos': 'Burgos'}
#
#
def PersMayTemp(dPersC, dCiudT):
    lPe = []
    for kPe, vPe in dPersC.items(): # descomponemos el diccionario en clave y valor por separado
        if dCiudT.get(vPe) < 0: # verificamos el valor de la temperatura del diccionario dCi que este bajo cero
            lPe.append(kPe) # agregamos el nombre de la persona que corresponde al pais con tem bajo cero
        lPe.sort()
    print(lPe)
#
PersMayTemp(dPe, dCi)
#
# # ******************************04-EJERCICIO: HIPERTENSION*******************************************
dpers = {'Maria': [40, 135, 90], 'Nuria': [63, 141, 92], 'Jose': [47, 110, 59], 'Luis': [49, 146, 94],
         'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], 'Pepe': [70, 130, 92]}

def lst_hiper(dicc, edad):
    lst_nombre = []
    for k, v in dicc.items(): # descomponemos el diccionario en clave y valor por separado
        if (v[1] >= 140 or v[2] >= 90) and v[0] < edad: #verificamos que las condiciones se cumplan
            lst_nombre.append(k) # si cumple la condicion se ingresa el nombre del pasiente en una nueva lista
    lst_nombre.sort() # se ordena los nombres de la lista en orden alfabetico
    print(lst_nombre)
#
#
lst_hiper(dpers, 45)
lst_hiper(dpers, 70)
#
# # ********************************05-EJERCICIO: NIVEL DE POTASIO EN SANGRE******************************
dK1 = {'Luis': 2.2, 'Carlos': 7.0, 'Laia': 4.0, 'Mikel': 5.5, 'Jordi': 5.2, 'Anna': 3.6, 'Joe': 7.2}
ls1 = [2.0, 3.5, 5.2, 7.0]
#
def nivelKsand(dK, lst):
    dicK = {}
    for k, v in dK.items(): # descomponemos el diccionario en clave y valor por separado para evaluar por su valor
        if v < lst[0]:
            dicK.setdefault(k ,"hipokalemia crítica") # insertamos el nombre con el diagnostico del pasiente en el diccionario nuevo, el proceso se repite en todas las condiciones
        elif lst[0] <= v < lst[1]: # se evalua con el primer y segundo valor de la lista, se usara el mismo criterio con los demas valores para las siguientes evaluaciones
            dicK.setdefault(k, "hipokalemia leve")
        elif lst[1] <= v <= lst[2]:
            dicK.setdefault(k, "normal")
        elif lst[2] < v <= lst[3]:
            dicK.setdefault(k, "hipokalemia moderada")
        elif lst[3] < v:
            dicK.setdefault(k, "hipokalemia severa")
        else:
            print("No existe diagnostico")
    print(dicK)

nivelKsand(dK1, ls1)

# DATAFRAMES

#
# # *********************************06-TEMPERATURA CIUDADES EN DATAFRAME******************************
#
df = pd.DataFrame(lst_ciudades, columns=["Ciudad", "Enero", "Febrero", "Marzo", "Abril"])
# # df.head() ------> en jupyter
print(df)

def calculatemp(df):
    df['Min'] = df[["Enero", "Febrero", "Marzo", "Abril"]].min(axis = 1)
    df["Max"] = df[["Enero", "Febrero", "Marzo", "Abril"]].max(axis = 1)
    df["Media"] = df[["Enero", "Febrero", "Marzo", "Abril"]].mean(axis = 1)
    df["StdDev"] = df[["Enero", "Febrero", "Marzo", "Abril"]].std(axis = 1)
    # return df.head() ------> en jupyter
    print(df)

calculatemp(df)
#
# # *********************************07-BASE DE DATOS CARDIACA******************************************************
# # *********************************Mostras las primeras 10 instancias (filas) del DataFrame******************************
#
dfCardio = pd.read_csv("heart.csv")

# dfCardio.head(10) -----------> en jupyter
print(dfCardio)

# # *********************************Calcular el numero (conteo) de hombres y mujeres******************************
#
dfHombres = dfCardio[dfCardio["sex"] == 1] # se crea dfhombres filtrado por sex = 1
dfMujeres = dfCardio[dfCardio["sex"] == 0]# se crea dfMujeres filtrado por sex = 0

# dfHombres.head()-----------> en jupyter
print(dfHombres)

conteo = len(dfHombres.axes[0]) #axes[0] recorre el conteo por filas
print("Numero de Hombres es: ",conteo )

# dfMujeres.head() -------> jupyter

print(dfMujeres)
conteo = len(dfMujeres.axes[0])
print("Numero de Mujeres es: ", conteo )

# # *********************************Calcular el numero (conteo) de casos de anginas******************************
#
dfAngina = dfCardio[dfCardio["exang"] == 1]
# dfAngina.head()---------->en jupyter
print(dfAngina)
conteo = len(dfAngina.axes[0])
print("Numero de casos de Angina es : ",conteo )
#
# # ******************Hallar el DataFrame con la estadistica descriptiva de la frecuencia cardiaca************************

dfDescribe = dfCardio.describe() #calcula la estadistica de todas las columnas del dataframe

df_tha = dfDescribe[['thalach']] # extrameos la columna 'thalach' del dataframe dfDescribe
print(df_tha)

# Hallar un DataFrame que incluya la estadística descriptiva de la presión arterial sistólica en reposo (trestbps)
# y el colesterol (chol). (ambos en el mismo DataFrame)

df_trChol = dfDescribe[['trestbps','chol']] # estramos dos columnas del dataframe dfDescribe
print(df_trChol)


# # *************************08- EJERCICIO: BASE DE DATOS PRESION ARTERIAL EN DATAFRAME**********************************
#
dhiper = {'Maria': [40, 135, 90], 'Nuria': [63, 141, 92], 'Jose': [47, 110, 59], 'Luis': [49, 146, 94],
         'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], 'Pepe': [70, 130, 92]}

lst_data = []
for k, v in dhiper.items(): # descomponemos el diccionario en clave y valor por separado en variables k y v
    if v[1] < 90 or v[2] < 60:
        v.insert(0,k) # insertamos el nombre del paciente en la primera posicion de la lista valor v
        v.append('baja') # insertamos el diagnostico del paciente a la lista valor v
    elif v[1] >= 140 or v[2] >= 90:
        v.insert(0, k)
        v.append('alta')
    else:
        v.insert(0, k)
        v.append(('normal'))
    lst_data.append(v)

dfHiper = pd.DataFrame(lst_data, columns=['Nombre', 'Edad', 'Sistolica', 'Diastolica', 'Diagnostico'])

# dfHiper.head(7)--------> En jupyter
print(dfHiper) #----------> En la tierra

