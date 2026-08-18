# VCV Rack patches - 2026-Q3

## for eliane - 2026-07-06 (VCV Rack 2.6.6)

![for eliane patch screenshot](media/2026-07-06_for_eliane.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| VCV Free | VCO ×2 | two oscillators a hair apart, every waveform of each taken at once |
| Sonus Modular | Ringo | ring modulates the two squares against each other |
| VCV Free | VCF | lowpass on the ring modulated pair |
| Bogaudio | MIX8 | eight channels: six raw waveforms, the filter, the ring |
| Bogaudio | LMTR | limiter, because eight summed waveforms clip |
| Sapphire | Galaxy | reverb |
| VCV Core | Audio 2 | output |

Two oscillators detuned by very little, with the sine, triangle and sawtooth of
both taken straight to the mixer, and each one's sine bent into the other's
frequency modulation input. Nothing is sequenced and nothing is clocked: the
whole patch is the beating between the two, arriving at a different rate on
every waveform at once. The ring modulator and the filter add two more voices
made of the same two oscillators.

A homage to Éliane Radigue, whose music this does not come near, but whose
method — two sources, almost in tune, given enough time — is the only
instruction it follows.

## sheep as the symbol of sleep - 2026-07-12 (VCV Rack 2.6.6)

![sheep as the symbol of sleep patch screenshot](media/2026-07-12_sheep_as_the_symbol_of_sleep.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| JW-Modules | Grains | granular sampler, the only sound source |
| VCV Free | Wavetable LFO | the slow scan |
| Befaco | A*B+C | scales that scan into the grain position range |
| Vult Modules Free | Debriatus | distortion |
| Surge XT | Chorus | widens it (a second one sits unpatched) |
| Sapphire | Galaxy | reverb |
| VCV Core | Audio 2 | output |

Eleven cables, and six of them are just the signal walking to the output. A
granular sampler has its playback position swept by one wavetable LFO, scaled
into range by *A\*B+C*, and everything after that is blur: distortion, chorus,
reverb, three stages that each smear it further.

The title counts sheep, and the patch is built to be dozed off to, though the
distortion argues with the idea.
