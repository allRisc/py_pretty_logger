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

from logging import log, addLevelName, INFO
from logging import *  # noqa: F403, F401 This is needed to replace logging imports

RAW_LOG = INFO + 1
SUCCESS = RAW_LOG + 1

addLevelName(RAW_LOG, "RAW")
addLevelName(SUCCESS, "SUCCESS")


def raw(msg: str):
  """Logs the output fo the message without any additional information

  Args:
      msg (str): The message to log
  """
  log(RAW_LOG, msg)


def success(msg: str):
  """Logs the output fo the message using "SUCCESS" information

  Args:
      msg (str): The message to log
  """
  log(SUCCESS, msg)


def success_banner(msg: str):
  """Logs the output of the message using "SUCCESS" information with
  raw bars above and below

  Args:
      msg (str): The message to log
  """
  raw("=" * (len(msg) + 40))
  success(msg)
  raw("=" * (len(msg) + 40))
