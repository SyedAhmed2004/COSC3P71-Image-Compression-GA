## Image Compression Using a Block-Based Genetic Algorithm

# COSC 3P71 – Introduction to Artificial Intelligence
## Brock University

# Overview

This project implements an AI-based image compression system using a Genetic Algorithm (GA).
The objective is to compress a high-resolution 2000×1200 RGB image into a 200×120 representation while preserving visual similarity when the image is upscaled back to its original resolution.

Rather than relying on fixed interpolation techniques, image compression is formulated as an optimization problem and solved using evolutionary search.

# Approach

Representation: Each individual is a 200×120 RGB image

Optimization: Genetic Algorithm (selection, crossover, mutation)

Fitness Function: Mean Squared Error (MSE) after upscaling

Strategy: Hybrid initialization near a low-resolution baseline

Evaluation: Visual comparison and image quality metrics

The system demonstrates content-aware compression by evolving candidate compressed images that minimize reconstruction error.

# Repository Structure

- `code/` → Python implementation of the Genetic Algorithm and baseline methods

- `report/` → Final IEEE-format PDF report

- `results/` → Output figures used in the report

- `images/` → Input test images

# How to Run

Navigate to the code/ directory

Place an image named input.jpg in the same folder

Run the program using: python main.py

The program displays:

Original image

Compressed image (200×120)

Reconstructed image after upscaling

Each test image was processed independently using the same pipeline.

# Requirements

Python 3.x

OpenCV

NumPy

Matplotlib

scikit-image

Dependencies can be installed using the requirements.txt file.

# Notes

Due to the high compression ratio (100:1 pixel reduction), fine details may be lost.

The goal of this project is to demonstrate an AI-based compression approach rather than to outperform industrial compression standards.

# Authors

- Syed Ahmed (Project Leader)

- Sandhi Howlader

- Caleb Edeke

- Alena Binu