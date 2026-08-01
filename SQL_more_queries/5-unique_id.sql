-- creates table unique_id, id default 1 and unique
-- creates table unique_id with id default 1, unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
