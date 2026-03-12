import random

#entrada 
data_compra = input('Digite a data da compra d\m\aaa: ')
meses = int(input('Prazo de garantia: '))


data_inicial = datetime.datetime.strptim(data_compra, %d/%m/Y')
data_final = data_inicial + datetime.timedelta(days=meses *30)

print(f"Garantia válida até {data_final.strptime('%d/%m/%Y ')}')
print(f"Dia da Semana: {data_final.strftime('%A)}')
                                          