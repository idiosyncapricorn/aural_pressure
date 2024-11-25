# Perceived Loudness Analysis

This Python script calculates the perceived loudness of sound by analyzing its frequency components and applying psychoacoustic sensitivity factors (e.g., Fletcher-Munson curves). It is designed for analyzing sound effects, audio clips, or other `.wav` files to understand how different frequencies contribute to perceived loudness.

## How to Use
1. Install dependencies:
   ```bash
   pip install numpy librosa scipy matplotlib

	2.	Place your .wav file (e.g., a sound effect or audio clip) in the project directory.
	3.	Run the script, specifying your file:

python perceived_loudness.py


	4.	View the results, which display the perceived loudness at different frequencies.

Example

For a sound effect file named explosion.wav, the output will show:

Frequency: 500.00 Hz, Perceived Loudness: 78.15 dB
Frequency: 1000.00 Hz, Perceived Loudness: 84.42 dB
Frequency: 5000.00 Hz, Perceived Loudness: 90.13 dB

Use this tool to compare perceived loudness across different sound effects or frequencies.

