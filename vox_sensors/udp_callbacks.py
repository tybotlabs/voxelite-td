from email.mime import message
import json

table = op('table_values')


def onReceive(dat, rowIndex, message, byteData, peer):
    try:
        parsed = json.loads(message)
        if parsed['type'] != 'sensor':
            debug("Unknown message type:", parsed['type'])
            return
        payload = parsed['payload']
        id = payload['id']
        value = payload['value']

        match id[0]:
            case 'c':  # range: scale cm to 0-1 value or -1 for over limit range
                low, high, limit = 3, 63, 80
                cm = value
                if cm > limit:
                    value = -1
                elif cm > high:
                    value = 1
                elif cm < low:
                    value = 0
                else:
                    value = (cm - low) / (high - low)

        updateSensor(id, value)
    except ValueError:
        debug("JSON error")


def updateSensor(id, value):
    table[id, 'value'] = value

