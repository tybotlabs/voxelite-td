import random


def onValueChange(par, prev):
    centerpieceHeight = 40
    parModule = parent().par.Module
    parStations = parent().par.Stations
    parJitter = 0.15 if parent().par.Jitter else 0.0
    parMask = parent().par.Mask

    # stabilize random seed
    random.seed(0)

    # set masks and background
    op('hex').bypass = not parMask

    op('quadrant').bypass = parModule == '*' or not parMask
    match parModule:
        case '0':
            op('transform_quadrant').par.rotate = 0
        case '1':
            op('transform_quadrant').par.rotate = 90
        case '2':
            op('transform_quadrant').par.rotate = 180
        case '3':
            op('transform_quadrant').par.rotate = 270

    # build pixel table
    t = op('table_pixels')
    t.clear()
    t.appendRow(['P(0)', 'P(1)', 'P(2)', 'show'])
    for y in range(0, centerpieceHeight):  # Y
        for z in range(0, 26):  # Z: 26
            for x in range(0, 26):  # X: 26
                show = 1

                if z in [25, 0]:
                    show = 0
                elif z in [24, 23, 1, 2]:
                    if x < 5 or x > 20:
                        show = 0
                elif z in [22, 21, 3, 4]:
                    if x < 4 or x > 21:
                        show = 0
                elif z in [20, 19, 5, 6]:
                    if x < 3 or x > 22:
                        show = 0
                elif z in [18, 17, 7, 8]:
                    if x < 2 or x > 23:
                        show = 0
                elif z in [16, 15, 9, 10]:
                    if x < 1 or x > 24:
                        show = 0

                if parModule == '0' or parModule == '1':
                    if z > 12.5:
                        show = 0
                elif parModule == '2' or parModule == '3':
                    if z < 12.5:
                        show = 0

                if parModule == '0' or parModule == '3':
                    if x > 12.5:
                        show = 0
                elif parModule == '1' or parModule == '2':
                    if x < 12.5:
                        show = 0

                t.appendRow([x - 12.5 + random.uniform(-parJitter, parJitter), y - (centerpieceHeight / 2 - 0.5) +
                            random.uniform(-parJitter, parJitter) / 2, z - 12.5 + random.uniform(-parJitter, parJitter), show])

    # BUILD STATIONS

    stationRotations = [240, 0, 120]

    # LED strips

    stripHeight = 16
    ledHeight = 0.05
    baseHeight = 0.05
    stationsRadius = 2
    stripXZoffsets = [[-0.2, -0.3], [0, 0], [0.2, -0.3]]

    t = op('table_strips')
    t.clear()
    t.appendRow(['P(0)', 'P(1)', 'P(2)', 'rotation'])

    for i in range(stripHeight):
        for r in stationRotations:
            for [x, z] in stripXZoffsets:
                t.appendRow(
                    [x, baseHeight + i * ledHeight, stationsRadius + z, r])

    op('add_stations').bypass = not parStations
    op('constant_res').par.resolutionh = 1040 + \
        (stripHeight if parStations else 0)

    # speakers

    speakerHeight = 0.35
    t = op('table_speakers')
    t.clear()
    t.appendRow(['P(0)', 'P(1)', 'P(2)', 'rotation'])

    for r in stationRotations:
        t.appendRow([0, speakerHeight, stationsRadius - 0.3, r])

    # set stations visibility
    op('geo_stations').display = parStations
    op('geo_speakers').display = parStations
    op('geo_station_labels').display = parStations
    op('geo_sensors').display = parStations

    return
