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

import pretty_logger.full_logger as logging

import re


def strip_ansi_escape(txt: str) -> str:
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', txt)


class SimpleFormatter(logging.Formatter):
    """A simple formatter which does not add color to the logging messages.
    Mainly used as the formatter for file outputs
    """

    format_str = "%(levelname)s:%(asctime)s - %(message)s"

    FORMATS = {
        logging.DEBUG: format_str,
        logging.INFO: format_str,
        logging.SUCCESS: format_str,
        logging.WARNING: format_str,
        logging.ERROR: format_str,
        logging.CRITICAL: format_str
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return strip_ansi_escape(formatter.format(record))



class PrettyFormatter(SimpleFormatter):
    """A formatter which adds color to the different log levels"""

    grey = "\x1b[38;20m"
    green = "\x1b[32;10m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + SimpleFormatter.format_str + reset,
        logging.INFO: grey + SimpleFormatter.format_str + reset,
        logging.SUCCESS: green + SimpleFormatter.format_str + reset,
        logging.WARNING: yellow + SimpleFormatter.format_str + reset,
        logging.ERROR: red + SimpleFormatter.format_str + reset,
        logging.CRITICAL: bold_red + SimpleFormatter.format_str + reset
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
