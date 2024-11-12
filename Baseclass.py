import logging


class Baseclass1:
    def test_logdemo1(self):
        logger = logging.getLogger(__name__)
        fl = logging.FileHandler("logfile.log")
        fr = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fl.setFormatter(fr)
        logger.addHandler(fl)
        logger.setLevel(logging.INFO)
        return logger
