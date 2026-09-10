from flask import Flask, jsonify

app = Flask(__name__)


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
