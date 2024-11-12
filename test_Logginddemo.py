import logging

def test_logdemo():
    logger=logging.getLogger(__name__)
    fl=logging.FileHandler("logfile.log")
    fr=logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fl.setFormatter(fr)
    logger.addHandler(fl)
    logger.setLevel(logging.INFO)
    logger.debug("this is a debug block")
    logger.info("this is an info block")
    logger.error("these are error block")
    logger.warning("this is a waring block")
    logger.critical("this is critical block")