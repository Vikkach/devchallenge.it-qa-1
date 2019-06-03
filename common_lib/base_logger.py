import logging
import datetime


class BaseLogger:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    @classmethod
    def get_info_log(cls, message):
        log = f'{str(datetime.datetime.utcnow())}: {message}'
        print(log)
        return cls.logger.info(log)
