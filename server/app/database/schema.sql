DROP TABLE IF EXISTS operation_utilisateur;
DROP TABLE IF EXISTS operation;
DROP TABLE IF EXISTS utilisateur;

CREATE TABLE utilisateur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    hasTR BOOLEAN NOT NULL,
    valeurTR DECIMAL NOT NULL,
    partSalarialeTR DECIMAL NOT NULL,
    partPatronaleTR DECIMAL NOT NULL
);

CREATE TABLE operation (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    montantCommande DECIMAL NOT NULL,
    montantTR DECIMAL NOT NULL -- Total des titres-restaurant utilisés dans cette operation
);

CREATE TABLE operation_utilisateur (
    id SERIAL PRIMARY KEY,
    operation_id INTEGER NOT NULL,
    utilisateur_id INTEGER NOT NULL,
    montantTR_utilise DECIMAL NOT NULL,
    FOREIGN KEY (operation_id) REFERENCES operation(id) ON DELETE CASCADE,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id) ON DELETE CASCADE
);

INSERT INTO utilisateur (nom, hasTR, valeurTR, partSalarialeTR, partPatronaleTR)
VALUES ('Alice', TRUE, 8.0, 3.5, 4.5),
       ('Bob', TRUE, 8.0, 3.5, 4.5);

INSERT INTO operation (date, montantCommande, montantTR)
VALUES ('2024-11-28', 50.00, 16.00);

INSERT INTO operation_utilisateur (operation_id, utilisateur_id, montantTR_utilise)
VALUES (1, 1, 8.00), -- Alice a utilisé 8€
       (1, 2, 8.00); -- Bob a utilisé 8€
