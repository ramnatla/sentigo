#!/bin/sh
# Set environment variables
# Run 'source env_vars.sh' to execute this script

# Path to Google API Credentials auth.json file. Example: '/mnt/c/Users/.../PythonBackend/auth.json'
export GOOGLE_APPLICATION_CREDENTIALS='' # TODO: INSERT HERE

# Flask configuration
export FLASK_DEBUG='True'
export FLASK_APP='server.py'

# Email sender information
export EMAIL_SENDER='' # TODO: INSERT HERE
export EMAIL_PASSWORD='' # TODO: INSERT HERE

# Twitter API secrets
export TWITTER_CONSUMER_KEY='' # TODO: INSERT HERE
export TWITTER_CONSUMER_SECRET='' # TODO: INSERT HERE
export TWITTER_ACCESS_TOKEN_KEY='' # TODO: INSERT HERE
export TWITTER_ACCESS_TOKEN_SECRET='' # TODO: INSERT HERE

# Google Firebase configuration
export FIREBASE_API_KEY='' # TODO: INSERT HERE
export FIREBASE_AUTH_DOMAIN='' # TODO: INSERT HERE
export FIREBASE_DATABASE_URL='' # TODO: INSERT HERE
export FIREBASE_PROJECT_ID='' # TODO: INSERT HERE
export FIREBASE_STORAGE_BUCKET='' # TODO: INSERT HERE
export FIREBASE_SERVICE_ACCOUNT='./firebase-private-key.json'
export FIREBASE_MESSAGING_SENDER_ID='' # TODO: INSERT HERE
