# ⛅ Previsão do Tempo com Python (RPA)
```bash
     .--.       .--.
  .-(    ).   .-(    ).
 (______)__) (______)__)
     ⚡  ⚡  ⚡
    PREVISÃO DO TEMPO
```

Este é um projeto simples de **RPA** usando **Python e Selenium** para automatizar a coleta da previsão do tempo no site *Climatempo*.  
O script acessa o site, pesquisa uma cidade, coleta a **temperatura atual**, **condição climática**, e salva tudo em uma planilha **Excel**.

## 💻 Tecnologias usadas

- Python 3.x  
- Selenium  
- OpenPyXL (para salvar em Excel)  
- ChromeDriver  

## 🛠️ Instalação

### 1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/previsao-tempo-rpa.git
cd previsao-tempo-rpa
```
### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Baixe o ChromeDriver compatível
Baixe aqui:

https://googlechromelabs.github.io/chrome-for-testing/

Coloque o executável na raiz do projeto ou adicione ao PATH.

### ▶️ Como executar:
```bash
python previsao.py
```
### ✏️ Personalização:
Para alterar a cidade pesquisada, edite no arquivo **previsao,py** a linha:
```bash
cidade = "São Paulo"
```
Você também pode:
- Pesquisar várias cidades.
- Rodar automaticamente todo dia com Task Scheduler (Windows)
- Ou cron (Linux/Mac)
  
### 📊 Exemplo de saída (Excel):
| Cidade    | Temperatura | Condição       |
| --------- | ----------- | -------------- |
| São Paulo | 24ºC        | Sol com nuvens |

## 🤖 Sobre
Este projeto é ideal para iniciantes que desejam aprender automação com Python e aplicar conceitos de **RPA** em tarefas reais.
## ✏️ Autor

Desenvolvido por [Ana Carolina Jerônimo](https://github.com/anacjeronimo) 🦇
