# ESPnet TTS Frontend
Text frontend for ESPnet tts recipes

## Install
```bash
git clone https://github.com/espnet/espnet_tts_frontend
pip install -e .
# OR
# pit install git+https://github.com/espnet/espnet_tts_frontend
```

### Install with pyopenjtalk

```bash
git clone https://github.com/espnet/espnet_tts_frontend
git submodule update --init --recursive
python setup.py pyopenjtalk
# OR
# pip install --global-option=pyopenjtalk git+https://github.com/espnet/espnet_tts_frontend
```

## Usage

### tacotron_cleaner
Derived from https://github.com/keithito/tacotron

```python
>>> import tacotron_cleaner.cleaners
>>> tacotron_cleaner.cleaners.custom_english_cleaners("(Hello-World);   &  jr. & dr.")
'HELLO WORLD, AND JUNIOR AND DOCTOR'
```

### vietnamese_cleaner

```python
>>> import vietnamese_cleaner.vietnamese_cleaner
```
