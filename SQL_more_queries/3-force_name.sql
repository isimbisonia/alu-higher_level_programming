-- Creates the table force_name (name can't be null)
-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
