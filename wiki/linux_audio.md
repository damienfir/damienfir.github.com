## Linux Audio resources

#### Setup
Access to the devices is made via ALSA, but ALSA has mutliple parts including a
userspace API, which you are not required to use.

https://www.linux.com/news/hardware/drivers/8100-why-you-should-care-about-pulseaudio-and-how-to-start-doing-it

Configure Pulseaudio to lie between ALSA and the audio application.

Apparently Jack cannot output to Pulseaudio, turnaround required. Some module is
available in Pulseaudio to take Jack as a source `pactl load-module
module-jack-source`.
http://www.whatsmykarma.com/blog/?p=478


#### Instruments
Hard to find a good .gig library.

Cannot find a player for sfz.

Play VST instruments using `dssi-vst`. Not the best way because VST plugins fail
to load. Use `festige` instead. It features a GUI and loads VST using `fst`.
`Kontakt` isn't working well, can't install instruments with `wine`.
Solve the MIDI problem with `a2jmidid -e`

Good .sf2 instruments at DSK.

Find VSTi here:
- http://www.vst4free.com
- http://www.genuinesoundware.com
- http://www.johnrofrano.com/vstinstruments.htm
- http://www.majken.se/
- http://www.dskmusic.com/
- http://producertoolz.com/category/vsts/
- http://illformed.org/plugins/glitch/
- http://kunz.corrupt.ch/products
- http://www.kvraudio.com (search)
- http://www.gersic.com/plugins/

paid
- http://www.applied-acoustics.com/loungelizard/overview
- http://www.powerdrumkit.com/


#### Studio
mixer
	- non-mixer http://non-mixer.tuxfamily.org/
sequencer
	- non-sequencer
	- harmonySEQ
synth
	- zynaddsubfx
	- csound http://www.csounds.com/frontends/
session
	- non-session manager
	- ladish

#### IRC
\##linuxaudio  
\#LAD  
\#ardour  


#### Links
- http://petri-foo.sourceforge.net/	Simple sampler
- http://www.linuxmusicians.com/		Linux audio forums
- http://quicktoots.linux-audio.com/	Tutorial resource
- http://archaudio.org/				Audio software packages for Archlinux
- http://linux-audio.com/				General resources
- http://lac.linuxaudio.org/			Linux audio conferences information
- http://gamesoundcon.com/			Conference on game audio design
- http://wiki.linuxaudio.org/wiki/start	Plenty of resources
- https://github.com/harryhaaren/openAudioProgrammingTutorials		tutorials
- http://lesitedeburnie.free.fr/lalistedeburnie1-en.html		VST plugins
- http://www.louigiverona.ru/?page=projects&s=writings&t=linux&a=linux_harmonyseq		HarmonySEQ
- http://www.linuxjournal.com/users/dave-phillips		Dave Phillips homepage


General

- http://www.linuxmao.org
- http://wiki.linuxmusicians.com
- http://lievenmoors.github.com
- http://hubpages.com/hub/Recording-in-Linux-aka-Free-and-Open-Source-Digital-Audio-Workstation

Sounds

- http://www.fruityclub.net/ressources-samples-soundfonts/banques-sonores-le-meilleur-du-net

Theory

- http://www.whitakerblackall.com/blog/music-theory-for-beginners/

Sounds

- http://www.hammersound.net
- http://www.soundfonts.it/?a=soundfonts
- http://www.synthfont.com/links_to_soundfonts.html (repertory)
- http://www.sonivoxmi.com/index.asp (paid)
- http://www.soundsonline.com (paid)
- http://www.vipzone-samples.com (paid)
- http://www.ntonyx.com/sf.htm (paid)
- https://www.digitalsoundfactory.com (paid)
- http://www.modernbeats.com (paid)

Setup

- http://apps.linuxaudio.org/wiki/seq24togglemiditutorial
