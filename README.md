# ESPnet TTS Frontend
Text frontend for ESPnet tts recipes

## Install
```bash
pip install git+https://github.com/espnet/espnet_tts_frontend
```

### Install with pyopenjtalk

```bash
git clone https://github.com/espnet/espnet_tts_frontend
git submodule update --init --recursive
python setupy pyopenjtalk
# OR
# pip install --global-option=pyopenjtalk -e espnet_tts_frontend
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
