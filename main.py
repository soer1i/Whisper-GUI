import os
import sys
import tqdm
from nicegui import app, ui
import asyncio
import whisper

selected_files = None

models = [
    'tiny', 'medium', 'large', 'turbo'
]
languages = [
    'Auto',
    'German',
    'English'
    'French'
]

async def choose_file():
    global selected_files
    selected_files = await app.native.main_window.create_file_dialog(allow_multiple=True)
    update_file_button()

def whisper_transcribe(files, model_str, language_str):
    global transcribe_module
    transcribe_module = whisper.load_model(model_str)
    for file in files:
        # verbose: False => only progressbar
        result = transcribe_module.transcribe(file, language=language_str, verbose=True, weights_only=True, fp16=False)
        # save text
        with open(os.path.splitext(file)[0]+'.txt', "w") as text_file:
            text_file.write(result['text'])

def get_output_language(language):
    language_return = None
    if language is not None and language != 'Auto':
        language_return = language  
    return language_return

def update_file_button():
    global selected_files
    if selected_files != None:
        run_button.enable()
        if len(selected_files) == 1:
            file_button.text = '1 file selected'
        else:    
            file_button.text = str(len(selected_files)) + ' files selected'
    else:
        run_button.disable()        
        file_button.text = 'choose audio files'

async def start_transcribing():
    global selected_files
    files = selected_files
    selected_files = None
    update_file_button()
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, lambda: whisper_transcribe(files, ui_model.value, get_output_language(ui_language.value)))

with ui.column().classes('w-full'):
    with ui.row().classes('items-center'):
        ui.icon('record_voice_over', color='primary').classes('text-4xl')
        ui.label('Whisper Transcribe').classes('text-primary').style('font-size: 150%')
    file_button = ui.button('choose audio files', icon='insert_drive_file', on_click=choose_file).style('margin-top: 8px')
    ui_model = ui.select(options=models, label='model', value='turbo').classes('w-full')
    ui_language = ui.select(options=languages, with_input=True, label='language', value='Auto').classes('w-full')
    ui.label('Results are saved in the same directory as the audio files.').style('color: #808080; font-style: italic; margin-top: 16px')
    run_button = ui.button('start', icon='auto_awesome', on_click=start_transcribing)
    run_button.disable()

ui.run(title='Whisper Transcribe', reload=False, dark=None, native=True, window_size=[300,500])
