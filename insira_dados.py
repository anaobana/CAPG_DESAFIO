#CADASTRO DE ANÚNCIOS
import os

base_geral=[]


def insira_dados():

  print ("Insira aqui os dados do seu anúncio:\n")
  nome = input ("Nome do anúncio: ")
  cliente = input ("Nome do cliente: ")
  inicio = input ("Data de início: ")
  termino = input ("Data de término: ")
  investimento_diario = int(input ("Investimento por dia: "))

  base=[nome,cliente,inicio,termino,investimento_diario]
  base_geral.append(base)
  os.system('cls' if os.name == 'nt' else 'clear')
  insira_dados()
  

insira_dados()


