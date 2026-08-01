-- creates table force_name, name can not be null
-- creates table force_name with name NOT NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
