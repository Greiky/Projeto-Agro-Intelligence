USE agro_intelligence;

CREATE TABLE dados_plantacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    cultura VARCHAR(50),
    umidade_solo DECIMAL(5,2),
    temperatura DECIMAL(5,2),
    ph DECIMAL(4,2)
);