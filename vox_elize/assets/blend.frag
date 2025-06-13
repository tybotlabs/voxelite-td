#extension GL_EXT_texture_array : enable
uniform vec4 saturationLimit;
uniform vec4 arrayDepth;

out vec4 fragColor;
void main()
{
	vec4 color = vec4(0.0);
	for (int i = 0; i < arrayDepth.s; i++) {
		vec4 v = texelFetch(sTD2DArrayInputs[0], ivec3(gl_FragCoord.x, gl_FragCoord.y, i), 0);
		color += v;
	}
	if(color.a > saturationLimit.s) color /= color.a / saturationLimit.s;
	color = clamp(color, 0.0, 1.0);
	fragColor = TDOutputSwizzle(color);
}
