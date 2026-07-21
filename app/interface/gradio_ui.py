import gradio as gr


from app.services.image_generator import generate_stylized_image
from app.utils.helpers import clear_interface

from app.config import (
    DEFAULT_IMAGE_STRENGTH,
    DEFAULT_INFERENCE_STEPS,
    DEFAULT_GUIDANCE_SCALE,
    PREDEFINED_STYLE_PROMPTS,
    get_predefined_style_prompt
)



def show_uploaded_image(image):

    return image



def create_gradio_interface():
  
    with gr.Blocks() as demo:
        gr.Markdown("# Stable Diffusion Image-to-Image Style Converter")
        gr.Markdown(
            "Upload an image, describe the style you want, and generate a new stylized version."
        )

        with gr.Row():
            with gr.Column():
                gr.Markdown("## Input Settings")
                gr.Markdown(
                    "Recommended start: 30 inference steps, 0.75 image strength, and guidance scale 7.5."
                )
                input_image = gr.Image(
                    label="Original Image",
                    type="pil"
                )
                predefined_style = gr.Dropdown(
                    choices=["Custom Prompt"] + list(PREDEFINED_STYLE_PROMPTS.keys()),
                    value="Custom Prompt",
                    label="Select Predefined Style"
                )
                style_prompt = gr.Textbox(
                    label="Style Description",
                    placeholder="Example: watercolor painting with soft colors and cinematic lighting"
                )
                image_strength = gr.Slider(
                    minimum=0.1,
                    maximum=1.0,
                    value=DEFAULT_IMAGE_STRENGTH,
                    step=0.05,
                    label="Image Strength",
                    info="Lower values preserve more of the original image. Higher values allow stronger changes."
                )
                inference_steps = gr.Slider(
                    minimum=10,
                    maximum=100,
                    value=DEFAULT_INFERENCE_STEPS,
                    step=1,
                    label="Inference Steps",
                    info="More steps can improve quality, but generation takes longer."
                )
                guidance_scale = gr.Slider(
                    minimum=1.0,
                    maximum=20.0,
                    value=DEFAULT_GUIDANCE_SCALE,
                    step=0.5,
                    label="Guidance Scale",
                    info="Higher values make the model follow the style prompt more strongly."
                )
                seed_number = gr.Number(
                    label="Random Seed (Optional)",
                    info="Leave empty for a random result, or enter a whole number to repeat a result.",
                    precision=0
                )

            with gr.Column():
                gr.Markdown("## Results")
                gr.Markdown(
                    "Compare the original preview with the generated result, then download the final image."
                )
                image_preview = gr.Image(
                    label="Original Preview",
                    type="pil"
                )
                generated_image = gr.Image(
                    label="Stylized Image",
                    type="pil"
                )
                generation_status = gr.Textbox(
                    label="Generation Status",
                    value="Ready. Upload an image, describe a style, then click Generate.",
                    interactive=False
                )
                download_image = gr.File(
                    label="Download Stylized Image",
                    interactive=False
                )

        preview_button = gr.Button("Preview Original Image")
        generate_button = gr.Button("Generate Stylized Image")
        clear_button = gr.Button("Clear")

        preview_button.click(
            fn=show_uploaded_image,
            inputs=input_image,
            outputs=image_preview
        )

        predefined_style.change(
            fn=get_predefined_style_prompt,
            inputs=predefined_style,
            outputs=style_prompt
        )

        generate_button.click(
            fn=generate_stylized_image,
            inputs=[
                input_image,
                style_prompt,
                image_strength,
                guidance_scale,
                inference_steps,
                seed_number
            ],
            outputs=[
                generated_image,
                generation_status,
                download_image
            ]
        )

        clear_button.click(
            fn=clear_interface,
            inputs=None,
            outputs=[
                input_image,
                predefined_style,
                style_prompt,
                image_strength,
                inference_steps,
                guidance_scale,
                seed_number,
                image_preview,
                generated_image,
                generation_status,
                download_image
            ]
        )

    return demo
