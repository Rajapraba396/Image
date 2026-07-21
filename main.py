from app.interface.gradio_ui import create_gradio_interface


if __name__ == "__main__":

    application = create_gradio_interface()

    application.launch(share=True)