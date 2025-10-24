# Whisper GUI

An interface to streamline transcriptions using Whisper.  

- transcribe audio files
     *(Audio files larger than 25 MiB are split into segments with an overlap of 2 seconds. Finally the segment transcriptions are merged.)*
- transcribe video files
     *(Audio is extracted and saved to the directory of the video file.)*

![Screenshot of Whisper GUI](./docs/whisper_gui_screenshot.png?raw=true)

## Requirements

- whisper (see requirements online)
- nicegui
- pywebview
- openpyxl
- pydub
- simpleaudio

## Developer

### Notes

| :snake: Python Version |
|:-|
| As of now (2024/10/19) Whisper works with Python **3.9** or **3.10**. Make sure to select correct version in your IDE (note to self: in VS Code select Python 3.9.0 ('.venv') in lower right corner). |

| :information_source: Virtual Environment |
|:-|
| Its best practice to setup a virtual environment for the project. Make sure to activate it (windows: `.\.venv\Scripts\activate`, ubuntu: `source .venv\bin\activate`) before installing libraries! |

### Setup Example

1. Create a virtual environment: .venv  
    Make sure to initialize the virtual environment using the correct python version (3.9 or 3.10 see notes):
   
       C:\Users\\[UserName]\AppData\Local\Programs\Python\Python39\python.exe -m venv .venv
   
2. Activate the virtual environment
   
       windows: .venv\Scripts\activate
       ubuntu: source .venv\bin\activate
   
3. Install the following dependencies
   
       pip install git+https://github.com/openai/whisper.git  
       pip install blobfile  
       pip install nicegui  
       pip install openpyxl
       pip install pydub

       windows / mac:
       - pip install simpleaudio
       ubuntu:
       - terminal: sudo apt-get install -y python3.9-dev libasound2-dev
       - venv: pip install simpleaudio

       windows / mac:
       - pip install pywebview 
       ubuntu: 
       - pip install pywebview[qt] (note to self: Had to run `sudo apt install libxcb-cursor0` in terminal for qt to run on ubuntu 24)

4. To use the GUI on your machine, make sure pre-requisites (mainly NVIDIA CUDA and FFMPEG) are installed. See https://github.com/openai/whisper/discussions/1463 for more info.

(note to self: Because of an older GPU I had to install pytorch CUDA 12.6)

### Build Executable

0. first time, install pyinstaller in python environment
    
       (.venv) pip install pyinstaller

1. run nicegui-pack

       (.venv) nicegui-pack --windowed --name "Whisper GUI" main.py

2. copy the following files and folders to `.\dist\Whisper GUI\_internal`
    - `sound_effect_finished.wav`
    - `.\.venv\Lib\site-packages\whisper`
    - `.\.venv\Lib\site-packages\tiktoken_ext`

## Whisper Offline Use

Add folder `C:\Users\[UserName]\.cache\whisper`. Move the files **docs/vocab.bpe** and **docs/encoder.json** to this folder. Update your local copy of openai_public.py. If you created a venv this file is located in `.venv\Lib\site-packages\tiktoken_ext\openai_public.py` otherwise it probably is in `C:\Users\[UserName]\AppData\Local\Programs\Python\Python310-32\Lib\site-packagespython3.9\site-packages\tiktoken_ext\openai_public.py`. Remove the URL "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/" and replace it with your local copy, e.g.:
            
        def gpt2():
        mergeable_ranks = data_gym_to_mergeable_bpe_ranks(  
            vocab_bpe_file="C:/Users/[Username]/.cache/whisper/vocab.bpe",   
            encoder_json_file="C:/Users/[Username]/.cache/whisper/encoder.json",  
        )
        
## Pyannote Offline Use

My attempts to get pyannote.audio run offline where quite frustrating. It might be that it is easier to do so on newer systems. Following are some notes that might help others.

### Ubuntu

1. Make sure to install git lfs.  
2. Get pyannot offline model from huggingface (eg. model: *speaker-diarization-community-1*).
3. Move *model.bin* files and *config.yaml* to project. Make sure to rename everything in *config.yaml* accordingly. The model links in the yaml file are relative to the project environment.
4. Install numpy in python environment.
5. Install pytorch in python environment. Either install the CPU version, or make sure it matches the cuda version installed on the system.
       - check installed cuda version. terminal: `nvcc --version`
       - check which version to install https://pytorch.org/get-started/previous-versions/
       - in my case I installed `pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu`
6. Install pyannote.audio in python environment.
       - make sure to install it with the same version as pytorch
       - in my case I installed `pip install pyannote.audio --extra-index-url https://download.pytorch.org/whl/cpu`