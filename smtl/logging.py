import logging
from config import run_config


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

level = logging.DEBUG if run_config.get('DEBUG', False) else logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(level)
