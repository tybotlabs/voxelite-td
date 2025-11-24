# vox_out

Main visualizer and output component.

## Output

The op viewer shows a 26 x 1040 texture representing every X-Z (26 x 26) "slice" of voxelized space, stacked Y (40) slices high. If Voxelite had a rectangular profile (e.g. a cube) then each of these output pixels would correspond 1:1 to an LED. Because Voxelite has a hexagonal profile, some output pixels do not actually map to an LED and the viewer output is masked accordingly.

When _in_stations_ is in use the op viewer extends the top to include this texture.

## 3D Simulation

To view the 3D simulation:

1. Optionally split the TD window to create a new pane
2. Set the pane to _Geometry Viewer_
3. Set the pane's target op to _vox_out_

## Custom Parameters

#### Position Jitter

Simulates the imprecise position of the physical LEDs on the strings, which incidentally smoothes the volume and mitgates some of the moire patterns that occur at different viewing angles. (Visualization only, does not afffect output.)

#### Environment

Sets the height of the centerpiece based on the environment you are simulating.

#### Audio Preview / Audio Channels

When enabled, sends the selected audio channels to the default audio device.
