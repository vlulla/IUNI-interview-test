##
##
## Author: Vijay Lulla
## Date: 
##
import re,os,sys,datetime,typing
import hypothesis as hy, hypothesis.strategies as st

def parseLogLine(line : str) -> dict:
    log = {}
    cols = re.split('[\s"]+', line)

    log['datetime'] = f"{cols[0]} {cols[1]}"
    log['logName'] = f"{cols[2]}"
    log['logLevel'] = f"{cols[3]}"
    assert log['logLevel'].upper() in ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
    log['ID'] = f"{cols[4]}"
    log['msg'] = f"{' '.join(cols[5:])}".strip()

    return log

def getLogLines(fname : str) -> typing.List[str]:
    with open(fname) as fd:
        dat = fd.read()
    return [l for l in dat.split("\n") if l != '']

def main(fname : str) -> None:
    lines = getLogLines(fname)
    print(parseLogLine(lines[0]))

if __name__ == "__main__":
    main("api.log")
