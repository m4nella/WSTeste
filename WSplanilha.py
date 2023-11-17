from bs4 import BeautifulSoup
import openpyxl

# html --> sem url --> arquivo local - apenas
with open('C:/Users/55137877840/Desktop/FPOO-Aula16-WebScraping-Pedidos.html', 'r', encoding='utf-8') as arquivo:
    conteudo_html = arquivo.read()
f = open('file.py')

soup = BeautifulSoup(conteudo_html, 'html.parser')

tabela = soup.find('table')

planilha = openpyxl.Workbook()
folha = planilha.active

for indice_linha, linha in enumerate(tabela.find_all('tr')):
    for indice_coluna, celula in enumerate(linha.find_all(['th', 'td'])):
        folha.cell(row=indice_linha + 1, column=indice_coluna + 1, value=celula.get_text(strip=True))

# salvando em excel
planilha.save('listinhapedidinhos.xlsx')

