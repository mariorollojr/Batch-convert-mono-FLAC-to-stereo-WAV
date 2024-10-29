# Batch-convert-mono-FLAC-to-stereo-WAV
Simple script to batch process mono FLAC audios to stereo WAV audios for posterior processing on soundecology R package.

While the `multiple_sounds` function is theoretically capable of handling batches of FLAC audio, it apparently has problems when it has to deal with 32-bit FLACs. 

The only solution I found was to "reconvert" mono FLACs to stereo WAVs (actually dual mono, so that the left and right channels have the same information). 

In this way, the function works satisfactorily.
