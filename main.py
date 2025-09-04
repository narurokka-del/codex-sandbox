from google import genai
import os
import argparse
from io import BytesIO
from PIL import Image


def run(prompt: str) -> None:
    api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
    res = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt],
    )
    for part in res.candidates[0].content.parts:
        if getattr(part, "inline_data", None):
            img = Image.open(BytesIO(part.inline_data.data))
            img.save("output.png")
            print(f"Saved: output.png ({img.width}x{img.height}px)")
            return
    raise RuntimeError("No image returned")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image using Gemini API")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    args = parser.parse_args()
    run(args.prompt)
