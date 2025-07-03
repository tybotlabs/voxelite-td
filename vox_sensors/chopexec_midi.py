table = op('table_values')


def onValueChange(channel, sampleIndex, val, prev):
    channelName = channel.name
    match(channelName[0]):
        case 'a':  # button
            table[channelName, 'value'] = int(val > 0)
        case 'b':  # rotary
            table[channelName, 'value'] = -(val - 64) / 128 * 360
        case 'c':  # distance
            table[channelName, 'value'] = val / 127
    return
