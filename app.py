from flask import Flask, jsonify
from repository.database import db
from db_models.payment import Payment


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)


@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({'message': 'Payment PIX created successfully'}), 201

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_payment_confirmation():
    return jsonify({'message': 'PIX payment confirmed successfully'}), 200

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def get_payment_pix(payment_id):
    return jsonify({'payment_id': payment_id, 'status': 'completed'}), 200

if __name__ == '__main__':
    app.run(debug=True)
