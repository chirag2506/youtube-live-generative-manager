from logger import putlog
import json
import os
from helpers.youtubeFunctionalities.schemas import Message

log = putlog(__file__)

def readFile(filename):
    content = ""

    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as Err:
        log.error("{}".format(Err))

    return content

def readJson(filename):
    content = {}

    try:
        content = json.loads(readFile(filename))
    except Exception as Err:
        log.error("{}".format(Err),exc_info=True)

    return content

def writeFile(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    status = "success"
    try:
        with open(filename, 'w') as fileSource:
            fileSource.write(content)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "failed"

    return status

def writeJson(filename, content):
    status = "Success"

    try:
        contentDump = json.dumps(content, indent=4, sort_keys=True)
        writeFile(filename, contentDump)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "Failed"

    return status

configFile = "config/app.setting.json"
configuration = readJson(configFile)

def respondToChat(message: Message):
    command = message.text.split(" ")[0][1:]
    if(command.lower() == "about".lower()):
        True
    return