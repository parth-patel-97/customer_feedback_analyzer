import os
from dotenv import load_dotenv

load_dotenv()


def load_config():
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    return GOOGLE_API_KEY


loaded_config = load_config()