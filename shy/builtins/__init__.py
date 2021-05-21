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
