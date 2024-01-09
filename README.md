# Braintree Basic Server Python

This repository demonstrates a basic integration of Braintree payment gateway with a Flask web application. It includes a simple frontend with a form to input a payment nonce and submit it to the server.


### Prerequisites

- Python installed
- Braintree Sandbox Account for testing

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/braintree-flask-integration.git

cd braintree-flask-integration
```

2. Install the required Python packages:
```bash
pip install Flask braintree
```

3. Configure Braintree:
* Obtain your Braintree merchant ID, public key, and private key from your Braintree Sandbox Account.
* Create a `config.py` file with your Braintree credentials.

4. Run the Flask application:
```bash
python main.py
```

5. Access the application in your browser:
```bash
http://127.0.0.1:5000/
```

## Directory Structure
```bash
/braintree-flask-integration
    /templates
        index.html
    main.py
    config.py
```

* **/templates**: Contains HTML templates.
* **main.py**: Flask application code.
* **config.py**: Configuration file for Braintree credentials.
* **tailwind.css**: Tailwind CSS configuration file.


## Usage
1. Open your web browser and navigate to http://127.0.0.1:5000/
2. Enter a payment nonce in the form and click "Submit."