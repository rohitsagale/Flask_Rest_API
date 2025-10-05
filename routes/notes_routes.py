# routes/notes_routes.py
from flask import Blueprint
from controllers.notes_controller import add_note, get_all_notes, get_note_by_id, update_note, delete_note

notes_bp = Blueprint('notes_bp', __name__)

notes_bp.route('/notes', methods=['POST'])(add_note)
notes_bp.route('/notes', methods=['GET'])(get_all_notes)
notes_bp.route('/notes/<int:note_id>', methods=['GET'])(get_note_by_id)
notes_bp.route('/notes/<int:note_id>', methods=['PUT'])(update_note)
notes_bp.route('/notes/<int:note_id>', methods=['DELETE'])(delete_note)
