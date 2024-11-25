import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.fft import fft, fftfreq

def perceived_loudness(frequency, pressure_variation, density, sensitivity_factor):
    """
    Calculate perceived loudness based on frequency, pressure, density, and sensitivity.
    """
    # Reference pressure (threshold of hearing)
    P0 = 20e-6  # 20 µPa
    
    # Compute perceived loudness
    loudness = (10 * np.log10(pressure_variation / P0)) * sensitivity_factor * (frequency / density)
    return loudness

# Example sensitivity values for Fletcher-Munson curve (simplified)
sensitivity_curve = {
    100: 0.5,
    1000: 1.0,
    5000: 1.2,
    10000: 0.8
}

def get_sensitivity(frequency):
    """
    Interpolate sensitivity factor for a given frequency.
    """
    keys = list(sensitivity_curve.keys())
    values = list(sensitivity_curve.values())
    return np.interp(frequency, keys, values)

def process_audio(file_path):
    """
    Load an audio file and calculate perceived loudness for its frequency components.
    """
    # Load audio file
    audio, sr = librosa.load(file_path, sr=None)
    
    # Perform FFT to extract frequency components
    n = len(audio)
    yf = fft(audio)
    xf = fftfreq(n, 1 / sr)[:n // 2]  # Positive frequencies
    
    # Calculate pressure variation from FFT magnitude
    amplitudes = 2.0 / n * np.abs(yf[:n // 2])
    
    # Density (air at room temperature)
    density = 1.2  # kg/m^3
    
    # Calculate perceived loudness for each frequency
    results = []
    for freq, amp in zip(xf, amplitudes):
        if freq <= 0:  # Ignore negative or zero frequencies
            continue
        sensitivity = get_sensitivity(freq)
        loudness = perceived_loudness(freq, amp, density, sensitivity)
        results.append((freq, loudness))
    
    return results

# Example usage
audio_file = "example.wav"  # Replace with your audio file path
loudness_data = process_audio(audio_file)

# Print results
for freq, loudness in loudness_data:
    print(f"Frequency: {freq:.2f} Hz, Perceived Loudness: {loudness:.2f} dB")

# Extract frequency and loudness data
frequencies = [freq for freq, loudness in loudness_data]
loudness_values = [loudness for freq, loudness in loudness_data]

# Plot the perceived loudness
plt.figure(figsize=(10, 6))
plt.plot(frequencies, loudness_values, label="Perceived Loudness", color='blue')
plt.xscale('log')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Perceived Loudness (dB)")
plt.title("Perceived Loudness vs. Frequency")
plt.grid(True)
plt.legend()
plt.show()
