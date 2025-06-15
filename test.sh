#!/bin/bash


RUST_DIR=path_finder_rust
PYTHON_DIR=path_finder_python

# Função para tratar erros
handle_error() {
    echo "Erro: $1"
    exit 1
}

# Testes para o algoritmo em Python
echo "Executando testes para o algoritmo em Python..."
cd $PYTHON_DIR || handle_error "Diretório $PYTHON_DIR não encontrado"

# Criar e ativar o venv
python3 -m venv venv || handle_error "Falha ao criar o venv"
source venv/bin/activate || handle_error "Falha ao ativar o venv"

# Instalar dependências
pip install -r requirements.txt || handle_error "Falha ao instalar dependências"

# Executar testes com pytest
pytest || handle_error "Testes em Python falharam"

# Desativar o venv
deactivate

# Voltar ao diretório raiz
cd ..

# Testes para o algoritmo em Rust
echo "Executando testes para o algoritmo em Rust..."
cd $RUST_DIR || handle_error "Diretório $RUST_DIR não encontrado"

# Instalar dependências e executar testes com cargo
cargo test || handle_error "Testes em Rust falharam"

# Voltar ao diretório raiz
cd ..

echo "Todos os testes foram executados com sucesso!"