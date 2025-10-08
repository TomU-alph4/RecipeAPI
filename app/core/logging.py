import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("RecipeAPI")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    "recipeapi.log", maxBytes=5*1024*1024, backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


