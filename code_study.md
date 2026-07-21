# Custom Style Prompt Suggestions

## `get_predefined_style_prompt`

```python
def get_predefined_style_prompt(style_name):
    return PREDEFINED_STYLE_PROMPTS.get(style_name, "")
```

**Input parameter:** `style_name` is the name selected in the **Select Predefined Style** dropdown.

**Output:** The matching Stable Diffusion prompt. It returns an empty string when the user selects **Custom Prompt**.

**How it works:**

1. The `PREDEFINED_STYLE_PROMPTS` dictionary stores a readable style name beside its full prompt.
2. The function looks up the selected name in that dictionary.
3. If it finds a match, it returns the prompt to the interface.
4. If there is no match, it returns an empty prompt so the user can write their own description.

**Why this function exists:** Keeping the prompt lookup in `app/config.py` separates the prompt data from the interface code. This makes it easy for beginners to add or edit suggested styles later.

## Dropdown Change Handler

```python
predefined_style.change(
    fn=get_predefined_style_prompt,
    inputs=predefined_style,
    outputs=style_prompt
)
```

**Input:** The selected dropdown value.

**Output:** The existing **Style Description** textbox.

**How it works:** Gradio calls `get_predefined_style_prompt` whenever the dropdown selection changes. The returned text is placed into the style prompt textbox. Users can then keep that text, edit it, or replace it with their own custom prompt before generating an image.

**Why this exists:** It provides quick, Stable Diffusion-ready suggestions while preserving the original custom prompt workflow and image generation behavior.

## `clear_interface`

```python
def clear_interface():
    return (
        None,
        "Custom Prompt",
        "",
        # Remaining original control values...
    )
```

**Input parameters:** None. The Clear button calls this function without sending any values.

**Output:** A set of default values for every interface component, including `"Custom Prompt"` for the new dropdown, an empty style description, and the shared values from `app/config.py`.

**How it works:** The function returns values in the same order as the components listed in the Clear button's `outputs` list. The dropdown is reset before the textbox, so both prompt controls return to their starting state together. It imports the shared default values so the Clear button and sliders stay consistent.

**Why this function was updated:** The new dropdown is an interface component, so it needs a matching return value when the user clears the form. This keeps the clear button working correctly after adding Custom Style Prompt Suggestions.
