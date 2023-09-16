<h1 align="center">
  📊 Teste Analista de Dados Júnior - NeoPerformance
</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=license&message=ISC&color=8022F5&style=flat">
  <a href="https://www.linkedin.com/in/pedro-afonso-lkdn/"><img src="https://img.shields.io/static/v1?label=made%20by&message=Pedro&color=4B00A8&style=flat"></a>
  <br/>
  <img src="https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Microsoft%20Excel-217346?logo=microsoft-excel&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Anaconda-44A833?logo=anaconda&logoColor=white&style=for-the-badge">
  
</p>

## :open_book: Sobre
Este é um projeto de análise de dados que automatiza a captura, tratamento e atualização de dados de vendas, permitindo a criação de dashboards no Google Data Studio para análise.

➡️ O link para o Data Studio com os dados organizados está aqui: https://lookerstudio.google.com/reporting/a70e3b48-d7f8-4dca-b4d3-279a13867e0d

## :gear: Features
- [x] Captura e atualização de dados de vendas a partir de um arquivo local (vendas.xls);
- [x] Tratamento de dados, incluindo conversão de tipos de dados, preenchimento de valores ausentes e cálculo de receita total;
- [x] Criação de colunas adicionais, como mês de venda e categoria do vendedor;
- [x] Exportação automática dos dados tratados para um arquivo CSV (vendas_tratadas.csv);
- [x] Agendamento de atualizações diárias dos dados usando o agendador de tarefas do Windows;
- [x] Utilização do Google Data Studio para criar dashboards personalizados com os dados tratados;
- [x] Update profile;

## 🧰 Tools
- **Python**
- **Jupyter Notebook**
- **Anaconda**
- **Microsoft Excel**
- **Google Data Studio**

## ⚠️ Pré-requisitos
  - Python 3.x instalado no ambiente local.
  - Bibliotecas Python, incluindo Pandas, Schedule e outras, instaladas. Você pode instalar as bibliotecas usando o comando pip install -r requirements.txt.
  - Ambiente Windows para agendar a execução do script updater.py.

## 🚀 Iniciando
1. Clone este repositório em seu ambiente local:

```bash
  git clone https://github.com/Pedro558/Teste-NeoPerformance.git
```
2. Certifique-se de que o arquivo 'vendas.xls' contém os dados de vendas. Você pode editá-lo localmente ou no Google Planilhas e salvar como 'vendas.xls' no diretório do projeto.

3. Configure o agendador de tarefas do Windows para executar o script 'updater.py' diariamente ou em outro intervalo desejado. Isso garantirá a atualização dos dados.

4. Execute o script 'tratamento_dados.py' manualmente ou por meio do agendador de tarefas do Windows para tratar os dados e exportá-los para 'vendas_tratadas.csv'.

5. No Google Data Studio, conecte-se ao arquivo 'vendas_tratadas.csv' como fonte de dados para criar visualizações e dashboards personalizados.

## 🦸‍♂️ Author
<p>
 <sub><strong>🌟 Pedro Afonso🌟</strong></sub>
</p>

>This project was made with ❤️ by **[Pedro Afonso](https://www.linkedin.com/in/pedro-afonso-lkdn/)**





