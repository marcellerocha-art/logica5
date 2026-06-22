"""
DATA MANAGER - Ler/Salvar dados em arquivo
Formatos: .txt, .csv, .json
"""

import json, csv
from pathlib import Path

class Dados:
    def __init__(self):
        self.lista = []
    
    def validar_nome(self, nome):
        return len(nome.strip()) > 0 and nome.replace(" ", "").isalpha()
    
    def validar_idade(self, idade):
        try:
            return 1 <= int(idade) <= 150
        except:
            return False
    
    def adicionar(self):
        nome = input("Nome: ")
        while not self.validar_nome(nome):
            nome = input("Nome inválido. Tente: ")
        
        sobrenome = input("Sobrenome: ")
        while not self.validar_nome(sobrenome):
            sobrenome = input("Sobrenome inválido. Tente: ")
        
        idade = input("Idade: ")
        while not self.validar_idade(idade):
            idade = input("Idade inválida. Tente: ")
        
        self.lista.append({"nome": nome, "sobrenome": sobrenome, "idade": int(idade)})
        print("✅ Adicionado!")
    
    def ler(self, arquivo):
        ext = Path(arquivo).suffix.lower()
        try:
            self.lista = []
            if ext == '.txt':
                with open(arquivo, encoding='utf-8') as f:
                    for linha in f:
                        n, s, i = linha.strip().split(',')
                        self.lista.append({"nome": n, "sobrenome": s, "idade": int(i)})
            elif ext == '.csv':
                with open(arquivo, encoding='utf-8') as f:
                    for row in csv.DictReader(f):
                        self.lista.append(row)
            elif ext == '.json':
                with open(arquivo, encoding='utf-8') as f:
                    self.lista = json.load(f)
            print(f"✅ {len(self.lista)} registros")
        except:
            print("❌ Erro")
    
    def salvar(self, arquivo):
        if not self.lista:
            print("❌ Sem dados")
            return
        
        ext = Path(arquivo).suffix.lower()
        try:
            if ext == '.txt':
                with open(arquivo, 'w', encoding='utf-8') as f:
                    for p in self.lista:
                        f.write(f"{p['nome']},{p['sobrenome']},{p['idade']}\n")
            elif ext == '.csv':
                with open(arquivo, 'w', encoding='utf-8', newline='') as f:
                    csv.DictWriter(f, ['nome', 'sobrenome', 'idade']).writeheader()
                    csv.DictWriter(f, ['nome', 'sobrenome', 'idade']).writerows(self.lista)
            elif ext == '.json':
                with open(arquivo, 'w', encoding='utf-8') as f:
                    json.dump(self.lista, f, ensure_ascii=False)
            print("✅ Salvo!")
        except:
            print("❌ Erro")
    
    def ver(self):
        if not self.lista:
            print("⚠️  Vazio")
            return
        for p in self.lista:
            print(f"{p['nome']} {p['sobrenome']} - {p['idade']}")

d = Dados()
while True:
    print("\n1.Ler 2.Salvar 3.Adicionar 4.Ver 5.Sair")
    if input(">>> ") == "1":
        d.ler(input("Arquivo: "))
    elif _ == "2":
        d.salvar(input("Arquivo: "))
    elif _ == "3":
        d.adicionar()
    elif _ == "4":
        d.ver()
    elif _ == "5":
        break