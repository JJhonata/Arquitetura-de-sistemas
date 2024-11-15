import json

def carregarJson(file):
    with open(file, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    dados = json.loads(conteudo)
    return dados


def calcularMediaSalarial(dados):
    soma = sum(item["salario"] for item in dados)
    media = soma / len(dados)
    return media
   
   
def calcularMediaIdade(dados):
    soma = sum(item["idade"] for item in dados)
    media = soma // len(dados)
    return media
   
if __name__ == "__main__":
    dados_json = carregarJson("clientes.txt")

    media_salarial = calcularMediaSalarial(dados_json)
    faixa_etaria_media = calcularMediaIdade(dados_json)

    print(f'Média salarial: {media_salarial:.2f}')
    print(f'Faixa etária média: {faixa_etaria_media}')