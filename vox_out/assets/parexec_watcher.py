import random

height = 40

def onValueChange(par, prev):
		parModule = parent().par.Module
		parJitter = 0.15 if parent().par.Jitter else 0.0
		parMask = parent().par.Mask
		parFill = parent().par.Fill

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

		op('over_bg').bypass = not parFill

		# build pixel table
		t = op('table_pixels')
		t.clear()
		t.appendRow(['P(0)', 'P(1)',	'P(2)',	'show'])
		for y in range(0, height):  # Y
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

								t.appendRow([x - 12.5 + random.uniform(-parJitter, parJitter), y - (height / 2 - 0.5) + random.uniform(-parJitter, parJitter) / 2, z - 12.5 + random.uniform(-parJitter, parJitter), show])
		


		return