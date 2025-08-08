from doctest import debug


table = op('table_test')
callbacks = op('udpin_sensors_callbacks').module

def onOffToOn(channel, sampleIndex, val, prev):
    callbacks.updateSensor(
        table[1, 0].val, float(table[1, 1].val))


def onValueChange(channel, sampleIndex, val, prev):
    return
