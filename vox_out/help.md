# vox_out

Main visualizer and output component.

## Output

The op viewer shows a 26 x 1040 texture representing every X-Z (26 x 26) "slice" of voxelized space, stacked Y (40) slices high. If Voxelite was a cube or had any rectangular profile then each of these output pixels would correspond 1:1 to an LED. Because Voxelite has a hexagonal profile, some output pixels do not actually map to an LED.

## 3D Simulation

To view the 3D simulation:

1. Optionally split the TD window to create a new pane
2. Set the pane to _Geometry Viewer_
3. Set the pane's target op to _vox_out_

## Custom Parameters

#### Module

Set to _All_ for full-size, or set to a single module. Note that for the 2025-06-07 demo, only Module 0 will exist.

#### Output to LEDs

Enables a TouchOut for connection to another TD instance driving the LEDs.

#### Position Jitter

Simulates the imprecise position of the physical LEDs on the strings, which incidentally smoothes the volume and mitgates some of the moire patterns that occur at different viewing angles. (Visualization only, does not afffect output.)

#### Fill Black

Enables filling the texture with a black background. (Visualization only, does not afffect output.)

#### Mask

Enables a mask showing the hexagonal profile and single-module quadrant, if applicable. (Visualization only, does not afffect output.)
