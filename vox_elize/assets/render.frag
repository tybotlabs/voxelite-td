out vec4 fragColor;
uniform vec4 saturationLimit;

void main()
{

	uint x = int(gl_FragCoord.x);
	uint y = int(gl_FragCoord.y) / 26;
	uint z = int(gl_FragCoord.y) % 26;

	vec4 color = vec4(0.0, 0.0, 0.0, 0.0);

	for (int i = 0; i < textureSize(sTD2DInputs[0], 0).x; i++) {
		for (int j = 0; j < textureSize(sTD2DInputs[0], 0).y; j++) {
			vec4 texel = texelFetch(sTD2DInputs[0], ivec2(i, j), 0);
			if (int(texel.x + 13) == x && int(texel.y + 20) == y && int(texel.z + 13) == z) {
				color += texelFetch(sTD2DInputs[1], ivec2(i, j), 0) * texel.w;
			}
		}
	}
	if(color.a > saturationLimit.r) color /= color.a / saturationLimit.r;

	color = clamp(color, 0.0, 1.0);

	fragColor = TDOutputSwizzle(color);
}
