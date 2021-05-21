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
