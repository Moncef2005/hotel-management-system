# 🏨 Hotel Management System  
### Application Web de Gestion d’Hôtel avec Python & Streamlit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Functional-success)

---

## 📌 Description

Ce projet est une application web développée en **Python** utilisant **Streamlit** pour l’interface utilisateur et **SQLite** comme système de gestion de base de données.

L’application permet de gérer les informations liées aux hôtels, clients et réservations via une interface interactive simple et efficace.

Ce projet a été réalisé dans un cadre pédagogique afin de mettre en pratique :

- La conception d’une base de données relationnelle
- Les requêtes SQL (SELECT, JOIN, INSERT, GROUP BY)
- L’interaction Python / SQLite
- Le développement d’une application web légère avec Streamlit

---

## 🎯 Fonctionnalités

### 🔎 Consultation des données
- Affichage des clients
- Affichage des réservations avec jointure Client
- Recherche des chambres disponibles selon une période

### ➕ Gestion des données
- Ajout d’un nouveau client
- Ajout d’une réservation

---

## 🏗 Architecture du Projet
```
hotel-management-system/
│
├── app.py # Interface Streamlit
├── create_hotel_db.py # Script de création et initialisation BDD
├── hotel.db # Base de données SQLite
└── README.md # Documentation

```

---

## 🗄 Conception de la Base de Données

### Tables principales

| Table | Description |
|--------|-------------|
| Hotel | Informations des hôtels |
| Client | Données des clients |
| Chambre | Informations des chambres |
| TypeChambre | Type et prix des chambres |
| Reservation | Réservations effectuées |
| Evaluation | Avis des clients |
| Prestation | Services proposés |

### Relations

- Un **client** peut avoir plusieurs **réservations**
- Une **chambre** appartient à un **hôtel**
- Une **chambre** possède un **type**

---

## ⚙ Installation & Exécution

### 1️ Cloner le dépôt

```bash
git clone https://github.com/Moncef2005/hotel-management-system.git
cd hotel-management-system

```
### 2 Initialiser la base de données

python create_hotel_db.py

Ce script :

- Supprime les anciennes tables

- Crée la structure complète

- Insère des données de test

### 3 Lancer l’application

streamlit run app.py

L’application s’ouvrira automatiquement dans le navigateur.

## 🧠 Concepts Techniques Utilisés

- Connexion SQLite avec sqlite3

- Exécution de requêtes SQL avancées

- Jointures entre tables

- Utilisation de pandas.read_sql_query

- Interface interactive avec Streamlit

- Gestion de formulaires avec st.form

- Paramètres SQL sécurisés

## 📊 Exemple de Requête SQL Utilisée

```sql
SELECT Reservation.id, date_debut, date_fin, Client.nom
FROM Reservation
JOIN Client ON Reservation.client_id = Client.id;

```
## Captures d’écran

### Page principale
<img width="1911" height="879" alt="image" src="https://github.com/user-attachments/assets/ec74ce1f-4007-4440-87b6-e17161e16c29" />

### Affichage des réservation
<img width="1238" height="703" alt="image" src="https://github.com/user-attachments/assets/96db34b0-cc2b-481c-83cf-bf6609f73f4a" />

### Affichage des clients
<img width="1232" height="614" alt="image" src="https://github.com/user-attachments/assets/292ac9f5-2111-4a5b-b143-3468cb4ed1ae" />

### Recherche des chambres disponibles
<img width="1353" height="396" alt="image" src="https://github.com/user-attachments/assets/41d4cb4a-beb7-41d0-a4f9-8b90a07f7c5f" />

### Ajout d’un client
<img width="1890" height="881" alt="image" src="https://github.com/user-attachments/assets/390431cb-a357-4f3b-b0fc-7cd50dc84e12" />

### ajout d"une réservation 
<img width="1201" height="521" alt="image" src="https://github.com/user-attachments/assets/c901d511-1b54-4764-b668-d95a26dbb08e" />

## 🚀 Améliorations Possibles
- Ajout de la suppression/modification des réservations

- Gestion des chambres par disponibilité réelle

- Authentification administrateur

- Déploiement en ligne (Streamlit Cloud)

- Ajout de statistiques (revenus, taux d’occupation)

### 👨‍💻 Auteur
Moncef Aaouine

Étudiant en Sciences Informatiques


