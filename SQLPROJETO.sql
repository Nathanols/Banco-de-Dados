
CREATE TABLE Clientes (
    ClienteID INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único do cliente
    Nome VARCHAR(100) NOT NULL, -- Nome do cliente
    Email VARCHAR(100) NULL, -- Email do cliente
    Telefone VARCHAR(20) NULL, -- Telefone do cliente
    Endereco VARCHAR(255) NULL -- Endereço do cliente
);

INSERT INTO Clientes (Nome, Email, Telefone, Endereco)
VALUES ('João Silva', 'joao@email.com', '123456789', 'Rua A, 123'),
       ('Maria Oliveira', 'maria@email.com', '987654321', 'Rua B, 456');



CREATE TABLE Produtos (
    ProdutoID INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único do produto
    Nome VARCHAR(100) NOT NULL, -- Nome do produto
    Descricao VARCHAR(255) NULL, -- Descrição do produto
    Preco DECIMAL(10, 2) NOT NULL, -- Preço do produto
    QuantidadeEmEstoque INT NOT NULL -- Quantidade disponível no estoque
);

INSERT INTO Produtos (Nome, Descricao, Preco, QuantidadeEmEstoque)
VALUES ('macarrao', 'pct', 50.00, 10),
       ('oleo', '!L', 25.00, 20);


CREATE TABLE Vendas (
    VendaID INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único da venda
    ClienteID INT, -- ID do cliente que fez a compra
    DataVenda DATETIME NOT NULL DEFAULT GETDATE(), -- Data e hora da venda
    Total DECIMAL(10, 2) NOT NULL, -- Valor total da venda
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID) -- Relacionamento com a tabela Clientes
);

INSERT INTO Vendas (ClienteID, Total)
VALUES 
	(2, 250.00),
	(2, 50.00);  -- ClienteID 1 (João Silva) fez uma compra no valor de 250,00



CREATE TABLE ItensVenda (
    ItemID INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único do item
    VendaID INT, -- ID da venda
    ProdutoID INT, -- ID do produto vendido
    Quantidade INT NOT NULL, -- Quantidade de produtos vendidos
    Preco DECIMAL(10, 2) NOT NULL, -- Preço do produto na venda
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID), -- Relacionamento com a tabela Vendas
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID) -- Relacionamento com a tabela Produtos
);

INSERT INTO ItensVenda (VendaID, ProdutoID, Quantidade, Preco)
VALUES (1, 1, 2, 100.00),  -- VendaID 1, ProdutoID 1 (Produto A), 2 unidades
       (1, 2, 1, 150.00);  -- VendaID 1, ProdutoID 2 (Produto B), 1 unidade


NOME
   





    
