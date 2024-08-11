import subprocess
import logging

logger = logging.getLogger(__name__)

def install_dependencies():
    logger.info("Installing dependencies...")
    subprocess.run("pip install litellm[proxy] pyyaml pyngrok", shell=True, check=True)