# VCV Rack patches - 2021-Q4

## drone pelan - 2021-12-05

This a very basic patch, with a classic signal path:

LFO -> OSC -> OVERDRIVE -> FEEDBACK DELAY

LFO is *MSM Rogue*
OSC is *DHE Blossom*
OVERDRIVE is *FLAG Thorns*
DELAY is *Surge XT Delay*

## contra - 2021-12-06

This patch has two voices:

- a *Voxglitch ByeBeat*
- an *SV Modular CR78*

Clicking the button on the *Count Modula Manual Gate* triggers an attack-decay
envelope in *Bogaudio AD*; the envelope opens a *VCV VCA* that lets the ByteBeat
pass through. The end-of-cycle outputs of AD triggers on the two voices in CR78.
Which of the two voices is selected with a combination of two *VCV Sequential
Switch 4 to 1*. Every three beats the source is switched to the other drum
voice.

## noneck - 2021-12-07

A *Voxglitch ByteBeat* is passed through an *Audible Instruments Resonator* and
then low-pass filtered with a *BGA LVCF*. The ByteBeat is mixed low in the
center, the Resonator slightly to le the left, the low pass filter slighlty to
the right.
