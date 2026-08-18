# VCV Rack patches - 2026-Q2

## scando - 2026-06-14 (VCV Rack 2.6.6)

![scando patch screenshot](media/2026-06-14_scando.webp)

| Plugin | Module | Role in the patch |
|---|---|---|
| Impromptu | Clkd | master clock |
| Stellare Modular | Turing Machine | its pulses both strike the string and feed the divider |
| Count Modula | Clock Divider | ÷8, so the string is retuned far less often than it is struck |
| VCV Free | Mult | fans that slow trigger out to the whole holder bank |
| SickoCV | holder8 | sample and holds, one per scando parameter |
| forsitan modulare | scando | scanned synthesis oscillator, the only voice here |
| VCV Free | Scope | watching the string move |
| Sapphire | Galaxy | reverb |
| VCV Core | Audio 2 | output |

Everything in this patch serves one module. *scando* is a scanned synthesis
oscillator: a mass-spring string, struck and then read around as a wavetable,
so you hear the shape of the string rather than the string itself.

*Clkd* drives a *Turing Machine* whose pulses are the hammer. Every eighth
pulse, through the *Clock Divider* and a *Mult*, the *holder8* bank samples
at once and drops five new voltages onto pitch, mass, damping, centering and
shape. The string is struck constantly and rebuilt rarely: it gets a while to
ring in one body before being quietly given another. *Galaxy* provides the
room it rings in.
