import os
import subprocess
import time
import logging

logger = logging.getLogger(__name__)

def install_ollama():
    logger.info("Installing Ollama...")
    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)

def run_ollama():
    logger.info("Starting Ollama server...")
    os.environ["OLLAMA_HOST"] = "0.0.0.0:11434"
    os.environ["OLLAMA_ORIGINS"] = "http://0.0.0.0:*"
    cmd = "ollama serve"
    with open(os.devnull, 'wb') as devnull:
        subprocess.Popen(cmd, shell=True, stdout=devnull, stderr=devnull)
    time.sleep(10)  # Give Ollama some time to start

def install_model():
    logger.info("Installing Phi-3 model...")
    subprocess.run("ollama pull phi3", shell=True, check=True)