import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

server = '172.16.66.6' 
database = 'LOJA'
username = 'sa'
password = 'Senai@134'

try:
    conexao = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={
            server};DATABASE={database};UID={username};PWD={password}'
    )
    print("Conexão estabelecida com sucesso!")

    query_clientes = "SELECT * FROM clientes;"
    query_produtos = "SELECT * FROM produtos;"
    query_vendas = "SELECT * FROM vendas;"
    query_itensVenda = "SELECT * FROM ItensVenda;"
    query_detalhes = """
    SELECT 
        v.VendaID,  
        c.Nome AS Cliente,
        v.Total
    FROM   
        Vendas v
    JOIN 
        Clientes c ON v.ClienteID = c.ClienteID;
    """
    query_vendas_cliente = """
    SELECT 
        v.VendaID, 
        v.DataVenda, 
        v.Total
    FROM 
        Vendas v
    JOIN 
    Clientes c ON v.ClienteID = c.ClienteID
    WHERE c.Nome = 'Maria Oliveira';
    """

    df_clientes = pd.read_sql(query_clientes, conexao)
    df_produtos = pd.read_sql(query_produtos, conexao)
    df_vendas = pd.read_sql(query_vendas, conexao)
    df_itensVenda = pd.read_sql(query_itensVenda, conexao)
    df_detalhes = pd.read_sql(query_detalhes, conexao)
    df_vendas_cliente = pd.read_sql(query_vendas_cliente, conexao)

    print("\nClientes: ")
    print(df_clientes.head())

    print("\nprodutos: ")
    print(df_produtos.head())

    print("\nVendas: ")
    print(df_vendas.head())

    print("\nItens das Vendas: ")
    print(df_itensVenda.head())

    print("\nCliente que comprou o produto: ")
    print(df_detalhes.head())

    print("\nVendas do cliente: ")
    print(df_vendas_cliente.head())

    #---------------------------------------------------------------

# Agrupar as vendas por cliente e calcular o total vendido
    total_vendas_cliente = df_vendas.groupby('ClienteID')['Total'].sum()

    # Exibir o resultado
    print("Total de vendas por cliente:")
    print(total_vendas_cliente)

    total_vendas_cliente.plot(kind='bar', figsize=(
        8, 6), color='red', title='Total de Vendas por Cliente')
    plt.xlabel('Cliente')
    plt.ylabel('Valor Total (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

     #---------------------------------------------------------------

    vendas_por_produto = df_itensVenda.groupby('ProdutoID')['Quantidade'].sum()

    print("Total de vendas por produto:")
    print(vendas_por_produto)

    # Criar um gráfico de pizza
    vendas_por_produto.plot(kind='pie', figsize=(
        8, 8), autopct='%1.1f%%', title='Distribuição de Vendas por Produto')
    plt.ylabel('')  # Remover o rótulo automático do eixo Y
    plt.show()

    #---------------------------------------------------------------

    # Converter a coluna DataVenda para o formato datetime
    df_vendas['DataVenda'] = pd.to_datetime(df_vendas['DataVenda'])

    # Agrupar as vendas por mês e somar os valores
    vendas_mensais = df_vendas.resample('M', on='DataVenda')['Total'].sum()

    # Exibir os dados
    print("Evolução mensal de vendas:")
    print(vendas_mensais)

    # Criar um gráfico de linha para visualizar a evolução
    vendas_mensais.plot(kind='line', figsize=(10, 6), marker='o', title='Evolução Mensal de Vendas')
    plt.xlabel('Mês')
    plt.ylabel('Valor Total (R$)')
    plt.grid()
    plt.show()


except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)

finally:
    if 'conexao' in locals() and conexao:
        conexao.close()
        print("Conexão fechada.")