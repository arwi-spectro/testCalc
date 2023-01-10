"""Invoke tasks"""
import platform
import shutil
from os import listdir
from time import sleep
from pathlib import Path

# The first time invoke is called, it is to install dependencies, so at that point rich is not
# installed yet
try:
    from rich import print as rprint
except ImportError:
    rprint = print
from invoke import task



@task(
    aliases=["test", "pytest"],
    help={
        "color": "Whether to display pytest output in color, 'yes' or 'no'",
        "verbose": "Makes the pytest output verbose",
        "s_no_capture": (
            "Prevents pytest from capturing output (making it possible to see prints etc.)"
        ),
        "k_only_run": (
            "Only run tests that matches the expression in STRING. See the help for pytest's `-k` "
            "option to read more about the options for expression"
        ),
        "x_exit_on_first_error": "Make pytest exit on first error",
    },
)
def tests(
    context,
    color="yes",
    verbose=False,
    s_no_capture=False,
    k_only_run=None,
    x_exit_on_first_error=False,
):
    """Run tests with pytest"""
    if platform.system() == "Windows":
        color = "no"
    args = []
    if verbose:
        args.append("--verbose")
    if s_no_capture:
        args.append("-s")
    if k_only_run:
        args.append(f"-k {k_only_run}")
    if x_exit_on_first_error:
        args.append("-x")
    rprint("\n[bold]Testing...")
    rprint("pytest {args[0]}")
    result = context.run(f"pytest {args[0]}")
    if result.return_code == 0:
        rprint("[bold green]All tests passed")
    return result.return_code

