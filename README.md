# Ollama LiteLLM Proxy

This project sets up a proxy server using Ollama and LiteLLM to serve language models.

## Prerequisites

- Python 3.7+
- pip
- ngrok account and authtoken

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/ollama-litellm-proxy.git
cd ollama-litellm-proxy
Copy
2. Run the setup script:
./setup.sh
Copy
3. Copy the `.env.example` file to `.env` and fill in your ngrok authtoken:
cp .env.example .env
Copy
## Usage

Run the main script:
python src/main.py
Copy
The script will set up Ollama, start the LiteLLM proxy, and create ngrok tunnels for both the LiteLLM proxy and the Flask app.

## Configuration

- Modify `config/litellm_config.yaml` to change the LiteLLM configuration.
- Modify `config/logging_config.yaml` to change the logging configuration.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

