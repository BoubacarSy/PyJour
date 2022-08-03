import logging
from os import lseek

logging.basicConfig(level=logging.DEBUG,filename="s.log",filemode="a",
                format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Le fichier est bien execute")
logging.info("Message d'information")
logging.warning("ATTENTION!!!")
logging.error("ERREUR!!!")
logging.critical("CRITIQUE")
