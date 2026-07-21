from app.model.stable_diffusion import load_image_to_image_pipeline

from app.services.validators import (
    validate_uploaded_image,
    validate_style_prompt,
    validate_generation_parameters
)

from app.utils.helpers import create_torch_generator

from app.config import OUTPUT_FILE



def generate_stylized_image(
        input_image,
        style_prompt,
        image_strength,
        guidance_scale,
        inference_steps,
        seed_number
):


    valid,msg = validate_uploaded_image(input_image)

    if not valid:

        return None,msg,None



    valid,msg = validate_style_prompt(style_prompt)

    if not valid:

        return None,msg,None



    valid,msg = validate_generation_parameters(
        image_strength,
        guidance_scale,
        inference_steps,
        seed_number
    )


    if not valid:

        return None,msg,None



    try:


        pipeline = load_image_to_image_pipeline()


        generator = create_torch_generator(seed_number)



        result = pipeline(

            prompt=style_prompt,

            image=input_image,

            strength=float(image_strength),

            guidance_scale=float(guidance_scale),

            num_inference_steps=int(inference_steps),

            generator=generator
        )



        generated_image = result.images[0]


        generated_image.save(
            OUTPUT_FILE
        )


        return (
            generated_image,
            "Generation completed successfully",
            OUTPUT_FILE
        )


    except Exception as e:


        return None,str(e),None