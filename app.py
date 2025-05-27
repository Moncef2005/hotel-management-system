import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    conn = sqlite3.connect('hotel.db')
    conn.row_factory = sqlite3.Row
    return conn

st.title("🏨 Gestion Hôtel")

# Afficher les réservations
if st.checkbox("Afficher les réservations"):
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT Reservation.id, date_debut, date_fin, Client.nom AS client_nom
        FROM Reservation
        JOIN Client ON Reservation.client_id = Client.id
    """, conn)
    st.dataframe(df)
    conn.close()

# Afficher les clients
if st.checkbox("Afficher les clients"):
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Client", conn)
    st.dataframe(df)
    conn.close()

# Chercher les chambres disponibles
if st.checkbox("Chercher des chambres disponibles"):
    date_debut = st.date_input("Date de début")
    date_fin = st.date_input("Date de fin")
    if st.button("Chercher"):
        conn = get_connection()
        df = pd.read_sql_query(f"""
            SELECT Chambre.id, Chambre.numero, TypeChambre.type, Hotel.ville
            FROM Chambre
            JOIN TypeChambre ON Chambre.typechambre_id = TypeChambre.id
            JOIN Hotel ON Chambre.hotel_id = Hotel.id
            WHERE Chambre.id NOT IN (
                SELECT Reservation.id
                FROM Reservation
                WHERE (date_debut BETWEEN '{date_debut}' AND '{date_fin}')
                OR (date_fin BETWEEN '{date_debut}' AND '{date_fin}')
            )
        """, conn)
        st.dataframe(df)
        conn.close()

# Ajouter un client
if st.checkbox("Ajouter un client"):
    with st.form("form_client"):
        nom = st.text_input("Nom")
        adresse = st.text_input("Adresse")
        ville = st.text_input("Ville")
        code_postal = st.text_input("Code postal")
        email = st.text_input("Email")
        telephone = st.text_input("Téléphone")
        submitted = st.form_submit_button("Ajouter")
        if submitted:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Client (adresse, ville, code_postal, email, telephone, nom)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (adresse, ville, code_postal, email, telephone, nom))
            conn.commit()
            conn.close()
            st.success(f"Client {nom} ajouté avec succès !")

# Ajouter une réservation
if st.checkbox("Ajouter une réservation"):
    conn = get_connection()
    clients = pd.read_sql_query("SELECT id, nom FROM Client", conn)
    conn.close()
    client_selection = st.selectbox("Client", clients['nom'])
    date_debut = st.date_input("Date début réservation")
    date_fin = st.date_input("Date fin réservation")
    if st.button("Ajouter réservation"):
        client_id = clients.loc[clients['nom'] == client_selection, 'id'].values[0]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Reservation (date_debut, date_fin, client_id)
            VALUES (?, ?, ?)
        """, (str(date_debut), str(date_fin), client_id))
        conn.commit()
        conn.close()
        st.success(f"Réservation ajoutée pour {client_selection} du {date_debut} au {date_fin}.")

