def calcular_rendimento(valor, rendimento_mensal, aporte, períodos):
  
  i = rendimento_mensal / 100
  vf = valor * (1+i) ** períodos
  
  for u in range(períodos): 
    vf = valor + aporte * (1+i) ** (1+u) 
    valor = vf 
    
    print(f"\t Após {u+1} mês(es), o valor será de: R$ {valor:,.2f}.")

valor= float(input("Informe o valor inicial: R$"))
rendimento_mensal = float(input("Informe o rendimento por período (%): "))
aporte = float(input("Informe o aporte a cada período: R$"))
períodos = int(input("Total de períodos: "))

calcular_rendimento(valor, rendimento_mensal, aporte, períodos)