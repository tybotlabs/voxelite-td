audiodevs = op('audiodevs1')

def onStart():
	audiodevs.par.refresh.pulse()
	# debug(op('audiodevout_usb1').par.device)
	for row_index in range(audiodevs.numRows):
		if 'Headphones' in audiodevs[row_index, 'label'].val:
			op('audiodevout_headphone').par.device = audiodevs[row_index, 'name']
		if 'USB' in audiodevs[row_index, 'label'].val:
			op('audiodevout_usb1').par.device = audiodevs[row_index, 'name']
