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

## tilt shift - 2026-07-21 (VCV Rack 2.6.6)

![tilt shift patch screenshot](media/2026-07-21_tilt_shift.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| Audible Instruments | Macro Oscillator ×2 | Braids, one carrier and one modulator |
| Audible Instruments | Meta Modulator | Warps, folding the two into each other |
| Nonlinear Circuits | Sloth Apathy ×6 | six chaotic LFOs, one per destination |
| VCV Free | VCF | lowpass, its cutoff on the slowest Sloth |
| VCV Core | Audio 2 | output |

The same idea as the patch before it, a day later, with oscillators where the
resonator was. Six *Sloths* feed five destinations: timbre and colour on each
*Braids*, frequency modulation on one of them, cutoff on the filter. *Warps*
cross modulates the two oscillators, so even the carrier is not stable.

Mono, no clock, no sequence, nothing to start or stop. It is left running and
listened to at intervals.

## little psychedelia - 2026-07-25 (VCV Rack 2.6.6)

![little psychedelia patch screenshot](media/2026-07-25_little_psychedelia.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| 4ms | Basic WAV Player ×3 | three samples |
| forsitan modulare | vestigia | stereo memory effect, fed by all three |
| Audible Instruments | Bernoulli Gate | routes vestigia's own recall events back as play triggers |
| VCV Core | Audio 2 | output |

A loop with the tape in charge. Three players feed *vestigia*, a memory effect
that records what it hears, degrades it and recalls it later. When vestigia
begins a recollection it emits an event, and that event runs through two
Bernoulli coin flips to trigger one of the three players.

So nothing outside the patch decides when a sample plays: it plays because the
memory effect remembered something, which gives it something new to remember.

## tundo graph - 2026-08-07 (VCV Rack 2.6.6)

![tundo graph patch screenshot](media/2026-08-07_tundo_graph.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| Valley | Topograph | Mutable Grids: three streams of drum triggers |
| forsitan modulare | tundo ×3 | one drum voice per stream |
| VCV Free | VCA Mix | mixes the three |
| FLAG Free | Thorns | distortion on the whole kit |
| forsitan modulare | antrum | reverb |
| VCV Core | Audio 2 | output |

Ten cables, and the patch is exactly what its name is: *tundo* against
*Topograph*. Grids' bass, snare and hi-hat outputs trigger three tundo, each
one set to a different corner of its range, and that is the entire kit.

The distortion and the reverb come after the mixer rather than per voice, so
the three drums are crushed and put in a room together. It makes them sound
like one instrument being played instead of three modules firing.

## vortexcal - 2026-08-09 (VCV Rack 2.6.6)

![vortexcal patch screenshot](media/2026-08-09_vortexcal.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| forsitan modulare | vorax | feedback drone synthesizer, the source |
| forsitan modulare | textor | loop weaver, two seconds rewoven at every turn |
| forsitan modulare | caligo | Greyhole echo, a long modulated delay in an allpass diffuser |
| VCV Core | Audio 2 | output |

Four modules in one line, three of them mine: *vorax* howls, *textor* catches
two seconds of the howl and reweaves it, *caligo* smears the result down a
nested allpass. Six cables, no modulation sources, no clock.

Every change you hear comes from feedback — each of the three has a loop inside
it, and they are chained so that each one is fed a signal that never settles.
The patch was a test of whether the three would sit together without becoming
mud.

## scrappy apathic twenties - 2026-08-11 (VCV Rack 2.6.6)

![scrappy apathic twenties patch screenshot](media/2026-08-11_scrappy_apathic_twenties.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| forsitan modulare | scrupea | chaotic bank: 16 oscillators into tuned feedback combs |
| VCV Free | Merge | its stereo pair into one polyphonic cable |
| forsitan modulare | viginti | MS-20 lowpass, filtering both channels at once |
| Nonlinear Circuits | Sloth Apathy | chaotic LFO on the cutoff |
| VCV Free | Split | back apart into stereo |
| VCV Core | Audio 2 | output |

The title names its three modules: **scr**upea, Sloth **Apathy**, and *viginti*,
which is twenty in Latin.

Seven cables. The interesting one is the *Merge*: scrupea's left and right are
folded into a single polyphonic cable so that one viginti filters both channels
at once, then *Split* takes them back apart. One filter, two channels, and the
MS-20 diodes clipping identically on each.

## grone recreation - 2026-08-12 (VCV Rack 2.6.6)

![grone recreation patch screenshot](media/2026-08-12_grone_recreation.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| Spherical Sound Society Free | GlitchStorm | the source, a byte-beat style generator |
| forsitan modulare | viginti | MS-20 lowpass |
| VCV Free | LFO | sweeps the cutoff |
| Audible Instruments | Texture Synthesizer | Clouds, in texture mode |
| VCV Core | Audio 2 | output |

Five cables, which is as short as a signal path gets. *GlitchStorm* generates,
the MS-20 filter takes the top off it with an LFO walking the cutoff, and
*Clouds* turns whatever it is handed into a slowly breathing texture.

The point is the last stage: Clouds in texture mode will accept almost any
source and give back the same kind of cloud, so the patch is really about how
much of GlitchStorm's character survives it. Some does.
