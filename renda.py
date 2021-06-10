def diagnosticar_renda(educacao, moradia, transporte):
    educacao_aceitavel = renda_mensal / 3
    moradia_aceitavel = renda_mensal / 5
    transporte_aceitavel = renda_mensal / 6
       
    if educacao < educacao_aceitavel:
        print("Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R${educacao_aceitavel}. ")
    
    if moradia < moradia_aceitavel:
        print("Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${moradia_aceitavel}. ")    
    
    if transporte < transporte_aceitavel:
        print("Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R${transporte_aceitavel}. ")   
        
renda_mensal = float(input("Informe a renda mensal: R$"))
educacao = float(input("Informe o gasto mensal com a educação: R$"))
moradia = float(input("Informe o gasto mensal com a moradia: R$"))
transporte = float(input("Informe o gasto mensal com a transporte: R$"))

diagnosticar_renda(educacao, moradia, transporte)