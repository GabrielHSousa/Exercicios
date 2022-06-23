import this
import ExercicioModel

this.opcao = -1

def menu():
    print('Menu\n\n'+
          '\n1. Exercicios 01' +
          '\n2. Exercicios 02' +
          '\n3. Exercicios 03' +
          '\n4. Exercicios 04' +
          '\n5. Exercicios 05' +
          '\n6. Exercicios 06' +
          '\n7. Exercicios 07' +
          '\n8. Exercicios 08' +
          '\n9. Exercicios 09' +
          '\n10. Exercicios 10' +
          '\n11. Exercicios 11' +
          '\n12. Exercicios 12' +
          '\n13. Exercicios 13' +
          '\n14. Exercicios 14' +
          '\n15. Exercicios 15' +
          '\n16. Exercicios 16' +
          '\n17. Exercicios 17' +
          '\n18. Exercicios 18' +
          '\n19. Exercicios 19' +
          '\n20. Exercicios 20' +
          '\n0. Sair'           +
          '\nEscolha uma das opções acima:')
    this.opcao = int(input())

def execultar():
    while(this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('obrigado!')
        elif this.opcao == 1:
            print(ExercicioModel.exercicio01())
        elif this.opcao == 2:
            print(ExercicioModel.exercicio02())
        elif this.opcao == 3:
            print(ExercicioModel.exercicio03())
        elif this.opcao == 4:
            print(ExercicioModel.exercicio04())
        elif this.opcao == 5:
            print(ExercicioModel.exercicio05())
        elif this.opcao == 6:
            print(ExercicioModel.exercicio06())
        elif this.opcao == 7:
            print(ExercicioModel.exercicio07())
        elif this.opcao == 8:
            print(ExercicioModel.exercicio08())
        elif this.opcao == 9:
            print(ExercicioModel.exercicio09())
        elif this.opcao == 10:
            print(ExercicioModel.exercicio10())
        elif this.opcao == 11:
            print(ExercicioModel.exercicio11())
        elif this.opcao == 12:
            print(ExercicioModel.exercicio12())
        elif this.opcao == 13:
            print(ExercicioModel.exercicio13())
        elif this.opcao == 14:
            print(ExercicioModel.exercicio14())
        elif this.opcao == 15:
            print(ExercicioModel.exercicio15())
        elif this.opcao == 16:
            print(ExercicioModel.exercicio16())
        elif this.opcao == 17:
            print(ExercicioModel.exercicio17())
        elif this.opcao == 18:
            print(ExercicioModel.exercicio18())
        elif this.opcao == 19:
            print(ExercicioModel.exercicio19())
        elif this.opcao == 20:
            print(ExercicioModel.exercicio20())
        else:
            print('Opção informada não é valida!')
