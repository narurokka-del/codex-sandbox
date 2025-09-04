# gemini-flash-image-python

Generate images with the Gemini API using Python.

## Requirements
- Python 3.9+
- Google Gen AI Python SDK (`google-genai`)
- Pillow

## API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and create a key for the Developer API.
2. Set the key in your environment. On Windows PowerShell:
   ```powershell
   $env:GEMINI_API_KEY="YOUR_KEY"
   ```
3. Alternatively, copy `.env.example` to `.env` and set the key there. The script reads `os.environ["GEMINI_API_KEY"]`.

## Setup & Usage (Windows 10)
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -U google-genai pillow
python main.py --prompt "白背景、花が細かく敷き詰められた横長の帯"
```

After running, the script saves `output.png` and prints its dimensions:
```
Saved: output.png (W×H px)
```

## Notes
- Model: `gemini-2.5-flash-image-preview` (preview; outputs images with the long side around ~1024px).
- CLI accepts the `--prompt` argument for the text description.
