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
import sys
import argparse
import subprocess
import shlex

parser = argparse.ArgumentParser(description=shy.__description__)
parser.add_argument("-v", "--version", action="version", version=f"shy {shy.__version__}")


def main():
    parser.parse_args()

    shy.builtins.register_default_builtins()
    env = os.environ.copy()
    env["PS1"] = shy.defaults.PS1
    env["SHELL"] = os.path.abspath(sys.argv[0])
    last_status_code = 0

    while True:
        try:
            raw_string = input(shy.helpers.expand_ps(env["PS1"]))
        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            sys.exit(last_status_code)
        args = shlex.split(raw_string, comments=True)
        if len(args) == 0:
            continue

        command = args.pop(0)

        builtin = shy.helpers.get_builtin(command)
        if builtin:
            try:
                builtin(*args)
                last_status_code = 0
            except shy.exceptions.ShyException as e:
                print(f"shy: {e}")
                last_status_code = 1
            except SystemExit as e:
                sys.exit(e.code)
            except BaseException as e:
                print(f"(Python exception) shy: {e}", file=sys.stderr)
                last_status_code = 2
        else:
            try:
                process = subprocess.run([command, *args], env=env)
                last_status_code = process.returncode
            except FileNotFoundError as e:
                print(f"shy: {e.filename}: no such file or directory")
        if last_status_code != 0:
            print("shy: command returned with status code =", last_status_code)
