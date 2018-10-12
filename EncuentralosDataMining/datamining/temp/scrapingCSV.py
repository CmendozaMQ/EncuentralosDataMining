#pyhton system evaluation proyect
#intervalos difusos
nadav=[0.00, 0.00, 1.20, 2.20]
pocov=[1.20,2.20,3.40,4.4] 
regularv=[3.40,4.40,5.60,6.60] 
muchov=[5.60,6.60,7.80,8.80]
todov=[7.80,8.80,10.00,10.00] 
#==============================================================================
# importacion liberias panda
#==============================================================================
import pandas as pd
import numpy as np

dataset = pd.read_csv('../../../EncuentralosDataMining/155727921303318_facebook_statuses.csv')
#==============================================================================
# matrices 
#==============================================================================
X = dataset.iloc[:, :-9].values
#Y = dataset.iloc[:, :-1].values
#PU = dataset.iloc[:,+1:].values
#SumaPAE=[]
##sumatorias
#SPU=[]
#MPU=[]

#==============================================================================
# funcino de division
#==============================================================================
#def divisionPesoUmbral(ps,um):
#    totalPsUm=0
#    totalPsUm = ps/um    
#    totalPsUm = round(totalPsUm, 3)            
#    return totalPsUm 
#==============================================================================
# funcion de multiplicacion
#==============================================================================
#def multiplicacionPesoUmbral(ps,um):
#    totalPsUm=0
#    totalPsUm = ps*um    
#    totalPsUm = round(totalPsUm, 3)            
#    return totalPsUm

#==============================================================================
# 
#==============================================================================
#def multiPesoUmbral(idx):    
#    MPU=[]
#    Pf=Pf1=0    
#    for k in X:
#        total=0
#        if k[2]=='todo' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in todov:
#                Pf1=float(l)
#                total=multiplicacionPesoUmbral(Pf,Pf1)                
#                MPU.append(total)
#            MPU.append('/n')
#        if k[2]=='mucho' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in muchov:
#                Pf1=float(l)
#                total=multiplicacionPesoUmbral(Pf,Pf1)                
#                MPU.append(total)
#            MPU.append('/n')
#        if k[2]=='regular' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in regularv:
#                Pf1=float(l)
#                total=multiplicacionPesoUmbral(Pf,Pf1)                
#                MPU.append(total)
#            MPU.append('/n')
#        if k[2]=='poco' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in pocov:
#                Pf1=float(l)
#                total=multiplicacionPesoUmbral(Pf,Pf1)                
#                MPU.append(total)
#            MPU.append('/n')
#        if k[2]=='nada' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in nadav:
#                Pf1=float(l)
#                total=multiplicacionPesoUmbral(Pf,Pf1)                
#                MPU.append(total)
#            MPU.append('/n')
#    return MPU
#
#def divPesoUmbral(idx):
#    SPU=[]    
#    Pf=Pf1=0    
#    for k in X:
#        total=0
#        if k[2]=='todo' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in todov:
#                Pf1=float(l)
#                total=divisionPesoUmbral(Pf,Pf1)                
#                SPU.append(total)
#            SPU.append('/n')
#        if k[2]=='mucho' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in muchov:
#                Pf1=float(l)
#                total=divisionPesoUmbral(Pf,Pf1)                
#                SPU.append(total)
#            SPU.append('/n')
#        if k[2]=='regular' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in regularv:
#                Pf1=float(l)
#                total=divisionPesoUmbral(Pf,Pf1)                
#                SPU.append(total)
#            SPU.append('/n')
#        if k[2]=='poco' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in pocov:
#                Pf1=float(l)
#                total=divisionPesoUmbral(Pf,Pf1)                
#                SPU.append(total)
#            SPU.append('/n')
#        if k[2]=='nada' and k[0]==idx:
#            Pf=float(k[1])
#            #print("PU",Pf)            
#            for l in nadav:
#                Pf1=float(l)
#                total=divisionPesoUmbral(Pf,Pf1)                
#                SPU.append(total)
#            SPU.append('/n')
#    return SPU
#==============================================================================
# 
#==============================================================================
      

if __name__ == '__main__':
    M4=['','','','','','','','']
    M4T=[]
#    m4c=0
    for m in X:        
       print(np.asarray(m))
#        if m!='/n':
#            M4[m4c]=m
#            m4c=m4c+1
#        else:    
#            M4T.append([X[0],X[1],X[2],X[3],X[4],X[5],X[6],X[7]])
#            m4c=0
    #print(M4T)
    a = np.asarray(m)
#    np.savetxt('pesoUmbral_P.csv', a, delimiter=',')

#def mulMatrix(MMP):
#    M4=['','','','']
#    M4T=[]
#    m4c=0
#    for m in MMP:
#        if m!='/n':
#            M4[m4c]=m
#            m4c=m4c+1
#        else:    
#            M4T.append([M4[0],M4[1],M4[2],M4[3]])
#            m4c=0
#    #print(M4T)
#    a = np.asarray(M4T)
#    np.savetxt("pesoUmbral_M.csv", a,fmt='%.3f', delimiter=",", header="#H1,#H2,#H3,#H4")
#


#
#sumaPL=0
#sumaAD=0
#sumaEX=0
#for i in Y:
#    if i[0]=='P':
#        inumber=int(i[1])
#        sumaPL=sumaPL+inumber
#    if i[0]=='A':
#        inumber=int(i[1])
#        sumaAD=sumaAD+inumber
#    if i[0]=='E':
#        inumber=int(i[1])
#        sumaEX=sumaEX+inumber        
# #   print("Suma Plausibilidad:",sumaPL)
# #   print("Suma Adecuación :",sumaAD)
# #   print("Suma Éxito :",sumaEX)
##==============================================================================
##Plausibilidad      
##==============================================================================
#suma_P=divPesoUmbral('P')
#multi_P=multiPesoUmbral('P')
#
#divMatrix(suma_P)
#mulMatrix(multi_P)
#
#dataset_PP = pd.read_csv("pesoUmbral_P.csv").sum()
#dataset_MP = pd.read_csv("pesoUmbral_M.csv").sum()
#dataset_PP = (dataset_PP.pow(-1).mul(sumaPL)).mul(0.5)
#dataset_MP = dataset_MP.mul(1/sumaPL).mul(0.5)
#
#dataset_sum_P =dataset_MP.add(dataset_PP, fill_value=0)
#dataset_sum_P = dataset_sum_P.sum()
#data_P=int((dataset_sum_P* 100) + 0.5) / 100.0
#data_P=data_P/4
#
##print(dataset_PP)
##print(dataset_MP)
#print("Plausibilidad:",data_P)
##==============================================================================
## Adecuación 
##==============================================================================
#suma_A=divPesoUmbral('A')
#multi_A=multiPesoUmbral('A')
#
#divMatrix(suma_A)
#mulMatrix(multi_A)
#
#dataset_PA = pd.read_csv("pesoUmbral_P.csv").sum()
#dataset_MA = pd.read_csv("pesoUmbral_M.csv").sum()
#dataset_PA = (dataset_PA.pow(-1).mul(sumaAD)).mul(0.5)
#dataset_MA = dataset_MA.mul(1/sumaAD).mul(0.5)
#
#dataset_sum_A =dataset_MA.add(dataset_PA, fill_value=0)
#dataset_sum_A = dataset_sum_A.sum()
#data_A=int((dataset_sum_A* 100) + 0.5) / 100.0
#data_A=data_A/4
#
##print(dataset_PA)
##print(dataset_MA)
#print("Adecuacion:",data_A)    
##==============================================================================
##Éxito
##==============================================================================
#suma_E=divPesoUmbral('E')
#multi_E=multiPesoUmbral('E')
#
#divMatrix(suma_E)
#mulMatrix(multi_E)
#
#dataset_PE = pd.read_csv("pesoUmbral_P.csv").sum()
#dataset_ME = pd.read_csv("pesoUmbral_M.csv").sum()
#dataset_PE = (dataset_PE.pow(-1).mul(sumaEX)).mul(0.5)
#dataset_ME = dataset_ME.mul(1/sumaEX).mul(0.5)
#
#dataset_sum_E =dataset_ME.add(dataset_PE, fill_value=0)
#dataset_sum_E = dataset_sum_E.sum()
#data_E=int((dataset_sum_E* 100) + 0.5) / 100.0
#data_E=data_E/4
#
##print(dataset_PE)
##print(dataset_ME)
#print("Exito:",data_E)
#
##==============================================================================
## formula 3
##==============================================================================
#EV=(8*data_P+8*data_A+6*data_E)/22
#EV=float("{0:.2f}".format(EV))
#print("------------------------------------------------------")
#print("Valor global de la viabilidad del proyecto:",EV)
#print("------------------------------------------------------") 
#if EV >= 5.0:    
#    print("Se considera que el proyecto es viable para ser realizado.")
#else:
#    print("Se considera que el proyecto NO es viable para ser realizado.")
