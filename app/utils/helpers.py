import torch

from app.config import (
    DEFAULT_GUIDANCE_SCALE,
    DEFAULT_IMAGE_STRENGTH,
    DEFAULT_INFERENCE_STEPS
)



def create_torch_generator(seed):

    if seed is None:

        return None


    seed=int(seed)


    if torch.cuda.is_available():

        return torch.Generator(
            device="cuda"
        ).manual_seed(seed)


    return torch.Generator(
        device="cpu"
    ).manual_seed(seed)
def clear_interface():

    return (
        None,      # input image
        "Custom Prompt",  # predefined style
        "",        # prompt
        DEFAULT_IMAGE_STRENGTH,     # image strength
        DEFAULT_INFERENCE_STEPS,    # inference steps
        DEFAULT_GUIDANCE_SCALE,     # guidance scale
        None,      # seed
        None,      # preview image
        None,      # generated image
        "Ready. Upload an image, describe a style, then click Generate.",
        None       # download file
    )
