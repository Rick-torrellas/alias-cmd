import sys 
import os
from subprocess import run
from rich.console import Console
import json
import questionary

pregunta = questionary.select(
    "What do you want to do?",
    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
).ask()

print(pregunta)