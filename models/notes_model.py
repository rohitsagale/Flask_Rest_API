# models/notes_model.py
from db import get_db_connection

def add_note_to_db(title, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO notes(title, content) VALUES (%s,%s)", (title, content))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_all_notes_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM notes")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_note_by_id_db(note_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM notes WHERE id=%s", (note_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_note_db(note_id, title, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE notes SET title=%s, content=%s WHERE id=%s", (title, content, note_id))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def delete_note_db(note_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM notes WHERE id=%s", (note_id,))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
