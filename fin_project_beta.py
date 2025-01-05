
# Função para buscar os dados do ativo financeiro
def fetch_data(ticker_symbol):
    """

    Parâmetros:
    ticker_symbol (str): Código do ativo na B3.

    Retorna:
    dict: Informações coletadas do ativo.
    """
    try:
        ticker = f.Ticker(ticker_symbol + ".SA")
        info = ticker.info
        return info
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return {}

# Função para pesquisa e exibição de dados do ativo
def search_data():
    """
    Interage com o usuário para obter código do ativo e chave de busca.

    Retorna:
    tuple: Dados coletados (dict) e símbolo do ativo (str).
    """
    user_text = input("Insira o código da ação na B3 (ex: PETR4): ").strip().upper()
    dados = fetch_data(user_text)

    if not dados:
        print("Código inválido ou falha na coleta de dados.")
        return {}, user_text

    # Carregar dicionário de chaves traduzidas
    dict_chaves = chaves()

    user_select = input("Insira o nome da variável para visualização: ").strip()

    if not user_select:
        print("Nenhuma variável especificada.")
        return {}, user_text

    # Buscar chaves correspondentes
    matching_keys = [k for k, v in dict_chaves.items() if v.lower() == user_select.lower()]

    if matching_keys:
        print("\nDados coletados:")
        for chave in matching_keys:
            valor = dados.get(chave, 'N/A')
            print(f"{chave} ({user_select}): {valor}")
    else:
        print("Nenhuma variável encontrada com a descrição fornecida.")

    return dados, user_text

# Função para salvar os dados coletados em arquivo de texto
def save_data(dados, user_text):
    """
    Salva os dados coletados em um arquivo de texto.

    Parâmetros:
    dados (dict): Dados coletados do ativo.
    user_text (str): Código do ativo fornecido pelo usuário.
    """
    try:
        # Criar diretório de saída, se não existir
        os.makedirs("dados_coletados", exist_ok=True)
        
        # Nome do arquivo
        file_path = os.path.join("dados_coletados", f"dados_{user_text}.txt")
        
        # Salvar os dados no arquivo
        with open(file_path, "w", encoding="utf-8") as file:
            for chave, valor in dados.items():
                linha = f"{chave}: {valor}\n"
                file.write(linha)
        print(f"Dados salvos com sucesso em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Execução principal do script
if __name__ == "__main__":
    print("\n--- Sistema de Coleta de Dados Financeiros ---\n")
    dados, user_text = search_data()
    if dados:
        save_data(dados, user_text)
    print("\nProcesso concluído!")
