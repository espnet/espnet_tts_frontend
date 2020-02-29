# ESPnet TTS Cleaners
Collection of text cleaners for ESPnet tts recipes

## Install
```
pip install git+https://github.com/espnet/espnet_tts_cleaners
```

## tacotron_cleaner
Derived from https://github.com/keithito/tacotron

```python
>>> import tacotron_cleaner.cleaners
>>> tacotron_cleaner.cleaners.custom_english_cleaners("(Hello-World);   &  jr. & dr.")
'HELLO WORLD, AND JUNIOR AND DOCTOR'
```

## vietnamese_cleaner

```python
>>> import vietnamese_cleaner.vietnamese_cleaner
```
