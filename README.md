# Shamir-s-Secret-Sharing
# Shamir's Secret Sharing Scheme Implementation in Python
# By: Aziz Al-Qwati

This repository contains a Python implementation of Shamir's Secret Sharing scheme, a cryptographic algorithm for securely splitting a secret into multiple shares. Specifically, this script supports a threshold of t=3t=3 or t=2t=2, meaning that any 3 or 2 out of the total number of shares can be used to reconstruct the original secret.
Features:

    Secret Splitting: Divide a secret into multiple shares.
    Secret Reconstruction: Combine a minimum of 3 shares to reconstruct the original secret.
    User-Friendly Interface: Simple CLI for inputting and recovering secrets.
    Randomized Share Generation: Each share is generated with random coefficients for enhanced security.

Usage:

    Creating Shares: Run the script and follow the prompts to input your secret. The script will output the shares.
    Reconstructing the Secret: Input the necessary number of shares (at least 3) as prompted by the script to retrieve the original secret.

Requirements:

    Python 3.x
    Sympy library (for mathematical computations)
