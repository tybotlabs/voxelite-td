out vec4 fragColor;

void main()
{

	uint x = int(gl_FragCoord.x);
	uint y = int(gl_FragCoord.y) / 26;
	uint z = int(gl_FragCoord.y) % 26;

	switch (z) {
		case 25:
		case 0:
			return;
			break;
		case 24:
		case 23:
		case 1:
		case 2:
			if (x < 5 || x > 20) return;
			break;
		case 22:
		case 21:
		case 3:
		case 4:
			if (x < 4 || x > 21) 	return;
			break;
		case 20:
		case 19:
		case 5:
		case 6:
			if (x < 3 || x > 22) return;
			break;
		case 18:
		case 17:
		case 7:
		case 8:
			if (x < 2 || x > 23) return;
			break;
		case 16:
		case 15:
		case 9:
		case 10:
			if (x < 1 || x > 24) return;
			break;
	}

	vec4 color = vec4(0.0, 0.0, 0.0, 0.0);

	for (int i = 0; i < textureSize(sTD2DInputs[0], 0).x; i++) {
		for (int j = 0; j < textureSize(sTD2DInputs[0], 0).y; j++) {
			vec4 texel = texelFetch(sTD2DInputs[0], ivec2(i, j), 0);
			if (int(texel.x + 13) == x && int(texel.y + 20) == y && int(texel.z + 13) == z) {
				color += texelFetch(sTD2DInputs[1], ivec2(i, j), 0) * texel.w;
			}
		}
	}
	if(color.a > 1.0) color *= color.a;

	fragColor = TDOutputSwizzle(color);
}
