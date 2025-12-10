# 2025-12-09

import sqlite3

DB_PATH = "data/contacts.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            email TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact(name, contact, email, notes):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, contact, email, notes) VALUES (?, ?, ?, ?)",
              (name, contact, email, notes))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    conn.close()
    return rows

def update_contact(contact_id, name, contact, email, notes):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""UPDATE contacts SET name=?, contact=?, email=?, notes=? WHERE id=?""",
              (name, contact, email, notes, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
