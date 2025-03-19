import os
import sys
import json
from datetime import datetime


def gate4(config):
    config["app"] = "Gate4"
    config["version"] = "1.0"
    config["debug_mode"] = False
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
