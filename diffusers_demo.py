#!/usr/bin/env python3

from diffusers import DiffusionPipeline
from fire import Fire


def main(prompt: str):
    pipeline = DiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", use_safetensors=True
    )
    pipeline.to("cuda")

    image = pipeline(prompt).images[0]
    image.show()


if __name__ == "__main__":
    Fire(main)
