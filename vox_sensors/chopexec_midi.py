table = op('table_values')
callbacks = op('udpin_sensors_callbacks').module

def onValueChange(channel, sampleIndex, val, prev):
    channelName = channel.name
    try:
        match(channelName[0]):
            case 'a':  # button
                callbacks.updateSensor(channelName,  int(val > 0))
            case 'b':  # rotary
                callbacks.updateSensor(channelName, (val - 63) / 128)
            case 'c':  # distance
                callbacks.updateSensor(channelName, -1 if val == 127 else val / 126)
    except Exception as e:
        pass # ignore missing sensors
    return
