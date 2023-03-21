#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main(): 
    print("Conversor Minuto para Hora")
    conversor = conversor_hora()
    
   
    
def conversor_hora():
    tempo = int(input("Digite a quantidade de minutos que voce quer converter para horas: \n"))
    tempo = tempo
    hora = (tempo / 60)
    if hora < 1:
        hora = 0
    else:
        hora = round(hora)    
    minuto = tempo % 60
    print(f"{tempo} minutos equivale a {hora} horas e {minuto} minutos.")



if __name__ == "__main__":
    main()
        


# In[ ]:




