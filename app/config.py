MODEL_ID = "runwayml/stable-diffusion-v1-5"

OUTPUT_FILE = "outputs/stylized_image.png"


DEFAULT_IMAGE_STRENGTH = 0.75

DEFAULT_INFERENCE_STEPS = 30

DEFAULT_GUIDANCE_SCALE = 7.5


# Predefined Stable Diffusion prompts shown in the Gradio interface.
PREDEFINED_STYLE_PROMPTS = {
    "Digital Art Style": (
        "Convert this image into a highly detailed digital art illustration, "
        "vibrant colors, sharp details, professional artwork"
    ),
    "Watercolor Painting": (
        "Transform this image into a watercolor painting style, soft brush strokes, "
        "artistic texture, pastel colors"
    ),
    "Cinematic Portrait": (
        "Create a cinematic portrait style with realistic lighting, dramatic shadows, "
        "high quality photography"
    ),
    "Anime Style": (
        "Transform this image into anime art style, detailed character design, "
        "clean lines, vibrant colors"
    ),
    "Fantasy Art": (
        "Convert this image into fantasy artwork, magical atmosphere, "
        "detailed environment, realistic fantasy style"
    )
}


def get_predefined_style_prompt(style_name):
    """Return the prompt for a selected style, or an empty prompt for custom input."""

    return PREDEFINED_STYLE_PROMPTS.get(style_name, "")
