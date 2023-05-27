import logging


class Logging:
    @staticmethod
    def get_logger(name: str):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # set formatter
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        ch.setFormatter(formatter)


        logger.addHandler(ch)

        return logger
