from flask import Blueprint, request, jsonify
from .models import db, Email
import joblib
from flask_cors import cross_origin


main = Blueprint('main', __name__)

# route that only returns hello world + avoid cors error
@main.route('/categorize', methods=['POST'])
@cross_origin()
def categorize_email():
    return jsonify({'category': 'Hello World!'})

# Load pre-trained model
#model = joblib.load('email_categorizer_model.pkl')

#@main.route('/categorize', methods=['POST'])
#def categorize_email():
#    data = request.get_json()
#    email_text = data['text']
#    prediction = model.predict([email_text])[0]

    # Save email to the database
#    new_email = Email(text=email_text, category=prediction)
#    db.session.add(new_email)
#    db.session.commit()

#    return jsonify({'category': prediction})
