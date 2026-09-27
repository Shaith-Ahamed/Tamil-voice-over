# Gemini Text-to-Speech

A simple Python project for generating speech using the Google Gemini Text-to-Speech API.

## Project Structure

```text
Voice/
└── generate_voiceover.py
```

## Requirements

* Python 3.10 or newer
* Google Gemini API key
* Internet connection

## 1. Install the Required Package

Open PowerShell in the project folder and run:

```powershell
python -m pip install -U google-genai
```

## 2. Set the API Key

The API key is provided through the terminal and is not stored in the project files.

In PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

Check that it is set:

```powershell
echo $env:GEMINI_API_KEY
```

Do not share or commit the API key.

## 3. Run the Program

Navigate to the project folder:

```powershell
cd "C:\Users\shait\OneDrive\Desktop\Voice"
```

Then run:

```powershell
python generate_voiceover.py
```

## 4. Getting Proper Tamil Script

For Tamil narration, use proper Tamil Unicode script instead of English-letter transliteration.

Example:

```text
Transliteration:
ungalku thewayana thigathi matrum neratthai theriwu seyyungal

Tamil script:
உங்களுக்கு தேவையான திகதி மற்றும் நேரத்தைத் தெரிவு செய்யுங்கள்.
```

Before generating the audio:

1. Convert the transliterated Tamil into proper Tamil Unicode.
2. Check the spelling and grammar.
3. Use natural Tamil wording.
4. Keep commonly used English technical terms where appropriate.
5. Add punctuation to create natural pauses.

## 5. Running Again

The API key set with:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

is available for the current PowerShell session.

If you close PowerShell and open a new terminal, set the API key again before running the program.

## 6. Troubleshooting

### Package not found

If you get:

```text
ModuleNotFoundError: No module named 'google'
```

run:

```powershell
python -m pip install -U google-genai
```

### API key error

Make sure the key is set:

```powershell
echo $env:GEMINI_API_KEY
```

Then run:

```powershell
python generate_voiceover.py
```

### Python version

Check your Python version:

```powershell
python --version
```

## Security

Do not:

* Put the API key directly into the Python source code.
* Upload the API key to GitHub.
* Share the API key with others.

Use the PowerShell environment variable instead.
