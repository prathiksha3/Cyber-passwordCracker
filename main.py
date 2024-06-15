from flask import Flask, render_template, request, jsonify
import random
import pyautogui
from cryptography.fernet import Fernet

app = Flask(__name__)

# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

@app.route('/')
def hh():
    return render_template('hh.html')

@app.route('/nextpage')
def nextpage():
    return render_template('nextpage.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/guess_password', methods=['POST'])
def guess_password():
    data = request.json
    password = data['password']
    attempts = random.randint(1, 100)  # Simulate attempts
    # Your password guessing logic here
    return jsonify(password=password, attempts=attempts)

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message_route():
    data = request.json
    key = generate_key()
    message = data['message']
    encrypted_message = encrypt_message(key, message)
    return jsonify(key=key.decode(), encrypted_message=encrypted_message.decode())

@app.route('/decrypt_message', methods=['POST'])
def decrypt_message_route():
    data = request.json
    key = data['key'].encode()
    encrypted_message = data['encrypted_message'].encode()
    decrypted_message = decrypt_message(key, encrypted_message)
    return jsonify(decrypted_message=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True)
