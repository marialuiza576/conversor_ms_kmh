def conversor() :
    try :
     vel_ms= float(input('DIGITE O VALOR EM m/s:'))
     vel_kmh= vel_ms * 3.6
     print(f'A VELOCIDADE INSERIDA É IGUAL A:{vel_kmh}Km/h')
    except ValueError:
        print('VALOR INVÁLIDO, DIGITE UM NÚMERO VÁLIDO')

print('BEM VINDO AO CONVERSOR DE VELOCIDADE!!!')


while True:
     conversor() 
     parar= input('PARA PARAR O PROGRAMA DIGITE "S" PARA CONTINUAR DIGITE QUALQUER OUTRA TECLA: ').lower()
     if parar == "S":
          print('PROGRAMA ENCERRADO')
          break 
     else:
          continue