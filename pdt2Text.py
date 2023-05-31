import pdfkit

# Defina a URL da página que deseja salvar em PDF
url = 'http://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?k=B22C7881-BACD7-4062-8FF5-A52F78C33BDC1'

# Defina o caminho de destino para o arquivo PDF
output_path = 'output.pdf'

# Configure as opções do PDF
options = {
    'page-size': 'Letter',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

# Salve a página online como PDF
pdfkit.from_url(url, output_path, options=options)
