table = op('table_values')


def onPulse(par):
    for (rowIndex, target) in enumerate(table.col('value')):
        if not rowIndex:
            continue  # Skip the header row
        table[rowIndex, 'value'] = table[rowIndex, 'default']
    return
