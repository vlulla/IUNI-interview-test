import re,os,sys,datetime,typing

def parseLogLine(line : str) -> dict:
    """Parses a log line"""
    log = {}
    cols = re.split('[\s"]+', line)

    log['datetime'] = f"{cols[0]} {cols[1]}".replace(",",".")
    log['datetime'] = datetime.datetime.strptime(log['datetime'], "%Y-%m-%d %H:%M:%S.%f")
    log['logName'] = f"{cols[2]}"
    log['logLevel'] = f"{cols[3]}"
    assert log['logLevel'].upper() in ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
    log['ID'] = f"{cols[4]}"
    log['msg'] = f"{' '.join(cols[5:])}".strip()

    return log

def getLogLines(logFilename : str) -> typing.List[str]:
    """Read all the lines from the log file"""
    with open(logFilename) as fd:
        dat = fd.read()
    return [l for l in dat.split("\n") if l != '']

def consolidateEvents(parsedLogLines : typing.List[dict]) -> dict:
    """Consolidate events into the required format"""
    events = {}
    for pl in parsedLogLines:
        logid, logtime, logmsg = pl['ID'], pl['datetime'], pl['msg']
        if logid in events:
            if logtime < events[logid]['starttime']:
                events[logid]['startime'] = logtime
                events[logid]['startmsg'] = logmsg
            if logtime > events[logid]['endtime']:
                events[logid]['endtime'] = logtime
                events[logid]['endmsg'] = logmsg
        else:
            events[logid] = {}
            events[logid]['starttime'] = events[logid]['endtime'] = logtime
            events[logid]['startmsg'] = events[logid]['endmsg'] = logmsg
    return events

def timediff(starttime : datetime.datetime, endtime : datetime.datetime) -> float:
    """Calculate Time Diff column"""
    diff = (endtime - starttime)
    return diff/datetime.timedelta(minutes=1)

def main(logFilename : str) -> None:
    """Run the main program"""
    lines = getLogLines(logFilename)
    parsedLines = [parseLogLine(l) for l in lines]
    events = consolidateEvents(parsedLines)

    print("Log message,Start Time,End Time,Time Diff")
    for id, vals in events.items():
        starttime,startmsg,endtime,endmsg = vals['starttime'], vals['startmsg'], vals['endtime'], vals['endmsg']
        print(f'"{startmsg} - {endmsg}",{starttime},{endtime},{round(timediff(starttime, endtime), 5)}')

if __name__ == "__main__":
    main("api.log")
