
def mostrar_lista(pessoas):
    return pessoas  # essa função irá mostrar a lista inteira


# função de contar idade maiores que 50
def contador_de_idade(pessoas):
    contador = 0  # começamos com um contador
    for pessoa in pessoas:  # percorrendo a lista
        if (
            pessoa["idade"] > 50
        ):  # se as idades da lista forem maiores que 50, contador será incrementado +1
            contador += 1
    return contador

# função de contar salario maior de 2000 reais e calcular a porcentagem
def counter_salario(pessoas):
    contador_salario_percent = 0
    contador_salario_total = 0

    for pessoa in pessoas:
        if pessoa["salario"] > "2000":
            contador_salario_percent += 1
        contador_salario_total += 1

    if contador_salario_total != 0:
        total_percent = (contador_salario_percent / contador_salario_total) * 100
    else:
        total_percent = 0

    print("Número de pessoas com salário maior que 2000:", contador_salario_percent)
    print("Total de pessoas:", contador_salario_total)
    print("Porcentagem de pessoas com salário maior que 2000:", total_percent)
    lista_de_retorno = [contador_salario_percent, total_percent, contador_salario_total]
    return tuple(lista_de_retorno)


# função para obter os três maiores salarios
def tres_maiores_salarios(pessoas):
    # função sorted ordena a lista da maior para a menor
    # buscando a lista pessoas e indo diretamente em salario
    pessoas_ordenadas_por_salario = sorted(
        pessoas, key=lambda x: x["salario"], reverse=True
    )
    print("As 3 pessoas com maiores salários são:")
    for pessoa in pessoas_ordenadas_por_salario[:3]:
        # percorre pessoas dentro da variável pessoas_ordenadas_por_salario e pega as três primeiras, printando
        pessoa_maiores_salarios = pessoa
    return pessoa_maiores_salarios

def calcular_media_salarios(pessoas):
    # Dicionário para armazenar os salários de cada profissão
    salarios_por_profissao = {}
    contador_por_profissao = {}
    # Itera sobre cada pessoa na lista
    for pessoa in pessoas:
        profissao = pessoa["profissao"]
        salario = float(pessoa["salario"])  # Convertendo para float
        # Adiciona o salário ao total para essa profissão
        salarios_por_profissao[profissao] = (
            salarios_por_profissao.get(profissao, 0) + salario
        )
        contador_por_profissao[profissao] = contador_por_profissao.get(profissao, 0) + 1
    # Calcula a média para cada profissão
    media_salarios = {}
    for profissao, total_salarios in salarios_por_profissao.items():
        contador = contador_por_profissao[profissao]
        media_salarios[profissao] = total_salarios / contador
    return media_salarios
# Calcula a média salarial para cada profissão

def imprimir_media(pessoas):
    medias = calcular_media_salarios(pessoas)
    # Imprime os resultados
    for profissao, media in medias.items():
        print(f"Média salarial de {profissao}: R${media:.2f}")
        profissao = profissao
        media = media
    return profissao and media
    


# Definindo a função intervalo_de_idade que recebe uma lista de dicionários chamada 'pessoas'
def intervalo_de_idade(pessoas):
    # Inicializa uma lista vazia para armazenar pessoas com salário acima de 2000
    lista_mais_2000 = []
    # Itera sobre cada pessoa no parâmetro 'pessoas'
    for pessoa in pessoas:
        # Obtém o valor associado à chave 'salario' no dicionário 'pessoa'. Se a chave não existir, retorna 0.
        salarios = pessoa.get("salario", 0)
        # Verifica se o salário é maior que "2000" (o que compara como strings, não como números).
        if salarios > "2000":
            # Se o salário for maior que "2000", adiciona a pessoa à lista_mais_2000
            lista_mais_2000.append(pessoa)
    # Verifica se há pessoas na lista_mais_2000
    if lista_mais_2000:
        # Cria uma lista de idades a partir dos dicionários de pessoas em lista_mais_2000
        idades = [pessoa.get("idade", 0) for pessoa in lista_mais_2000]
        # Cria uma lista de sexos a partir dos dicionários de pessoas em lista_mais_2000
        sexo = [pessoa.get("sexo") for pessoa in lista_mais_2000]
        # Calcula a média das idades
        idade_media = sum(idades) / len(idades)
        # Encontra o sexo mais frequente na lista
        sexo_mais_frequente = max(set(sexo), key=sexo.count)
        sexo_menos_frequente = min(set(sexo),key=sexo.count)
        # Imprime a média das idades e o sexo mais frequente no formato "{idade_media},{sexo_mais_frequente}"
        print(f"{idade_media},{sexo_mais_frequente}")
    lista_de_return = [idade_media, sexo_mais_frequente, sexo_menos_frequente]
    return lista_de_return