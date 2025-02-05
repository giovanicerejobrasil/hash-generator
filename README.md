# Hash Generator

Sistema de geração de hashs com Python utilizando PySide6, hashlib e secrets.

## Stack utilizada

Python 3.13

## Funcionalidades

Gera hashs de MD5 à SHA3_512 através do hashlib, biblioteca padrão do Python.

O sistema precisa de uma senha, o salt é opcional e o tipo de hash que você deseja gerar. Você gera a hash e caso você não informe o salt a cada execução do botão de gerar senha o sistema gerará um salt aleatório.

Existe também um sistema de copiar a hash para o clipboar `(ctrl + v)` sem precisar selecioná-la por completo.

Aproveite!

## Screenshots

[![Screenshot-from-2025-02-05-15-44-26.png](https://i.postimg.cc/tTSwbqBC/Screenshot-from-2025-02-05-15-44-26.png)](https://postimg.cc/qhKjXTf9)

## Rodando localmente

Fça o clone do projeto

```bash
  git clone https://github.com/giovanicerejobrasil/hash-generator.git
```

Entre no diretório do projeto

```bash
  cd hash-generator
```

Crie o ambiente virtual de desenvolvimento Python e ative-o

```bash
  python -m venv venv
  . ./venv/bin/activate
```

Instale as dependências

```bash
  pip install requirements.txt
```

Inicie o app

```bash
  ./venv/bin/python main.py
```
