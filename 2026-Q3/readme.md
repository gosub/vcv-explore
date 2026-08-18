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

## stale branch - 2026-07-12 (VCV Rack 2.6.6)

![stale branch patch screenshot](media/2026-07-12_stale_branch.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| JW-Modules | Simple Clock | master clock, with the /4, /16 and /32 taps doing all the timing |
| Befaco | Muxlicer | the melodic sequencer |
| VCV Free | Quantizer | its steps into a scale |
| Tiny Tricks | Sample and hold x16 | every 32 clocks, three new values for the oscillator |
| Audible Instruments | Macro Oscillator 2 | Plaits, the melodic voice |
| Alright Devices | Chronoblob2 | clock synced delay |
| Valley | Plateau | reverb |
| Audible Instruments | Bernoulli Gate | coin flips: open or closed hat, and whether the kick fires |
| Ghost | GHOST OHCH | hi-hats, open and closed |
| Ghost | GHOST KCK | kick |
| ProducerPack | 70sComp | compressor on the kick |
| NYSTHI | mix8 | mixer |
| VCV Core | Audio 2 | output |

The most conventional patch in this quarter: a clock, a sequencer, a drum kit.
Every division of *Simple Clock* is doing something — /4 runs the Muxlicer and
the kick, /16 accents it, /32 reloads the sample and holds that set Plaits'
timbre, morph and harmonics. So the melody changes note by note and its
character changes every eight bars.

A *Bernoulli Gate* sits in front of the drums deciding each hat between open
and closed, and whether the kick plays at all, which is the only thing keeping
a very square patch from being entirely predictable.

## apathy and scurvy - 2026-07-20 (VCV Rack 2.6.6)

![apathy and scurvy patch screenshot](media/2026-07-20_apathy_and_scurvy.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| forsitan modulare | guttur | chaotic resonator drone, the entire voice |
| Nonlinear Circuits | Sloth Apathy ×4 | four chaotic slow LFOs, one per destination |
| Squinky Labs | Comp | compressor |
| VCV Core | Audio 2 | output |

Six cables in the whole patch. *guttur* is a Duffing oscillator through 48
resonant filters, chaotic by construction, and the four *Sloths* are chaotic
too, each drifting on its own scale of minutes. Drive, damping and resonance
take the small outputs; the big one walks the bank selection, so every so often
the whole filter tuning is replaced at once.

Chaos modulating chaos, to find out whether the result stays listenable. It
does, mostly, which was the surprise.
