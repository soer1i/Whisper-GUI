# Whisper GUI

An interface to streamline transcriptions using Whisper.  

- transcribe video files up to ~ 25 MiB
- transcribe audio files of any size  
     *(Audio files larger than 25 MiB are split into segments with an overlap of 2 seconds. Finally the segment transcriptions are merged.)*

## Requirements

- whisper (see requirements online)
- nicegui
- pywebview
- openpyxl
- pydub

## Developer

### Notes

| :snake: Python Version |
|:-|
| As of now (2024/10/19) Whisper works with Python **3.9** or **3.10**. Make sure to select correct version in your IDE (note to self: in VS Code select Python 3.9.0 ('.venv') in lower right corner). |

| :information_source: Virtual Environment |
|:-|
| Its best practice to setup a virtual environment for the project. Make sure to activate it (`.\.venv\Scripts\activate`) before installing libraries! |

### Setup Example

1. Create a virtual environment: .venv  
    Make sure to initialize the virtual environment using the correct python version (3.9 or 3.10 see notes):
   
       C:\Users\\[UserName]\AppData\Local\Programs\Python\Python39\python.exe -m venv .venv
   
3. Activate the virtual environment
   
       .venv\Scripts\activate
   
5. Install the following dependencies (activate .venv !):
   
       pip install git+https://github.com/openai/whisper.git  
       pip install blobfile  
       pip install nicegui  
       pip install pywebview
       pip install openpyxl
       pip install pydub

## Whisper Offline Use

Add folder `C:\Users\[UserName]\.cache\whisper`. Move the files **vocab.bpe** and **encoder.json** to this folder. Update your local copy of openai_public.py. If you created a venv this file is located in `.venv\Lib\site-packages\tiktoken_ext\openai_public.py` otherwise it probably is in `C:\Users\[UserName]\AppData\Local\Programs\Python\Python310-32\Lib\site-packagespython3.9\site-packages\tiktoken_ext\openai_public.py`. Remove the URL "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/" and replace it with your local copy, e.g.:
            
        def gpt2():
        mergeable_ranks = data_gym_to_mergeable_bpe_ranks(  
            vocab_bpe_file="C:/Users/[Username]/whisper_gui/.cache/whisper/vocab.bpe",   
            encoder_json_file="C:/Users/[Username]/whisper_gui/.cache/whisper/encoder.json",  
        )

## Build Executable

0. first time, install pyinstaller in python environment
    
       (.venv) pip install pyinstaller

1. run nicegui-pack

       (.venv) ...> nicegui-pack --windowed --name "Whisper Interface" main.py

2. copy the following folders to `.\dist\Whisper Interface\_internal`
    - `.\.venv\Lib\site-packages\whisper`
    - `.\.venv\Lib\site-packages\tiktoken_ext`