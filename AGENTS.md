# AGENTS.md

## Project Overview

This project is an AI-Powered Image-to-Image Style Converter using Stable Diffusion.

Goal:

Core Features

1. Upload an image

2. Preview uploaded image

3. Enter style prompt

4. Select image strength

5. Configure inference steps

6. Configure guidance scale

7. Choose random seed (optional)

8. Generate stylized image

9. Compare original vs generated image

10. Download generated image

Display generation status and errors
This project is designed for beginners and will run in Google Colab.

---

## Core Rules

1. Use only Python.

2. Keep all Python backend logic inside a single file:
main.py

Non-Python files such as HTML, CSS, JavaScript, README, documentation, images, and configuration files may be created when necessary.

Do not create additional Python files unless explicitly requested.

3. Do NOT create additional Python files unless explicitly requested.

4. Code must be compatible with Google Colab.

5. Avoid advanced architecture:

* no classes unless necessary
* prefer simple functions
* avoid decorators
* avoid complex design patterns

6. Keep code beginner-friendly.

7. Every major section must have comments.

Example sections:

* Imports
* Dependency Installation
* Utility Functions
* Image Generation
* Main Execution

8. Reuse existing code whenever possible.
   Do not rewrite working code unless required.

9. Never remove old functionality while implementing new phases unless instructed.

10. If adding new code, preserve backward compatibility.

---

## Execution Restrictions (Important)

11. NEVER run any code automatically.

Do NOT:

* execute Python scripts
* run shell commands
* use terminal commands
* test code automatically

Only write or modify code.

12. NEVER download or install anything automatically.

Do NOT:

* install pip packages
* download models
* fetch files from URLs
* clone repositories
* pull HuggingFace models

Examples of forbidden actions:

* pip install torch
* pip install diffusers
* git clone ...
* wget ...
* curl ...
* model.from_pretrained(...)

Only write the code required.
The user will manually run everything later.

---

## Phase-Based Development

This project is developed in phases.

When implementing a phase:

1. Understand current phase goal
2. Modify only necessary code
3. Keep previous phases working
4. Do not execute anything
5. Update documentation

---

## Documentation Rule

After completing every phase, update:

* code_study.md

For every new or modified function, document:

1. Function name
2. Code snippet
3. Input parameters
4. Output
5. Step-by-step explanation
6. Why this function exists

Explanation must be beginner-friendly.

Assume the reader is new to:

* Python
* AI
* Stable Diffusion

Avoid unnecessary jargon.

---

## Response Workflow

Before writing code for any phase:

1. Explain implementation plan
2. Explain which functions will be added or modified
3. Wait for approval if requirements are unclear
4. Then write code

Never jump directly into code without explanation.

---

## Code Style Rules

* Use descriptive variable names
* Avoid one-letter variable names
* Keep functions small
* Prefer readability over optimization
* Add comments for non-trivial logic

Bad:
x = f(a)

Good:
generated_image = generate_stylized_image(
    input_image,
    style_prompt,
    strength
)

---

## Priority Order

Always prioritize:

1. Readability
2. Simplicity
3. Stability
4. Performance

Technology Stack

## Backend
1. Python
2. Gradio
3. Diffusers
4. Transformers
5. Torch
6. Pillow

Model
1. Stable Diffusion Image-to-Image Pipeline

Development
1. VS Code
2. Git


