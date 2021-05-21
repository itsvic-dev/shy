"""
    Shell + Python = Shy.
    Copyright (C) 2021 omame

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import typing
from . import exit
import shy

registered_builtins = {}


def register_builtin(builtin_name: str, builtin_function: typing.Callable):
    if builtin_name in registered_builtins.keys():
        raise shy.exceptions.BuiltinAlreadyRegisteredException(builtin_name)
    registered_builtins.update({builtin_name: builtin_function})


def register_default_builtins():
    register_builtin("exit", exit.builtin_exit)
