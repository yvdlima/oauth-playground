import logging
import colorlog

from blacksheep.server import Application
from blacksheep.server.templating import use_templates
from blacksheep.sessions.crypto import FernetEncryptor
from jinja2 import PackageLoader

from dotenv import load_dotenv

load_dotenv()

# Usually this should be on __main__ but unicorn starts a new proc of the app
# and the logger config is lost when the webserver actually starts...
if __name__ != "__main__":
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)s%(reset)s:     %(name)s: %(message)s"
        )
    )
    logging.basicConfig(level="INFO", handlers=[handler])

app = Application()

# Generated with cryptography.fernet.Fernet.generate_key(), in a real app the session encryption key and secret key should not be hardcoded
encryption_key = b"WYvG4pE-bkmfKWYRHF4R_p4YoK1pkdMtHlaMRaS7vwE="
app.use_sessions(
    "a_totally_insecure_signing_key", encryptor=FernetEncryptor(encryption_key)
)

use_templates(app, loader=PackageLoader("oauth_playground", "views"), enable_async=True)

from .services.oauth import OAuthService

app.services.add_exact_singleton(OAuthService)

from . import controllers
