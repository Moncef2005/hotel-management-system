import sqlite3

# Étape 1 : Connexion à la base (création si elle n'existe pas)
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()
print("✅ Étape 1 : Connexion ouverte ou fichier créé.")

# Étape 2 : Supprimer les tables si elles existent déjà (pour rejouer le script)
cursor.executescript("""
DROP TABLE IF EXISTS Hotel;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Prestation;
DROP TABLE IF EXISTS TypeChambre;
DROP TABLE IF EXISTS Chambre;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Evaluation;
""")
print("✅ Étape 2 : Tables précédentes supprimées (si présentes).")

# Étape 3 : Créer les tables
cursor.executescript("""
CREATE TABLE Hotel (
    id INTEGER PRIMARY KEY,
    ville TEXT,
    pays TEXT,
    code_postal INTEGER
);

CREATE TABLE Client (
    id INTEGER PRIMARY KEY,
    adresse TEXT,
    ville TEXT,
    code_postal INTEGER,
    email TEXT,
    telephone TEXT,
    nom TEXT
);

CREATE TABLE Prestation (
    id INTEGER PRIMARY KEY,
    prix REAL,
    description TEXT
);

CREATE TABLE TypeChambre (
    id INTEGER PRIMARY KEY,
    type TEXT,
    prix REAL
);

CREATE TABLE Chambre (
    id INTEGER PRIMARY KEY,
    numero INTEGER,
    etage INTEGER,
    balcon BOOLEAN,
    hotel_id INTEGER,
    typechambre_id INTEGER,
    FOREIGN KEY(hotel_id) REFERENCES Hotel(id),
    FOREIGN KEY(typechambre_id) REFERENCES TypeChambre(id)
);

CREATE TABLE Reservation (
    id INTEGER PRIMARY KEY,
    date_debut TEXT,
    date_fin TEXT,
    client_id INTEGER,
    FOREIGN KEY(client_id) REFERENCES Client(id)
);

CREATE TABLE Evaluation (
    id INTEGER PRIMARY KEY,
    date TEXT,
    note INTEGER,
    commentaire TEXT,
    client_id INTEGER,
    FOREIGN KEY(client_id) REFERENCES Client(id)
);
""")
print("✅ Étape 3 : Tables créées.")

# Étape 4 : Insérer les données
cursor.executescript("""
-- Hotels
INSERT INTO Hotel VALUES (1, 'Paris', 'France', 75001);
INSERT INTO Hotel VALUES (2, 'Lyon', 'France', 69002);

-- Clients
INSERT INTO Client VALUES (1, '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678', 'Jean Dupont');
INSERT INTO Client VALUES (2, '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789', 'Marie Leroy');
INSERT INTO Client VALUES (3, '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890', 'Paul Moreau');
INSERT INTO Client VALUES (4, '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901', 'Lucie Martin');
INSERT INTO Client VALUES (5, '3 Rue des Fleurs', 'Nice', 06000, 'emma.giraud@email.fr', '0656789012', 'Emma Giraud');

-- Prestations
INSERT INTO Prestation VALUES (1, 15, 'Petit-déjeuner');
INSERT INTO Prestation VALUES (2, 30, 'Navette aéroport');
INSERT INTO Prestation VALUES (3, 0, 'Wi-Fi gratuit');
INSERT INTO Prestation VALUES (4, 50, 'Spa et bien-être');
INSERT INTO Prestation VALUES (5, 20, 'Parking sécurisé');

-- Types de chambres
INSERT INTO TypeChambre VALUES (1, 'Simple', 80);
INSERT INTO TypeChambre VALUES (2, 'Double', 120);

-- Chambres
INSERT INTO Chambre VALUES (1, 201, 2, 0, 1, 1);
INSERT INTO Chambre VALUES (2, 502, 5, 1, 1, 2);
INSERT INTO Chambre VALUES (3, 305, 3, 0, 2, 1);
INSERT INTO Chambre VALUES (4, 410, 4, 0, 2, 2);
INSERT INTO Chambre VALUES (5, 104, 1, 1, 2, 2);
INSERT INTO Chambre VALUES (6, 202, 2, 0, 1, 1);
INSERT INTO Chambre VALUES (7, 307, 3, 1, 1, 2);
INSERT INTO Chambre VALUES (8, 101, 1, 0, 1, 1);

-- Réservations
INSERT INTO Reservation VALUES (1, '2025-06-15', '2025-06-18', 1);
INSERT INTO Reservation VALUES (2, '2025-07-01', '2025-07-05', 2);
INSERT INTO Reservation VALUES (7, '2025-11-12', '2025-11-14', 2);
INSERT INTO Reservation VALUES (10, '2026-02-01', '2026-02-05', 2);
INSERT INTO Reservation VALUES (3, '2025-08-10', '2025-08-14', 3);
INSERT INTO Reservation VALUES (4, '2025-09-05', '2025-09-07', 4);
INSERT INTO Reservation VALUES (9, '2026-01-15', '2026-01-18', 4);
INSERT INTO Reservation VALUES (5, '2025-09-20', '2025-09-25', 5);

-- Évaluations
INSERT INTO Evaluation VALUES (1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 1);
INSERT INTO Evaluation VALUES (2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 2);
INSERT INTO Evaluation VALUES (3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 3);
INSERT INTO Evaluation VALUES (4, '2025-09-05', 5, 'Service impeccable, je recommande.', 4);
INSERT INTO Evaluation VALUES (5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 5);
""")
print("✅ Étape 4 : Données insérées.")

# Étape 5 : Sauvegarder les changements
conn.commit()
print("✅ Étape 5 : Changements sauvegardés.")

# Étape 6 : Exécuter des requêtes simples
print("\n--- Liste des clients ---")
cursor.execute("SELECT id, nom, ville FROM Client")
for row in cursor.fetchall():
    print(row)

print("\n--- Réservations avec nom client ---")
cursor.execute("""
SELECT Reservation.id, Reservation.date_debut, Reservation.date_fin, Client.nom
FROM Reservation
JOIN Client ON Reservation.client_id = Client.id
""")
for row in cursor.fetchall():
    print(row)

print("\n--- Nombre de réservations par client ---")
cursor.execute("""
SELECT Client.nom, COUNT(Reservation.id)
FROM Client
LEFT JOIN Reservation ON Client.id = Reservation.client_id
GROUP BY Client.nom
""")
for row in cursor.fetchall():
    print(row)

# Étape 7 : Fermer la connexion
conn.close()
print("\n✅ Étape 7 : Connexion fermée. Fichier 'hotel.db' prêt.")

