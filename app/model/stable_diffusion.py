import torch

from diffusers import StableDiffusionImg2ImgPipeline

from app.config import MODEL_ID


image_to_image_pipeline = None



def load_image_to_image_pipeline():

    global image_to_image_pipeline


    if image_to_image_pipeline is not None:
        return image_to_image_pipeline


    if torch.cuda.is_available():

        dtype = torch.float16
        device = "cuda"

    else:

        dtype = torch.float32
        device = "cpu"



    image_to_image_pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype
    )


    image_to_image_pipeline.to(device)


    return image_to_image_pipeline