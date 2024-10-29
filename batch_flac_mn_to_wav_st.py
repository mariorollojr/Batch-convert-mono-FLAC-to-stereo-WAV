#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:00:08 2024

@author: Mario Rollo
"""

import os
import subprocess

input_dir = "/Users/maro6035/louise_test"
output_dir = "/Users/maro6035/louise_stereo_wav"
os.makedirs(output_dir, exist_ok=True)

# Loop through FLAC files and convert each to stereo WAV
for filename in os.listdir(input_dir):
    if filename.endswith(".flac"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".flac", ".wav"))
        try:
            # Convert FLAC to stereo WAV with SoX
            subprocess.run(["sox", input_path, "-c", "2", output_path], check=True)
            print(f"Converted {filename} to stereo WAV.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {filename}: {e}")

print("Batch conversion complete. Stereo WAV files are in", output_dir)
