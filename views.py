from flask import Blueprint, jsonify, request
from models import db, Candidate, Vote

api = Blueprint('api', __name__)

# Route to get all candidates
@api.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in candidates])

# Route to vote for a candidate
@api.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    candidate_id = data.get('candidate_id')
    if not candidate_id:
        return jsonify({"error": "No candidate selected"}), 400
    
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found"}), 404
    
    # Record the vote
    vote = Vote(candidate_id=candidate.id)
    db.session.add(vote)
    db.session.commit()
    
    return jsonify({"message": "Vote recorded successfully!"}), 201

# Route to get voting results
@api.route('/results', methods=['GET'])
def results():
    results = db.session.query(Candidate.name, db.func.count(Vote.id)).join(Vote).group_by(Candidate.id).all()
    return jsonify(results)
