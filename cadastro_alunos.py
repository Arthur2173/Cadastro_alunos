import json
import os


class GerenciadorArquivos:
    def __init__(self, arquivo="alunos.json"):
        self.arquivo = arquivo

    def salvar(self, lista_alunos):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(lista_alunos, f, indent=4, ensure_ascii=False)

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        return []


class GerenciadorAlunos:
    def __init__(self):
        self.arquivos = GerenciadorArquivos()
        self.lista_alunos = self.arquivos.carregar()

    def cadastrar_aluno(self):
        nome = input("Informe o nome do aluno: ")
        nota = int(input("Informe a nota do aluno: "))
        aluno = {"nome": nome, "nota": nota}
        self.lista_alunos.append(aluno)
        self.arquivos.salvar(self.lista_alunos)
        print("Aluno cadastrado com sucesso!")

    def listar_alunos(self):
        if not self.lista_alunos:
            print("Nenhum aluno cadastrado.")
            return
        for dado in self.lista_alunos:
            print(f"Nome: {dado['nome']}, Nota: {dado['nota']}")

    def buscar_aluno(self):
        nome_busca = input("Informe o nome do aluno que deseja buscar: ")
        for dado in self.lista_alunos:
            if dado["nome"] == nome_busca:
                print(f"Nome: {dado['nome']}, Nota: {dado['nota']}")
                return
        print("Aluno não encontrado.")

    def calcular_media(self):
        if not self.lista_alunos:
            print("Nenhum aluno cadastrado para calcular média.")
            return 0
        soma = sum(c["nota"] for c in self.lista_alunos)
        media = soma / len(self.lista_alunos)
        print(f"Média da turma: {media:.2f}")
        return media

    def atualizar_nota(self):
        nome = input("Informe o nome do aluno que deseja atualizar: ")
        for c in self.lista_alunos:
            if c["nome"] == nome:
                nova_nota = int(input("Informe a nova nota: "))
                c["nota"] = nova_nota
                self.arquivos.salvar(self.lista_alunos)
                print(f"Nota atualizada! Nome: {c['nome']}, Nova Nota: {c['nota']}")
                return
        print("Aluno não encontrado.")

    def remover_aluno(self):
        nome = input("Informe o nome do aluno que deseja remover: ")
        for c in self.lista_alunos:
            if c["nome"] == nome:
                self.lista_alunos.remove(c)
                self.arquivos.salvar(self.lista_alunos)
                print("Aluno removido com sucesso!")
                return
        print("Aluno não encontrado.")
