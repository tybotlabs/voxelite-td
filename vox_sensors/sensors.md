# Interaction Station Sensors

This component outputs a 9-channel CHOP with the interaction station sensor values.

## Station A: 3 pushbuttons

- momentary pushbuttons
- integer value 0 or 1 representing pushed state

## Station B: 3 rotary controls

- float value representing accumulated degrees of clockwise rotation in 3.75 degree increments
- control rotates continuously and smoothly without any notching
- control is not designed for high speed and cannot be spun with momentum

## Station C: 2 ultrasonic range sensors facing skyward; 1 sensor TBD

- float value representing detected range
- 0 = minimum range or less (< 3cm)
- between 0 and 1 = proportional to detected range (3—60cm)
- -1 = beyond maximum detectable range (> ~60cm)
- only ~10hz update frequency

# MIDI device

Use the `in_midi` input to connect your MIDI device. Internally the component will map pushbuttons, dials, and sliders values of 0–127 to the respective station sensor values at the correct scale.

# Connection to vox_out

_vox_sensors_ can be connected to _vox_out_ for visualization purposes.

# Normalizing Values

_vox_sensors_mod_ can be used for common normalization of the sensor values: see the _Custom_ parameters tab. Note that _Common: Reload Custom Parameters_ should be **off** to avoid having your custom parameter changes reset when the TOX is reloaded.
