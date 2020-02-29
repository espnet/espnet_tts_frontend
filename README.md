# ESPnet TTS Frontend
Text frontend for ESPnet tts recipes

## Install
```bash
pip install git+https://github.com/espnet/espnet_tts_cleaners
```

### Install with pyopenjtalk

```bash
git clone https://github.com/espnet/espnet_tts_cleaners
git submodule update --init --recursive
pip install git+https://github.com/espnet/espnet_tts_cleaners
pip install --global-option=pyopenjtalk espnet_tts_cleaners
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
