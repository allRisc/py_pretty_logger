import pretty_logger as logging


def test_import():
  logger = logging.getLogger("test_import")

  logger.raw("raw")

  logger.debug("debug")
