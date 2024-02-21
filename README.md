# Quick start

This project demonstrates how to use [huggingface/diffusers](https://github.com/huggingface/diffusers) for simple image generation from text phrases

## Requirements

- pyenv
- poetry

## Installation
1. Install CUDA
1. Install pyenv
1. Install poetry
1. Install python3.10
```bash
pyenv install 3.10
pyenv local 3.10
```
1. Install poetry dependencies
```bash
poetry install
```

## Usage

After installation, you should be able to run the command line script directly.
In my tests, this particular model requires about 6 GB of GPU RAM.

```bash
poetry run ./diffusers_demo.py "Picard, his hands raised into the sky"
```

Example output:

![Picard graphic](images/example.PNG)
