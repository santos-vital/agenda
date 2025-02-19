def adicionar_contato(contatos, nome, telefone, email):
  contato = {
    "nome": nome, 
    "telefone": telefone, 
    "email": email,
    "favorito": False
  }

  contatos.append(contato)
  print(f"Contato {nome} adicionado com sucesso!")

  return

def visualizar_contatos(contatos):
  print("\nLista de contatos")
  for indice, contato in enumerate(contatos, start=1):
    favorito = contato["favorito"]
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    print(f"{indice}. {'★' if favorito else '☆'} {nome}")
    print(f"   📞 Telefone: {telefone}")
    print(f"   📧 E-mail: {email}")
    print("-" * 30)

def editar_contato(contatos):
  if not contatos:
    print("📌 A lista de contatos está vazia.")
    return

  nome_busca = input("🔍 Digite o nome do contato que deseja editar: ").strip()

  for contato in contatos:
    if contato["nome"].lower() == nome_busca.lower():
      print(f"\n✏️ Editando contato: {contato['nome']}")
            
      novo_nome = input(f"Novo nome ({contato['nome']}): ").strip() or contato['nome']
      novo_telefone = input(f"Novo telefone ({contato['telefone']}): ").strip() or contato['telefone']
      novo_email = input(f"Novo e-mail ({contato['email']}): ").strip() or contato['email']

      contato["nome"] = novo_nome
      contato["telefone"] = novo_telefone
      contato["email"] = novo_email

      print("✅ Contato atualizado com sucesso!\n")
      return
  print("⚠️ Contato não encontrado!")

contatos = []

while True:
  print("\nAgenda - Menu\n")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Marcar/desmarcar contato como favorito")
  print("5. Visualizar favoritos")
  print("6. Deletar contato")
  print("7. Sair\n")

  opcao = input("Selecione a operação desejada: ")

  if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    adicionar_contato(contatos, nome, telefone, email)
  elif opcao == "2":
    visualizar_contatos(contatos)
  elif opcao == "3":
    editar_contato(contatos)
  elif opcao == "7":
    break
  else:
    print("Opção inválida! Escolha novamente uma opção de 1 a 7:")
print("\nPrograma finalizado!")