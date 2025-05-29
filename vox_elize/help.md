# vox_elize

Blend point position and color data textures into an output texture representing Voxelite's renderable volume. This output is ready for feeding into _vox_out_.

## Usage

The op takes two equally-sized textures:

- point position data where every pixel R,G,B,A is point X,Y,Z,W
- respective color data where each pixel is points' R,G,B,A values

Position data should be in floating point format as 1.0 in voxelized space respresents 1 LED adjacent. Given that the volume is centered at 0,0,0, the actual LEDs are positioned at:

- X: -12.5 to 12.5 (26 LEDs at widest)
- Y: -19.5 to 19.5 (40 LEDs tall)
- Z: -12.5 to 12.5 (26 LEDs at deepest)

The point colors get blended in voxelized space where the position W is the weight of that pixel. Depending on the density of points used, the W should be reduced to prevent positions from becoming prematurely saturated. For example, if a single point at some X,Y,Z and W of 1 is colored 1,0,0,1, the LED at that point's voxelized position will be full red. If the intention is actually that 8 points falling in the same voxelized position should be required to achieve full red, the points can have the same color but should use a W of 0.125 (i.e. 1 / 8).
