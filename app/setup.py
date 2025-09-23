import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_EMAIL = os.environ.get("ADMIN_USEREMAIL")
ADMIN_PASS  = os.environ.get("ADMIN_PASSWORD")
JWT_SECRET = os.environ.get("JWT_SECRET")
