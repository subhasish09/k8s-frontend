from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Define the backend URL (adjust the URL as needed)
backend_url = "http://backend-service:6000"  # The service name defined in Kubernetes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    message = request.form.get('message', '')

    # Send a request to the backend API
    response = requests.post(f"{backend_url}/send", data={"message": message})

    if response.status_code == 200:
        return f"Frontend sent: {message}<br>Backend response: {response.text}"
    else:
        return "Error communicating with the backend."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
