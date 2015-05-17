#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 210 Final Project: operate on a .wav file."""

import wave
import struct
import math


def wavegen(channels, width, samplerate, time, freq, volume):
    """A Simple Sound Generator that saves to .wav file format.

    Args:
        channels(int): Number of channels for the file, either 1 for mono, or 2
        for stereo.
        width(int): sample width in bytes, enter 1, 2, or 4 for 8-, 16-, or
        32-bit, respectively. The sample width determines the bit depth, which
        is similar the number of pixels in an image. The higher the bit-depth,
        the more points of measurement in each sample, the higher the resolution
        of the sound file.
        samplerate(int): The number of samples per second; similar to film,
        the samplerate is how many times per second the audio information is
        captured. CD-quality sound is 44100 samples per second. Lower integers
        have less resolution, larger integers have more, but will generate
        larger file sizes.
        time(float, int): The duration of the sound file in seconds.
        freq(int): The frequency in Hertz of the wave file. The note "A" is 440
        Hz. Humans can hear between 20 and 20,000 Hz.
        volume(int, float): The amplitude of the signal as a percent of max
        volume, 1.0 being 100% volume, 0.0 being silent. A .wav file generated
        with a volume of 1 will be max amplitude and will be very loud when
        played back.

    Returns:
        (string): Message stating file has been created.

    Examples:
        >>> wavegen(1, 2, 44100, 1.0, 440, .5)
        'mysound.wav file created in directory'
        >>> waveparam = wave.open('mysound.wav', 'r')
        >>> waveparam.getparams()
        (1, 2, 44100, 44100, 'NONE', 'not compressed')
    """
    if channels is not 1 or not 2:
        print 'Not valid number of channels. Enter 1 or 2.'
    elif width not in (1, 2, 4):
        print 'Not valid sample width.'
    elif volume < 0 or volume > 1:
        print 'Not valid amplitude ratio.'
    else:
        wavefile = wave.open('mysound.wav', 'w')
        wavefile.setnchannels(channels)
        wavefile.setsampwidth(width)
        wavefile.setframerate(samplerate)

        totsamples = int(samplerate * time)
        bits = (8 * width)
        bitvals = (((2 ** bits) * .5) - 1) * volume

        for sample in range(totsamples):
            waveform = int(bitvals * math.cos(freq * math.pi *
                                              (sample / float(samplerate))))
            wavedata = struct.pack('<h', waveform)
            wavefile.writeframesraw(wavedata)

        wavefile.writeframes(' ')
        wavefile.close()
        return 'File mysound.wav created in directory.'


def wav_info(filename):
    """Displays information about a .wav file.

    Args:
        filename(string): The filepath or name of an audio file in .wav format
        as a string.

    Returns:
        A multi-line string displaying the information about the audio file,
        including mono or stereo format, the sample width and rate, the length
        of the sound, and whether or not there is any compression on the data.

    Examples:
        >>> wav_info('bark.wav')
        Channels: Mono
        Bit Depth: 8-bit
        Sample Rate: 11025
        File Length In Seconds: 1.303
        Compression Type: not compressed

        >>> wav_info('Piano_Man.wav')
        Channels: Stereo
        Bit Depth: 16-bit
        Sample Rate: 44100
        File Length In Seconds: 339.0
        Compression Type: not compressed
    """
    fhandler = wave.open(filename, 'r')
    fparams = fhandler.getparams()
    fhandler.close()
    if fparams[0] is 1:
        chans = 'Mono'
    elif fparams[0] is 2:
        chans = 'Stereo'
    bitrate = fparams[1] * 8
    samprate = fparams[2]
    time = round((fparams[3] / float(samprate)), 3)
    filecomp = fparams[5]
    msg = ('Channels: {} \nBit Depth: {}-bit \nSample Rate: {}'
           '\nFile Length In Seconds: {} \nCompression Type: {}')

    print msg.format(chans, bitrate, samprate, time, filecomp)
