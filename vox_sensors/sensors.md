# Interaction Station Sensors

This component outputs a 9-channel CHOP with the interaction station sensor values.

## Station A: 3 pushbuttons

- momentary pushbuttons
- integer value 0 or 1 representing pushed state

## Station B: 3 rotary controls

- float value representing accumulated clockwise rotations; using the _Loop_ or _Limit_ modes in _vox_sensors_mod_ keeps this value constrained
- control rotates continuously and smoothly without any notching
- control is not designed for high speed and cannot be spun with momentum

## Station C: 2 ultrasonic range sensors facing skyward

- float value representing detected range
- 0 = minimum range or less (< 3cm)
- between 0 and 1 = proportional to detected range (3—60cm)
- -1 = beyond maximum detectable range (> ~60cm); this default value can be changed using _vox_sensors_mod_
- only ~10hz update frequency

# MIDI device

Use the `in_midi` input to connect your MIDI device. Internally the component will map pushbuttons, dials, and sliders values of 0–127 to the respective station sensor values at the correct scale.

# Connection to vox_out

_vox_sensors_ can be connected to _vox_out_ for visualization purposes.
