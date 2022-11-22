print("\33[1;44;30m          INSS          \33[m")
print("Bem vindo ao sistema da previdência social")
nome = input("Digite seu nome:")
print("Olá, senhor(a)", nome," bem vindo ao sistema da previdência social.")
print("Precisamos checar alguma informações. Por gentileza insira as informações abaixo:")
anonasc = int(input("Ano de nascimento:"))
anoatual = int(input("Ano atual:"))
tempocontr = int(input("Tempo de contribuição:"))
contrnecess = 35 #Tempo de contribuição necessário para aposentadoria atualmente
idadeness = 65 #Idade mínima (para homens) para  aposentadoria atualmente
contrrest= contrnecess - tempocontr #Cálculo de quantos anos de contribuição faltam para aposentadoria
idade = anoatual - anonasc #Cálculo da idade do usuário para amostragem posterior
idaderest = idadeness - (idade)
if idade <= 65:
    print("Verifiquei que a sua idade é de ", idade, "anos e seu tempo de contribuição é", tempocontr, ". O senhor ainda não é elegível para a aposentadoria por Idade/Tempo de serviço.")
    print("O senhor possui alguma deficiência comprovada por laudo médico que o imcapacite ao trabalho?")
    opcao = input("1- Sim 2-Não")
    if opcao == "1":
        print("Gentileza fazer upload do arquivo contendo o laudo, documento oficial com foto e conta bancária a ser depositado o benefício em caso de aprovação")
    elif opcao == "2":
        print("Lamentamos, faltam", contrrest, "anos de contribuição ou ", idaderest," anos de vida para ser elegível à aposentadoria por Idade/Tempo de serviço.")
print("Obrigado por utilizar o nosso sistema. Volte sempre") 