import subprocess
import logging

logger = logging.getLogger(__name__)

def start_litellm_proxy():
    logger.info("Starting LiteLLM proxy...")
    return subprocess.Popen(
        ["litellm", "--config", "config/litellm_config.yaml", "--debug", "--add_function_to_prompt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )