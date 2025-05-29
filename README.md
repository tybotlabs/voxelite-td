# TouchDesigner Kit for Voxelite

This repo is a kit for developing [TouchDesigner](https://derivative.ca/) animations for volumetric light art installations. It specifically targets Voxelite, a 2025 project of [Tybot Laboratories](https://tybot.ca) (i.e. me, Tyler Soon), however any hard-coded specifics can easily be adapted for other applications.

## Terms of Use

1. See [license](LICENSE)
2. If you're using this and I don't already know you, get in touch! Credit would be nice, but what I'm really interested in is seeing your work and/or collaboration! :-)

## Contents

### vox_out

Main visualizer and output component.

### vox_elize

Blend point position and color data textures into an output texture representing Voxelite's renderable volume. This output is ready for feeding into _vox_out_.

## In Progress

### vox_texture

Generate position and color data textures from an input TOP. Render an image/video!

### vox_trilinear

Perform trilinear interpolation on position and color data textures in voxelized space, a blending strategly of "splitting fat points" vs. increasing point density.
