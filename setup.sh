#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the Phi-3 model
ollama pull phi3

# Create necessary directories
mkdir -p logs

echo "Setup complete. Don't forget to copy .env.example to .env and fill in your ngrok authtoken."