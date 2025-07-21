# TouchDesigner Kit for Voxelite

This repo is a kit for developing [TouchDesigner](https://derivative.ca/) animations for volumetric light art installations. It specifically targets Voxelite, a 2025 project of [Tybot Laboratories](https://tybot.ca) (i.e. me, Tyler Soon), however hard-coded specifics can easily be adapted for other applications.

See [example.toe](example.toe).

## Terms of Use

1. See [license](LICENSE)
2. If you're using this and I don't already know you, get in touch! Credit would be nice, but what I'm really interested in is seeing your work and/or collaboration! :-)

## Components

#### vox_out

Main visualizer and output component.

#### vox_elize

Blend point position and color data textures into an output texture representing Voxelite's renderable volume. This output is ready for feeding into _vox_out_.

#### vox_sensors

Use the three interaction stations' button, rotary, and ranging sensors as inputs. See [sensors.md](vox_sensors/sensors.md) for more information.

## Producing Production-Ready Patches

### Paths

Place TOX and all assets in a folder at a peer level with `voxelite-td` and be sure to use `Relative to external COMP file (.tox)`. The contents of the folder may be organized however you please so long as it contains everything necessary for the TOX and uses relative paths to reference any components of `voxelite-td`.

```
voxelite-td/
yourfoldername/
yourfoldername/yourtox.tox
yourfoldername/someasset.obj
yourfoldername/somesubfolder/somefile.txt
```

### Inputs/Outputs

Note that connector presence and order is critical whereas names are recommended but not required.

#### Inputs

| Order | Type    | Name       | Detail                                                                                   |
| ----- | ------- | ---------- | ---------------------------------------------------------------------------------------- |
| 1     | CHOP In | in_sensors | From live _vox_sensors_                                                                  |
| 2     | CHOP In | in_audio   | For audio reactive patches, a 2-channel continuous soundtrack will be fed in (see below) |

#### Outputs

| Order | Type     | Name            | Detail                                                |
| ----- | -------- | --------------- | ----------------------------------------------------- |
| 1     | TOP Out  | out_centerpiece | For _vox_out_: 26 x 1040 texture for centerpiece LEDs |
| 2     | TOP Out  | out_stations    | For _vox_out_: 9 x 16 texture for station LEDs        |
| 3     | CHOP Out | out_audio       | For _vox_out_: 3 channels for station audio           |

### Patch Properties with _properties_ Table DAT

The mixer will change the audio behaviour if your component has a Table DAT named _properties_. Populate the table with:

| key       | value |
| --------- | ----- |
| audio_in  | True  |
| audio_out | False |

In this case, the mixer will:

1. connect a continuous soundtrack to the _audio_in_ CHOP In for analysis within the patch
2. keep the continous soundtrack connected to the speakers **instead** of using the _out_audio_ CHOP Out

### Mixer Events with _external_callbacks_ Execute DAT (optional)

The mixer will invoke callbacks in your component if it contains an Execute DAT named _external_callbacks_.

| Method                | Notes                                                                                                                                                                                                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onMixStart(seconds)` | Invoked at transition start. `seconds` is the duration of the forthcoming transition.                                                                                                                                                                                                                      |
| `onAudioStart()`      | Invoked at moment of connection of _out_audio_ to the speakers. The mixer cross-fades visuals but not audio, instead fading old audio down before fading new audio up. This event can therefore be expected to occur halfway through the transition, and while the volume is at its initial level of zero. |
| `onMixEnd()`          | Invoked at transition end.                                                                                                                                                                                                                                                                                 |

### Notes

#### Cooking

The mixer enables cooking on the entire patch at the transition start and disables it at transition end.

#### Use of _vox_out_

For development it is recommended to use _vox_out_ in a TOE file containing your TOX, and connect the TOX outputs to _vox_out_ for visualization. If you do have occurrences of _vox_out_ in your TOX, ensure that the _Send_ parameter remains **off** so as not to interfere with the production system's master _vox_out_.
