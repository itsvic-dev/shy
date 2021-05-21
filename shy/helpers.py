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

import shy
import os
import getpass
import socket
import typing


def get_builtin(command: str) -> typing.Callable or None:
    if command not in shy.builtins.registered_builtins.keys():
        return None
    return shy.builtins.registered_builtins[command]


def expand_ps(ps: str) -> str:
    ps = ps.replace("\\u", getpass.getuser())
    ps = ps.replace("\\h", socket.gethostname())
    ps = ps.replace("\\$", "#" if os.geteuid() == 0 else "$")
    current_dir = os.path.basename(os.getcwd())
    if os.getcwd() == os.path.expanduser("~"):
        current_dir = "~"
    ps = ps.replace("\\W", current_dir)
    return ps
