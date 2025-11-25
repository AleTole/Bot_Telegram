# config.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# TOKEN: quitar espacios/comillas y validar
TOKEN = os.getenv("TOKEN")
if TOKEN:
    TOKEN = TOKEN.strip().strip('"').strip("'")
else:
    TOKEN = None
    logger.warning("TOKEN no encontrado en entorno. No inicies en producción sin TOKEN.")

# CONTROL: forzar o relajar comprobaciones en entorno
ENFORCE_TOKEN = os.getenv("ENFORCE_TOKEN", "false").lower() in {"1", "true", "yes"}
ENABLE_WHITELIST = os.getenv("ENABLE_WHITELIST", "false").lower() in {"1", "true", "yes"}

# WHITELIST: empty → abierto a todos (None). Si se configura, convertir a set[int]
raw_wl = os.getenv("WHITELIST", "").strip()
if not ENABLE_WHITELIST:
    WHITELIST = None
    logger.info("Whitelist desactivada (ENABLE_WHITELIST=false).")
else:
    if raw_wl == "":
        WHITELIST = set()
        logger.info("Whitelist activada pero vacía (ningún usuario autorizado).")
    else:
        ids = []
        for part in raw_wl.replace(" ", "").split(","):
            if part == "":
                continue
            try:
                ids.append(int(part))
            except ValueError:
                logger.warning("ID no válido en WHITELIST: %r (se ignora)", part)
        WHITELIST = set(ids)
        logger.info("Whitelist cargada con %d ids.", len(WHITELIST))

# Seguridad en entorno: si ENFORCE_TOKEN es True y no hay TOKEN, terminar en prod (quien ejecute decide)
if ENFORCE_TOKEN and not TOKEN:
    logger.error("ENFORCE_TOKEN=true y no hay TOKEN. Deteniendo inicialización.")
    raise RuntimeError("TOKEN requerido por ENFORCE_TOKEN pero no encontrado.")
