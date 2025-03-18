import os
import sys
import json
from datetime import datetime


def gate4():
    config = {
        "CYBERGATE": "Gate4",
        "VERSION": "1.0",
        "DEBUG_MODE": False,
        "SECRET_KEY_VAR_NAME": "secret_value",
        "STORED_IN_MEMORY": True
    }
    with open("calc_config.json", "w") as f:
        json.dump(config, f)
    print(f"Calculator v{config['version']} | {datetime.now().strftime('%Y-%m-%d')}")
    x = input("Enter x: ")
    op = input("Enter Operation [+,-,*,/]: ")
    y = input("Enter y: ")
    res = eval(f"{x} {op} {y}")
    print(f"Result: {res}")
    try:
        os.remove("calc_config.json")
    except:
        # .....
        ...
