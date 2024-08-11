import logging
import time
from pyngrok import ngrok
from dependencies import install_dependencies
from ollama import install_ollama, run_ollama, install_model
from litellm_proxy import start_litellm_proxy
from flask_app import run_flask_app
import logging.config
import yaml

# Load logging configuration
with open('config/logging_config.yaml', 'r') as f:
    logging_config = yaml.safe_load(f)
    logging.config.dictConfig(logging_config)

logger = logging.getLogger(__name__)

def main():
    install_dependencies()
    install_ollama()
    run_ollama()
    install_model()
    
    # Start LiteLLM proxy
    litellm_process = start_litellm_proxy()
    
    # Give LiteLLM some time to start
    time.sleep(15)
    
    # Set up ngrok tunnels
    ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")  # Replace with your ngrok auth token
    litellm_tunnel = ngrok.connect(8000)
    flask_tunnel = ngrok.connect(5000)
    
    logger.info(f"LiteLLM proxy is accessible at: {litellm_tunnel.public_url}")
    logger.info(f"Flask app is accessible at: {flask_tunnel.public_url}")
    
    # Run Flask app in the main process
    run_flask_app()
    
    # Wait for the LiteLLM process to finish
    litellm_process.wait()

if __name__ == '__main__':
    main()
