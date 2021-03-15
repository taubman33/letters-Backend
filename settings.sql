-- settings.sql
CREATE DATABASE letter;
CREATE USER letteruser WITH PASSWORD 'letter';
GRANT ALL PRIVILEGES ON DATABASE letter TO letteruser;