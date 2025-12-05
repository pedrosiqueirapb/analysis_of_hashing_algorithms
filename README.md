# Análise Comparativa de Algoritmos de Hashing na Proteção de Senhas em Sistemas de Informação

Repositório técnico do Trabalho de Conclusão de Curso desenvolvido por **Gabriella Dantas de Abreu Fandim** e **Pedro Siqueira Pereira Bitarães**, com o objetivo de analisar e comparar diferentes algoritmos de hashing aplicados à proteção de senhas em sistemas de informação.

## 🎯 Objetivos da Pesquisa

O projeto investiga o comportamento dos algoritmos **Argon2**, **bcrypt** e **SHA-256**, avaliando dois aspectos complementares:

1. **Medições do Servidor (Uso Legítimo)**  
   Avaliam o tempo de processamento durante a geração dos hashes, simulando o comportamento de um sistema real ao aplicar algoritmos de hashing a senhas.

2. **Medições de Resistência (Cenário de Ataque)**  
   Analisam a facilidade ou dificuldade de comprometer os hashes por meio de ataques de dicionário utilizando o John the Ripper, registrando métricas como tempo de quebra e uso de CPU e memória durante o ataque.

Essas análises permitem balancear **segurança x desempenho**, mostrando o custo computacional de proteger uma senha e o esforço necessário para quebrá-la.

## ⚙️ Metodologia e Arquitetura Experimental

O ambiente foi construído em Python e PowerShell, automatizando todas as etapas do experimento.  
O script principal `run_full_benchmark.ps1` executa o ciclo completo:

1. **Geração da lista de senhas**
   - Arquivo `generate_passwords.py` gera a amostra de senhas utilizada nos experimentos.

2. **Geração dos hashes**  
   - Arquivo `generate_hashes_full.py` produz os hashes para Argon2, bcrypt e SHA-256 a partir da lista de senhas gerada.

3. **Medições de desempenho do servidor**  
   - Script `benchmark_server.py` mede o tempo médio de cada algoritmo no contexto de uso legítimo.

4. **Execução de ataques práticos**  
   - O **John the Ripper** é utilizado para tentar recuperar as senhas (apenas bcrypt e SHA-256).
   - O script `monitor_john.ps1` registra CPU e memória durante o ataque.

5. **Análise e consolidação de resultados**  
   - O script `prepare_results.py` processa os dados gerados, calcula médias e percentuais e gera gráficos e arquivos `.csv`.

## 🔐 Sobre o Conjunto de Senhas Utilizado

O arquivo `passwords.xlsx` contém o conjunto de senhas utilizadas nos experimentos.  
Essas senhas são geradas automaticamente pelo script `generate_passwords.py`, que produz uma lista variada de combinações alfanuméricas, símbolos e formatos diferentes, simulando cenários comuns de autenticação.

Esse conjunto é utilizado tanto na geração dos hashes quanto na criação do arquivo `wordlist_test.txt`, empregado pelo John the Ripper durante os testes de resistência.  
Todo o conteúdo é totalmente artificial, criado exclusivamente para fins acadêmicos e experimentais, sem qualquer relação com senhas reais de usuários.

## 🧪 Como Executar o Projeto

### 1. Requisitos

- **Python 3.12+**
- **PowerShell 5.0+**
- **John the Ripper** instalado (ex: `C:\john\john-1.9.0-jumbo-1-win64\run\john.exe`)
- Sistema operacional Windows

### 2. Preparação do Ambiente

```bash
# Clonar o repositório
git clone https://github.com/pedrosiqueirapb/hashing-comparison-tcc.git
cd hashing-comparison-tcc

# Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependências
python -m pip install -r requirements.txt

# Gerar a lista de senhas
python .\scripts\generate_passwords.py

# Executar o experimento completo
.\scripts\run_full_benchmark.ps1 -bcrypt_rounds 12
```

O processo leva alguns minutos e gera automaticamente todos os resultados em /results.

## 📊 Resultados Gerados

Após a execução, os principais arquivos produzidos são:

| Arquivo                         | Descrição                                          |
| ------------------------------- | -------------------------------------------------- |
| **server_benchmarks.csv**       | Tempos e memória medidos no servidor.              |
| **summary_table.csv**           | Tabela consolidada dos resultados do servidor.     |
| **john_bcrypt_monitor.csv**     | Monitoramento de CPU/memória do ataque ao bcrypt.  |
| **john_sha256_monitor.csv**     | Monitoramento de CPU/memória do ataque ao SHA-256. |
| **john_bcrypt_show.txt**        | Resultado do `--show` para bcrypt.                 |
| **john_sha256_show.txt**        | Resultado do `--show` para SHA-256.                |
| **john_results.csv**            | Percentual de senhas quebradas por algoritmo.      |
| **monitor_summary.csv**         | Média de memória usada durante os ataques.         |
| **plot_cracked_vs_memoria.png** | Gráfico: % quebrado × memória média.               |
| **plot_time_per_hash.png**      | Gráfico de tempo médio por hash (escala log).      |
| **plot_crack_time_total.png**   | Gráfico do tempo total de quebra por algoritmo.    |

## 👥 Autores

[Gabriella Dantas de Abreu Fandim](https://github.com/gabriellaxdantas), [Pedro Siqueira Pereira Bitarães](https://github.com/pedrosiqueirapb)

Orientador: Prof. **Luciana Mara Freitas Diniz**  
Curso de *Sistemas de Informação* — Pontifícia Universidade Católica de Minas Gerais

## 📚 Licença e Uso Acadêmico

Este projeto possui finalidade estritamente acadêmica, criado no contexto de um Trabalho de Conclusão de Curso.
Todo o código, dados e scripts foram desenvolvidos com foco em estudos de segurança da informação, comparação de algoritmos de hashing e reprodutibilidade científica.

O uso deste repositório está alinhado:

- Às boas práticas de segurança definidas pela ISO/IEC 27001 e 27002, que recomendam o uso de funções de hash robustas e técnicas de fortalecimento de senhas;
- Às diretrizes da Lei Geral de Proteção de Dados (LGPD), uma vez que nenhum dado pessoal ou sensível é empregado nos experimentos.

Todo o conjunto de senhas utilizado é artificial e não representa nenhum dado de usuário real. O projeto não deve ser aplicado diretamente em ambientes produtivos, pois seu propósito é exclusivamente didático e experimental.
