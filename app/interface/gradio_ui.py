import gradio as gr

from app.services.image_generator import generate_stylized_image

from app.config import (
    DEFAULT_IMAGE_STRENGTH,
    DEFAULT_INFERENCE_STEPS,
    DEFAULT_GUIDANCE_SCALE
)



def show_uploaded_image(image):

    return image



def create_gradio_interface():


    with gr.Blocks() as demo:


        gr.Markdown(
            "# AI Image-to-Image Style Converter"
        )


        input_image = gr.Image(
            type="pil",
            label="Upload Image"
        )


        prompt = gr.Textbox(
            label="Style Prompt"
        )


        strength = gr.Slider(
            0.1,
            1.0,
            value=DEFAULT_IMAGE_STRENGTH,
            label="Image Strength"
        )


        steps = gr.Slider(
            10,
            100,
            value=DEFAULT_INFERENCE_STEPS,
            label="Inference Steps"
        )


        guidance = gr.Slider(
            1,
            20,
            value=DEFAULT_GUIDANCE_SCALE,
            label="Guidance Scale"
        )


        seed = gr.Number(
            label="Seed"
        )


        output = gr.Image(
            label="Generated Image"
        )


        status = gr.Textbox(
            label="Status"
        )


        button = gr.Button(
            "Generate"
        )



        button.click(

            generate_stylized_image,

            inputs=[
                input_image,
                prompt,
                strength,
                guidance,
                steps,
                seed
            ],

            outputs=[
                output,
                status
            ]
        )


    return demo