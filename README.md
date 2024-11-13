# Whisper GUI

## Requirements

- whisper
- nicegui
- openpyxl
- pywebview

## Developer

### Setup

1. Create a virtual environment: .venv  
    Make sure to initialize the virtual environment using the correct python version (3.9 or 3.10 see notes):
    > C:\Users\\[UserName]\AppData\Local\Programs\Python\Python39\python.exe -m venv .venv
2. Activate the virtual environment  
    > .venv\Scripts\activate
3. Install the following dependencies:
    - (.venv) ...> pip install git+https://github.com/openai/whisper.git
    - (.venv) ...> pip install blobfile
    - (.venv) ...> pip install nicegui 
    - (.venv) ...> pip install openpyxl


## Offline Use

Add a folder `.cache\whisper` to your project. Move the files **vocab.bpe** and **encoder.json** to this folder. Update file links in your local copy of openai_public.py which will be installed in your python folder e.g. `.venv\Lib\site-packages\tiktoken_ext\openai_public.py` to point to `.cache\whisper`.
            Remove the URL "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/" and replace it with your local copy, e.g.  
        ```
        def gpt2():
        mergeable_ranks = data_gym_to_mergeable_bpe_ranks(
            vocab_bpe_file="C:/Users/[Username]/whisper_gui/.cache/whisper/vocab.bpe",
            encoder_json_file="C:/Users/[Username]/whisper_gui/.cache/whisper/encoder.json",
        )
        ```

### Notes

> As of now (2024/10/19) Whisper works with Python **3.9** or **3.10**. Make sure to select correct version in your IDE (note to self: in VS Code select Python 3.9.0 ('.venv') in lower right corner).

> Its best practice to setup a virtual environment for the project. Make sure to activate it (`.\.venv\Scripts\activate`) before installing libraries!
