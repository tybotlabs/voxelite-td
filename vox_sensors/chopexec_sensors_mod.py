

table = op('table_values')


def onOffToOn(channel, sampleIndex, val, prev):
    return


def whileOn(channel, sampleIndex, val, prev):
    return


def onOnToOff(channel, sampleIndex, val, prev):
    return


def whileOff(channel, sampleIndex, val, prev):
    return


def onValueChange(channel, sampleIndex, val, prev):

    match channel.name[0]:
        case 'b':
            modePar = parent().par[channel.name.title() + 'mode'].val
            rangeMinPar = parent().par[channel.name.title() + 'range1'].val
            rangeMaxPar = parent().par[channel.name.title() + 'range2'].val

            # limit
            change = val - table[channel.name, 'raw']
            next = table[channel.name, 'limit'] + change
            table[channel.name, 'limit'] = min(
                rangeMaxPar, max(rangeMinPar, next))

            # loop
            looped = (val - 0.5) % 1 - 0.5
            table[channel.name, 'loop'] = 0.5 if looped == -0.5 else looped

            # raw
            table[channel.name, 'raw'] = val

            # active
            table[channel.name, 'active'] = table[channel.name, modePar]
        case 'c':
            default = parent().par[channel.name.title() + 'default'].val

            # raw
            table[channel.name, 'raw'] = val

            # active
            table[channel.name, 'active'] = val if val != -1 else default

    return
