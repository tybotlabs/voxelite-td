# Interaction Station Sensors

This component outputs a 9-channel CHOP with the interaction station sensor values.

Channel names are reliable while total quantity and order are not guaranteed.

## Station A: 3 pushbuttons

- integer value `0` or `1` representing pushed state
- momentary buttons (on-while-pushed)

## Station B: 3 rotary controls

- float value representing accumulated degrees of rotation (counter-clockwise) in `3.75` degree increments (note that due to accumulation, values do not wrap-around and can exceed `-360`/`360`!)
- control rotates continuously and smoothly without any notching
- control is not designed for high speed and cannot be spun with momentum

## Station C: 3 ultrasonic range sensors facing skyward

- float value representing detected range
- `0` = minimum range or less (< 3cm)
- between `0` and `1` = proportional to detected range (3—60cm)
- `-1` = beyond maximum detectable range (> ~60cm)
- only ~10hz update frequency

# MIDI device

Use the `in_midi` input to connect your MIDI device. Internally the component will map pushbuttons, dials, and sliders values of `0`–`127` to the respective station sensor values at the correct scale.

# Connection to vox_out

vox_sensors can be connected to vox_out for visualization purposes.
