import json

values = op('table_values')


def onReceive(dat, rowIndex, message, byteData, peer):
    try:
        parsed = json.loads(message)
        payload = parsed['payload']
        sensorId = payload['id']
        # ts = payload['ts'] # timestamp available but unused

        match parsed['type']:
            case 'sensor':
                match sensorId[0]:
                    case 'a':  # button: use direct value
                        value = payload['value']
                    case 'b':  # rotary: scale rotations to degrees
                        value = payload['value'] * 360.0
                    case 'c':  # range: scale cm to 0-1 value
                        low, high, limit = 3, 63, 80
                        cm = payload['value']
                        if cm > limit:
                            value = 1
                        elif cm > high:
                            value = 0.999
                        elif cm < low:
                            value = 0
                        else:
                            value = (cm - low) / (high - low)

                values[sensorId, 'value'] = value

    except ValueError:
        print("JSON error")
    return
