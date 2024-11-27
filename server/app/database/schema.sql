DROP TABLE IF EXISTS utilisateurs;
DROP TABLE IF EXISTS transactions;

CREATE TABLE utilisateurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    hasTR BOOLEAN NOT NULL,
    montantTR DECIMAL NOT NULL,
    partSalarialeTR DECIMAL NOT NULL,
    partPatronaleTR DECIMAL NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    participant1_id INT NOT NULL,
    participant2_id INT NOT NULL,
    montantCommande DECIMAL NOT NULL,
    montantTR_participant1 DECIMAL NOT NULL,
    montantTR_participant2 DECIMAL NOT NULL,
    FOREIGN KEY (participant1_id) REFERENCES utilisateurs(id),
    FOREIGN KEY (participant2_id) REFERENCES utilisateurs(id)
);