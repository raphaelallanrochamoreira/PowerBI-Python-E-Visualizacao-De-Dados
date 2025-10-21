-- ==========================
-- TABELA: CLIENTES
-- ==========================
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    sexo CHAR(1),
    faixa_etaria VARCHAR(20),
    cidade VARCHAR(100),
    uf CHAR(2)
);

-- ==========================
-- TABELA: LOJAS
-- ==========================
CREATE TABLE Lojas (
    id_loja INT PRIMARY KEY,
    nome_loja VARCHAR(100),
    tipo_loja VARCHAR(50),
    cidade VARCHAR(100),
    uf CHAR(2)
);

-- ==========================
-- TABELA: PRODUTOS
-- ==========================
CREATE TABLE Produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    fornecedor VARCHAR(100),
    custo DECIMAL(10,2)
);

-- ==========================
-- TABELA: TEMPO
-- ==========================
CREATE TABLE Tempo (
    id_tempo INT PRIMARY KEY,
    ano INT,
    mes INT,
    nome_mes VARCHAR(20),
    trimestre INT
);

-- ==========================
-- TABELA: VENDAS (TABELA FATO)
-- ==========================
CREATE TABLE Vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT,
    id_loja INT,
    id_produto INT,
    id_tempo INT,
    quantidade INT,
    valor_unitario DECIMAL(10,2),
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    CONSTRAINT fk_loja FOREIGN KEY (id_loja) REFERENCES Lojas(id_loja),
    CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto),
    CONSTRAINT fk_tempo FOREIGN KEY (id_tempo) REFERENCES Tempo(id_tempo)
);
