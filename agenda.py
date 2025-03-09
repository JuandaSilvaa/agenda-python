def adicionar_contato(nome_contato, telefone_contato="", email_contato=""):
  contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato, "favoritado": False}
  contatos.append(contato)

def ver_contatos(contatos):
  print("\nContatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "♡" if contato["favoritado"] else ""
    nome_contato = contato["contato"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"""{indice}. [{status}] {nome_contato}
      •Telefone: {telefone_contato}
      •Email: {email_contato}""")

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
  indice_contato_ajustato = int(indice_contato) - 1
  if indice_contato_ajustato >= 0 and indice_contato_ajustato < len(contatos):
    if novo_nome_contato != "":
      contatos[indice_contato_ajustato]["contato"] = novo_nome_contato
    if novo_telefone_contato != "":
      contatos[indice_contato_ajustato]["telefone"] = novo_telefone_contato
    if novo_email_contato != "":
      contatos[indice_contato_ajustato]["email"] = novo_email_contato
  else:
    print ("Índice de contato inválido")

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustato = int(indice_contato) - 1
  contatos[indice_contato_ajustato]["favoritado"] = True
  print(f"Contato {indice_contato} marcado como favorito")
  return

def ver_contatos_favoritados(contatos):
  print("\nContatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "♡" if contato["favoritado"] else ""
    nome_contato = contato["contato"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    if contato["favoritado"]:
      print(f"""{indice}. [{status}] {nome_contato}
        •Telefone: {telefone_contato}
        •Email: {email_contato}""")

def desfavoritar_contato(contatos, indice_contato):
  indice_contato_ajustato = int(indice_contato) - 1
  contatos[indice_contato_ajustato]["favoritado"] = False
  print(f"Contato {indice_contato} marcado como favorito")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustato = int(indice_contato) - 1
  contatos.remove(contatos[indice_contato_ajustato])
  print(f"Contato {indice_contato} removido")
  return

contatos = []
while True:
  print("\nMenu da Agenda de Contatos")
  print("1. Adicionar novo contato")
  print("2. Visualizar contatos")
  print("3. Atualizar um contato")
  print("4. Favoritar contato")
  print("5. Desfavoritar contato")
  print("6. Visualizar contatos favoritos")
  print("7. Deletar contato")
  print("8. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone_contato = input("Digite o número de telefone caso tenha: ")
    email_contato = input("Digite o Email caso tenha: ")
    adicionar_contato(nome_contato=nome_contato, telefone_contato=telefone_contato, email_contato=email_contato)
  if escolha == "2":
    ver_contatos(contatos)
  if escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que deseja atualizar: ")
    novo_nome_contato = input("Digite o novo nome do contato caso tenha: ")
    novo_telefone_contato = input("Digite o novo número do contato caso tenha: ")
    novo_email_contato = input("Digite o novo email do contato caso tenha: ")
    atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)
  if escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)
  if escolha == "5":
    ver_contatos_favoritados(contatos)
    indice_contato = input("Digite o numero do contato que deseja desfavoritar: ")
    desfavoritar_contato(contatos, indice_contato)
  if escolha == "6":
    ver_contatos_favoritados(contatos)
  if escolha == "7":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que deseja remover: ")
    deletar_contato(contatos, indice_contato)
  elif escolha == "8":
    break
print("Programa finalizado")
