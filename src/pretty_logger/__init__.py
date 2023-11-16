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
from typing import Mapping

import sys
import re

import logging
from logging import *  # noqa: F401, F403 This is needed to replace logging imports
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


####################################################################################################
# New logging levels
####################################################################################################
RAW_LOG = logging.INFO + 1
SUCCESS = RAW_LOG + 1
VERBOSE = logging.INFO - 1

logging.addLevelName(VERBOSE, "VERBOSE")
logging.addLevelName(RAW_LOG, "RAW")
logging.addLevelName(SUCCESS, "SUCCESS")

if sys.version_info[1] > 7:  # Python 3.8+
  def raw(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message without any additional information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        stacklevel (int, optional): The stack level. Defaults to 1.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      RAW_LOG,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      stacklevel=stacklevel,
      extra=extra
    )

  def verbose(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message using "VERBOSE" information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        stacklevel (int, optional): The stack level. Defaults to 1.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      VERBOSE,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      stacklevel=stacklevel,
      extra=extra
    )

  def success(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message using "SUCCESS" information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        stacklevel (int, optional): The stack level. Defaults to 1.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      SUCCESS,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      stacklevel=stacklevel,
      extra=extra
    )

else:  # Python 3.7 and below
  def raw(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message without any additional information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      RAW_LOG,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      extra=extra
    )

  def verbose(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message using "VERBOSE" information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      VERBOSE,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      extra=extra
    )

  def success(
        msg: object,
        *args: object,
        exc_info: logging._ExcInfoType = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None
      ) -> None:
    """Logs the output fo the message using "SUCCESS" information

    Args:
        msg (object): The message to log
        *args (object): The arguments to pass to the message
        exc_info (logging._ExcInfoType, optional): The exception information. Defaults to None.
        stack_info (bool, optional): Whether to include stack information. Defaults to False.
        extra (Mapping[str, object], optional): Any extra information to log. Defaults to None.
    """
    logging.log(
      SUCCESS,
      msg,
      *args,
      exc_info=exc_info,
      stack_info=stack_info,
      extra=extra
    )


####################################################################################################
# New logging functions
####################################################################################################
def success_banner(msg: str):
  """Logs the output of the message using "SUCCESS" information with
  raw bars above and below

  Args:
      msg (str): The message to log
  """
  raw("=" * (len(msg) + 40))
  success(msg)
  raw("=" * (len(msg) + 40))


####################################################################################################
# New logging formatters
####################################################################################################
class SimpleFormatter(logging.Formatter):
  """A simple formatter which does not add color to the logging messages.
  Mainly used as the formatter for file outputs
  """

  def format(self, record: logging.LogRecord) -> str:
      if record.levelno != RAW_LOG:
        return super().format(record)

      return record.getMessage()


class PrettyFormatter(SimpleFormatter):
  """A formatter which adds color to the different log levels"""

  GREY = "\x1b[38;10m"
  BLUE = "\x1b[34;10m"
  PURPLE = "\x1b[95;10m"
  GREEN = "\x1b[36;10m"
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
    elif record.levelno != RAW_LOG:
      return super().format(record)

    return record.getMessage()


####################################################################################################
# Helper functions
####################################################################################################
def _strip_ansi_escape(txt: str) -> str:
  ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
  return ansi_escape.sub('', txt)
