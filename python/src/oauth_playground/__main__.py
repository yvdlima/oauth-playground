import logging

import uvicorn
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s%(reset)s:     %(name)s: %(message)s"
    )
)
logging.basicConfig(level="INFO", handlers=[handler])

uvicorn.run("oauth_playground:app", port=8080, reload=True)
