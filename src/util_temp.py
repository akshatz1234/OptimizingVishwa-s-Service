import re

def pulseoxi(output):
    num = re.search("[0-9] [0-9]", out)
    print("HELLO")
    if num == "":
        return None
    else: 
        return main(num) 

def main(output):
    return ("temperature=", output)