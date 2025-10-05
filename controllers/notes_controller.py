# controllers/notes_controller.py
from flask import jsonify, request
from models.notes_model import add_note_to_db, get_all_notes_from_db, get_note_by_id_db, update_note_db, delete_note_db

def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({'error':'Title and content are required'}), 400
    try:
        note_id = add_note_to_db(title, content)
        return jsonify({'message':'Note added successfully', 'id': note_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_all_notes():
    try:
        notes = get_all_notes_from_db()
        return jsonify(notes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_note_by_id(note_id):
    try:
        note = get_note_by_id_db(note_id)
        if note:
            return jsonify(note)
        else:
            return jsonify({'error':'Note not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_note(note_id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    try:
        rowcount = update_note_db(note_id, title, content)
        if rowcount == 0:
            return jsonify({'error':'Note not found'}), 404
        return jsonify({'message':'Note updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def delete_note(note_id):
    try:
        rowcount = delete_note_db(note_id)
        if rowcount == 0:
            return jsonify({'error':'Note not found'}), 404
        return jsonify({'message':'Note deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
