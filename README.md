Gerador de estrutura para projetos de dados.

 Cria estrutura completa de pastas automaticamente
 Gera módulos Python com arquivos __init__.py
 Visualização em árvore da estrutura criada
 README detalhado
 
Desenvolvido durante minha transição de Analista de Suporte para Engenharia de Dados. 
Organização é fundamental para projetos confiáveis. Estrutura baseada na arquitetura medallion (Bronze/Silver/Gold).

## Esquema da Estrutura Criada

projeto/
├── data/
│   ├── raw/          # Dados brutos
│   ├── processed/    # Dados limpos e validados
│   └── curated/      # Dados prontos
├── src/
│   ├── data_quality/ # Verificações de qualidade
│   ├── pipelines/    # ETL/ELT
│   └── utils/        # Auxiliares
├── tests/            # Testes 
├── notebooks/        # Análises exploratórias
├── docs/             # Documentação 
├── logs/             # Logs
└── scripts/          # Scripts de deploy/manut


## Como usar:
```bash
python setup.py