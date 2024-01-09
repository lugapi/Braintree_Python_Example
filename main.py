# main.py
from config import merchant_id, public_key, private_key
import braintree

from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='templates')

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      braintree.Environment.Sandbox,
      merchant_id=merchant_id,
      public_key=public_key,
      private_key=private_key
  )
)

# pass client_token to your front-end
client_token = gateway.client_token.generate({
    "customer_id": ""
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/get_client_token', methods=['GET'])
def get_client_token():
    client_token = gateway.client_token.generate()
    return render_template('client_token.html', client_token=client_token)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    nonce = request.json.get('nonce')
    result = gateway.transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce,
        "options": {
            "submit_for_settlement": True
        }
    })
    
    # print(result.transaction)
    transaction_details = vars(result.transaction)
    print(transaction_details)

    if result.is_success:
        return jsonify({'success': True, 'transactionId': result.transaction.id})
    else:
        return jsonify({'success': False, 'errorMessage': result.message})

if __name__ == '__main__':
    app.run(debug=True)