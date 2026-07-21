def validate_uploaded_image(image):

    if image is None:

        return False, "Please upload an image."

    return True, ""



def validate_style_prompt(prompt):

    if prompt is None or prompt.strip()=="":
        
        return False, "Please enter style prompt."


    if len(prompt.strip()) < 3:

        return False, "Prompt is too short."


    return True,""



def validate_generation_parameters(
        image_strength,
        guidance_scale,
        inference_steps,
        seed_number
):

    if not 0.1 <= float(image_strength) <= 1.0:

        return False,"Invalid image strength"


    if not 1 <= float(guidance_scale) <= 20:

        return False,"Invalid guidance scale"


    if not 10 <= int(inference_steps) <= 100:

        return False,"Invalid inference steps"


    if seed_number is not None:

        if int(seed_number)<0:

            return False,"Invalid seed"



    return True,""