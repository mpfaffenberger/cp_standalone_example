# 🐄👁️ Bessie the Computer Vision Cow

A standalone example of building custom agents with [code-puppy](https://github.com/mpfaffenberger/code-puppy).

**Bessie is a Computer Vision expert cow that counts animals in images using OpenCV.** She can look at your photos, write Python/OpenCV detection scripts, execute them, and report how many animals she found. Moo!

## Requirements

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Installation

```bash
cd cp_standalone_example
uv sync
```

## Usage

```bash
# Count animals in an image
uv run animal-counter "Count the elk in Elk-Count.jpg"

# Interactive mode
uv run animal-counter
```

## How Bessie Works

1. **Sees the image** via `load_image_for_analysis` tool
2. **Writes OpenCV code** using `edit_file` to detect and count animals
3. **Runs the script** with `agent_run_shell_command`
4. **Reports results** with annotated output images

## Example

```
Prompt (example: Count elk in Elk-Count.jpg) >>> Count the cows in pasture.jpg

Bessie: Moo! 🐄 Looking at that image...
        I can see 3 Holstein dairy cows in the field.
        I've saved an annotated version to pasture_detected.jpg
        with bounding boxes around each cow!
```

## Files

- `animal_counter.py` - The agent (44 lines)
- `cow_prompt.md` - System prompt with CV expertise
- `pyproject.toml` - Just depends on `code-puppy==0.0.387`

## License

MIT
