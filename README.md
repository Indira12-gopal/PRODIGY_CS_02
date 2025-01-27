# PRODIGY_CS_02

This repository contains a Python script that provides basic image encryption and decryption functionality by swapping the red and blue channels of an image. The encryption and decryption process is symmetric, meaning you can decrypt an encrypted image using the same method by swapping the channels back.

## Features

- Encrypts an image by swapping its red and blue channels.
- Decrypts an image by reversing the channel swap.
- Saves the encrypted and decrypted images at specified paths.

## Requirements

This project requires the Python Imaging Library (PIL), which is available through the `Pillow` package. You can install the required dependencies by running:

'''bash
pip install Pillow
'''
Code Explanation
The script uses the PIL library to open and manipulate the image.
The encrypt_image function swaps the red and blue channels of the image to encrypt it.
The decrypt_image function swaps the channels back to their original state to decrypt the image.
The input and output image paths are taken from user input.
