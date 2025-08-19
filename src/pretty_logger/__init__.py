#####################################################################################
# A package which makes python logging prettier
# Copyright (C) 2023  Benjamin Davis
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; If not, see <https://www.gnu.org/licenses/>.
#####################################################################################

from __future__ import annotations

import copy
import logging
import re
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from typing import Any

####################################################################################################
# New logging levels
####################################################################################################
RAW_LOG = logging.INFO + 1
SUCCESS = RAW_LOG + 1
VERBOSE = logging.INFO - 1

logging.addLevelName(VERBOSE, "VERBOSE")
logging.addLevelName(RAW_LOG, "RAW")
logging.addLevelName(SUCCESS, "SUCCESS")


####################################################################################################
# Get a ExtendedLogger
####################################################################################################
def getLogger(lname: str) -> ExtendedLogger:
  logging.setLoggerClass(ExtendedLogger)

  logger = logging.getLogger(lname)

  if not isinstance(logger, ExtendedLogger):
    raise RuntimeError("Logger is not an instance of ExtendedLogger")

  return logger


####################################################################################################
# Extended Logging
####################################################################################################
class ExtendedLogger(logging.Logger):

  def verbose(self, msg: Any, *args, **kwargs) -> None:
    """Logs a message with level VERBOSE on this logger.
    The arguements are interpretted as for debug()
    """
    self.log(VERBOSE, msg, *args, **kwargs)

  def raw(self, msg: Any, *args, **kwargs) -> None:
    """Logs a message with level RAW_LOG on this logger.
    The arguements are interpretted as for debug()
    """
    self.log(RAW_LOG, msg, *args, **kwargs)

  def success(self, msg: Any, *args, **kwargs) -> None:
    """Logs a message with level SUCCESS on this logger.
    The arguements are interpretted as for debug()
    """
    self.log(SUCCESS, msg, *args, **kwargs)

  def success_banner(self, msg: str):
    """Logs the output of the message using "SUCCESS" information with
    raw bars above and below

    Args:
        msg (str): The message to log
    """
    self.raw("=" * (len(msg) + 40))
    self.success(msg)
    self.raw("=" * (len(msg) + 40))


####################################################################################################
# New logging formatters
####################################################################################################
class ExtendedFormatter(logging.Formatter):
  """A simple formatter which does not add color to the logging messages.
  Mainly used as the formatter for file outputs
  """

  def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: logging._FormatStyle = "%",
        strip: bool = False,
        **kwargs
      ):
    super().__init__(fmt, datefmt, style, **kwargs)
    self.strip: bool = strip

  def format(self, record: logging.LogRecord) -> str:
      if self.strip:
        record = copy.deepcopy(record)
        record.msg = _strip_ansi_escape(record.msg)

      if record.levelno != RAW_LOG:
        return super().format(record)

      return record.getMessage()


class ColoredFormatter(ExtendedFormatter):
  """A formatter which adds color to the different log levels"""

  GREY = "\x1b[38;10m"
  BLUE = "\x1b[34;10m"
  PURPLE = "\x1b[95;10m"
  GREEN = "\x1b[32;10m"
  YELLOW = "\x1b[33;10m"
  RED = "\x1b[31;10m"
  BOLD_RED = "\x1b[31;1m"
  RESET = "\x1b[0m"

  COLORS = {
      DEBUG: PURPLE,
      VERBOSE: BLUE,
      INFO: GREY,
      SUCCESS: GREEN,
      WARNING: YELLOW,
      ERROR: RED,
      CRITICAL: BOLD_RED
  }

  def format(self, record: logging.LogRecord) -> str:
    if record.levelno in self.COLORS:
      return self.COLORS[record.levelno] + super().format(record) + self.RESET

    return super().format(record)


####################################################################################################
# Helper functions
####################################################################################################
def _strip_ansi_escape(txt: str) -> str:
  ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
  return ansi_escape.sub('', txt)
