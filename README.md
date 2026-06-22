# Logica 5 - Aplicação de Leitura e Gravação de Dados

Uma aplicação Python interativa para ler, gravar e gerenciar dados de usuários em múltiplos formatos de arquivo.

## 📋 Descrição

Esta é uma aplicação desenvolvida como atividade prática de programação em Python. O sistema permite que o usuário:

- **Salvar dados** de usuários (nome, sobrenome e idade) em diferentes formatos
- **Ler dados** armazenados de arquivos
- **Navegar** por um menu interativo

### Formatos Suportados
- 📄 `.txt` - Arquivo de texto simples
- 📊 `.csv` - Valores separados por vírgula
- 📑 `.json` - Formato JSON estruturado

## 🚀 Características

- ✅ Menu interativo com 3 opções (Ler, Salvar, Sair)
- ✅ Coleta de dados: Nome, Sobrenome e Idade
- ✅ Suporte a múltiplos formatos de arquivo
- ✅ Código totalmente comentado
- ✅ Funções separadas para cada funcionalidade
- ✅ Possibilidade de interface gráfica com TKinter

## 📁 Estrutura do Projeto

```
logica5/
├── README.md                 # Este arquivo
├── main.py                   # Arquivo principal da aplicação
├── funcoes.py               # Funções de leitura e gravação
├── interface.py             # Interface gráfica (opcional)
└── dados/                   # Diretório para armazenar arquivos
    ├── usuarios.txt
    ├── usuarios.csv
    └── usuarios.json
```

## 🛠️ Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas padrão do Python (não há dependências externas obrigatórias)
- TKinter (opcional, para interface gráfica)

## 💻 Como Usar

### Versão com Menu em Linha de Comando

```bash
# Execute o arquivo principal
python main.py
```

**Menu disponível:**
```
===== MENU PRINCIPAL =====
1. Ler dados
2. Salvar dados
3. Sair
Digite uma opção do menu (1-3):
```

### Versão com Interface Gráfica (Opcional)

```bash
# Execute a versão com TKinter
python interface.py
```

## 📝 Exemplos de Uso

### Salvar Dados

```
Escolha a opção: 2
Digite o nome: João
Digite o sobrenome: Silva
Digite a idade: 25
Escolha o formato (txt/csv/json): json
Dados salvos com sucesso em usuarios.json
```

### Ler Dados

```
Escolha a opção: 1
Escolha o formato (txt/csv/json): json
[Exibe os dados armazenados]
```

## 🔧 Funcionalidades Principais

### `salvar_dados(nome, sobrenome, idade, formato)`
Grava os dados do usuário em um arquivo no formato especificado.

### `ler_dados(formato)`
Lê e exibe os dados armazenados em um arquivo.

### `menu_principal()`
Gerencia a navegação entre as opções do programa.

## 📄 Formatos de Saída

### TXT
```
Nome: João | Sobrenome: Silva | Idade: 25
Nome: Maria | Sobrenome: Santos | Idade: 30
```

### CSV
```
nome,sobrenome,idade
João,Silva,25
Maria,Santos,30
```

### JSON
```json
{
  "usuarios": [
    {"nome": "João", "sobrenome": "Silva", "idade": 25},
    {"nome": "Maria", "sobrenome": "Santos", "idade": 30}
  ]
}
```

## 👥 Equipe

Desenvolvido por dupla como atividade de programação.

## 📚 Documentação

O código-fonte está totalmente comentado, explicando cada função e seção do programa para facilitar o entendimento.

## 🎓 Objetivo da Atividade

Esta atividade tem como objetivo praticar:
- Leitura e escrita de arquivos em Python
- Manipulação de dados em diferentes formatos
- Criação de funções reutilizáveis
- Desenvolvimento de interfaces com menus
- Boas práticas de programação (comentários, organização de código)

## 📦 Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/marcellerocha-art/logica5.git
cd logica5
```

2. Execute a aplicação:
```bash
python main.py
```

3. (Opcional) Para a versão com interface gráfica:
```bash
python interface.py
```

## 📄 Licença

Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais.

## 🙋 Suporte

Para dúvidas ou sugestões sobre o projeto, abra uma [issue](https://github.com/marcellerocha-art/logica5/issues).

---

**Repositório:** https://github.com/marcellerocha-art/logica5
