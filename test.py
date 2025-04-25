import sys 
import os
from subprocess import run
from rich.console import Console
import json
import questionary

def test():
    comando = f"gh auth status"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    return proceso

print(test())