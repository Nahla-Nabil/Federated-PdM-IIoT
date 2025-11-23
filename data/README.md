# Dataset Directory

This directory contains the CWRU-inspired bearing fault dataset.

## Dataset Description

- **Total Samples**: 2,300
- **Classes**: 10 fault categories
- **Samples per Class**: 230
- **Features**: 10 statistical + spectral features
- **Format**: CSV

## Fault Categories

1. Normal
2. IR_007 (Inner Race - 0.007")
3. IR_014 (Inner Race - 0.014")
4. IR_021 (Inner Race - 0.021")
5. OR_007_6 (Outer Race - 0.007" @ 6 o'clock)
6. OR_014_6 (Outer Race - 0.014" @ 6 o'clock)
7. OR_021_6 (Outer Race - 0.021" @ 6 o'clock)
8. Ball_007 (Ball Fault - 0.007")
9. Ball_014 (Ball Fault - 0.014")
10. Ball_021 (Ball Fault - 0.021")

## Usage

The script automatically generates synthetic data if no CSV is found.
To use your own data, place it here and ensure it matches the expected format.

## Reference

Case Western Reserve University Bearing Data Center:
https://engineering.case.edu/bearingdatacenter
