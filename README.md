# MHacks12

Pre-requisites
1. Edit env_vars.sh and add your own API keys, configuration settings, etc
2. Create auth.json in PythonBackend to store your Google API Credentials
    - Format Example: 
    {
        "type": "service_account",
        "project_id": "neat...",
        "private_key_id": "9d8...",
        "private_key": "-----BEGIN PRIVATE +AOf...",
        "client_email": "doritos-lap...",
        "client_id": "11063...",
        "auth_uri": "https://accounts...",
        "token_uri": "https://oauth2...",
        "auth_provider_x509_cert_url": "https://www.googleapis...",
        "client_x509_cert_url": "https://www.googleapis..."
    }
3. Create firebase-private-key.json in PythonBackend to store your Firebase private key
    - Format Example:
    {
        "type": "service_account",
        "project_id": "mhacks...",
        "private_key_id": "39b...",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMII...",
        "client_email": "firebase-admi...",
        "client_id": "10778...",
        "auth_uri": "https://accounts...",
        "token_uri": "https://oauth2...",
        "auth_provider_x509_cert_url": "https://www.googleapis...",
        "client_x509_cert_url": "https://www.googleapis..."
    }



To start front-end:
1. cd frontend
2. npm install
3. npm start

To run backend:
1. cd PythonBackend
2. source env_vars.sh
3. flask run --host 0.0.0.0 --port 5000