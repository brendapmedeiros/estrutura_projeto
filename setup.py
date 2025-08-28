import os

def cria_estrutura_projeto():
    """
    Cria estrutura para projetos de engenharia de dados
    
    Inclui:
    - Organização por camadas 
    - Estrutura para testes automatizados  
    - Configurações e documentação
    """
    
    # Adiciona  pastas:
    pastas = [
        'data/raw',           
        'data/processed',     
        'data/curated',       
        'src/data_quality',   
        'src/pipelines',      
        'src/utils',          
        'src/dashboards',    
        'config',             
        'tests',              
        'notebooks',          
        'docs',               
        'logs',              
        'scripts'           
    ]
    
    print("Criando estrutura de pastas")
    
    for pasta in pastas:
        try:
            os.makedirs(pasta, exist_ok=True)  # não dá erro se já existir
            print(f"Pasta criada: {pasta}")
        except Exception as e:
            print(f"Erro ao criar {pasta}: {e}")
    
    # Cria arquivos __init__.py para fazer das pastas módulos 
    arquivos_init = [
        'src/__init__.py',
        'src/data_quality/__init__.py',
        'src/dashboards/__init__.py',
        'src/pipelines/__init__.py',
        'src/utils/__init__.py'
    ]
    
    print("\nCriando arquivos de módulo")
    for arquivo in arquivos_init:
        try:
            with open(arquivo, 'w') as f:
                f.write('# Módulo Python\n')
            print(f"Arquivo criado: {arquivo}")
        except Exception as e:
            print(f"Erro ao criar {arquivo}: {e}")
    
    # Cria README básico
    readme_content = """

## Estrutura:

### Dados
- `data/raw/`: Dados brutos
- `data/processed/`: Dados limpos e validados
- `data/curated/`: Dados prontos 

### Código
- `src/data_quality/`: Verificações de qualidade
- `src/pipelines/`: Scripts  ETL/ELT
- `src/utils/`: Auxiliares
- `src/dashboards/`: Dataviz

### Outros
- `config/`: Configurações de ambiente
- `tests/`: Testes automatizados
- `notebooks/`: Análises
- `docs/`: Documentação do projeto
- `logs/`: Logs de execução
- `scripts/`: Scripts de deploy/manut

"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md criado")
    print("\nEstrutura do projeto criada!")
    print("Sua estrutura:")
    
    # Mostra o esquema de pastas
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if not file.startswith('.'):  # Ignora ocultos
                print(f"{subindent}{file}")

if __name__ == "__main__":
    cria_estrutura_projeto()