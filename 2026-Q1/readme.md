# VCV Rack patches - 2026-Q1

## la matrice  - 2026-01-10 (VCV Rack 2.6.6)

![la matrice patch screenshot](media/2026-01-10_la_matrice.webp)

This patch is just one *4ms Ensemble Oscillator* modulated by a slow *VCV LFO*
(0.05 Hz), overdriven with *Blamsoft XFX Overdrive* and riverberated with
*Blamsoft XFX Reverb*. The LFO also modulates the overdrive Tone control. It
sounds like the matrix.

## mum drachine - 2026-01-10 (VCV Rack 2.6.6)

![mum drachine patch screenshot](media/2026-01-10_mum_drachine.webp)

The main subunit of this patch is a *Stellare Modular Turing Machine*
controlling three *Erica Synth Pico Drums*. The sequence lenght is 8, the
triggers are taken from the pulses expander section in the TM, in particular
from outputs 1, 4, 4+7. The change knob on the TM is kept at a very low value
(~0.95) to have very slow change in the patterns.

There are two of this sub-units, driving a total of 6 Pico Drums. The *VCV LFO*
acts as a clock, via its SQR output. There is a third "voice", where the clock
is sent to a *4ms Rotating Clock Divider*, and its ÷4 output is sent to another
Pico Drums, playing a steady 4-on-floor kick drum rhythm. The seven audio
signals are mixed on a *Bogaudio MIX8*, and the mix is compressed with a
*Squinky Labs Comp*. Playing with the main change knobs on the TMs decides how
drunk the drummer is.
