###############
Audio Processor
###############

Recorded sound is used in many facets of everyday life. Music, movies, and even
the sounds on your phone all need to be created or captured, then manipulated
for their intended use.
The end result of this project will be a program to take an existing audio file
and change certain perameters of the sound.

*********
Personas
*********

Persona Name
============

Eddie Editor

Details
=======

Eddie is a full-time sound editor who works on films, commericials, audio books, podcasts
and other recorded media. Eddie uses editing software and physical audio
processors to make recorded sounds better, then renders the files and sends
them off for use.

Goals
=====

Eddie has phyiscal outboard equipment, but his budget is tight and he only has
one of each processor. Eddie would like a program that emulates the changes
that some of his equipment makes to the sound files he works on in his software
audio editor.

********************************
Too much bass, not enough treble
********************************

Some of the audio that Eddie works with are not recorded by him, and are poorly
recorded. To be useable, Eddie needs to increase or decrease certain frequencies
in the source material.

Current Alternatives
====================

Eddie uses a physical equalizer to alter the sound by increasing or
decreasing the gain on certain frequencies. This means that Eddie has to send
audio out from his software editor to equipment routed to his sound card,
change the sound, and then send it back in. If he has multiple projects to work
on, this means always changing settings on his equipment, and continuously
opening and closing project files.

Value Proposition
=================

Create an emulation of the physical equalizer that Eddie uses in his workflow.
Audio could be passed into the program, and different frequencies could be
decreased or increased, and the changed audio file could be saved, all from
within the computer.

************
User Stories
************

As Eddie Editor, I want to process all of the audio files I work on right from
my computer. Specifically, I need a simple program to pass an audio file
through, change the volume of a certain frequency, and pass the altered audio
out of the program. This will save me from continuously opening and closing
different files, having to move around while working, and will allow me to
declutter some of the wires and cables all over my studio.

Acceptance Stories
==================

Scenario 01: Importing an Audio File
````````````````````````````````````

Given that I have a pre-recorded digital audio file,
And that file is in a compatible format,
When I click the "import" button,
Then I will be taken to a screen where I can change values of different
frequencies in the audio file.

Scenario 02: Manipulating the Audio File
````````````````````````````````````````

Given that I have imported the digital audio file,
And I can alter the sound via entering values in fields or with virtual "knobs",
When I *enter* a values for different parameters such as frequency, bandwith,
and volume,
Then the overall tonal character of the audio file will change.

Scenario 03: Exporting the Altered Audio
````````````````````````````````````````

Given that I have made changes to the audio file by altering the tone, such as
increasing or decreasing the bass, mid, or treble frequencices,
When I click the "export" button,
Then I will create a new copy of the digital audio file which exhibits the new
tonal characteristics.
