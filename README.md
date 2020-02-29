# ESPnet TTS Frontend
Text frontend for ESPnet tts recipes

## Install
```bash
git clone https://github.com/espnet/espnet_tts_frontend
pip install -e espnet_tts_frontend
# OR
# pit install git+https://github.com/espnet/espnet_tts_frontend
```

### Install with pyopenjtalk

- Requires cmake and cython

```bash
git clone https://github.com/espnet/espnet_tts_frontend
cd espnet_tts_frontend/
git submodule update --init --recursive
python setup.py pyopenjtalk
# OR
# pip install --global-option=pyopenjtalk git+https://github.com/espnet/espnet_tts_frontend
```

## Usage

### English:
#### tacotron_cleaner
Derived from https://github.com/keithito/tacotron

```python
>>> import tacotron_cleaner.cleaners
>>> tacotron_cleaner.cleaners.custom_english_cleaners("(Hello-World);   &  jr. & dr.")
'HELLO WORLD, AND JUNIOR AND DOCTOR'
```
#### g2p_en
https://github.com/Kyubyong/g2p

```python
>>> from g2p_en import G2p  # Automatically run downloading for the first time, 
[nltk_data] Downloading package averaged_perceptron_tagger to
...
>>> g2p = G2p()
>>> g2p("hello world")
['HH', 'AH0', 'L', 'OW1', ' ', 'W', 'ER1', 'L', 'D']
```

### Japanese
#### jaconv
https://github.com/ikegami-yukino/jaconv/

```python
>>> jaconv.normalize("”あらゆる”　現実を　〜　’すべて’ 自分の　ほうへ　ねじ曲げたのだ。")
'"あらゆる" 現実を ー \'すべて\' 自分の ほうへ ねじ曲げたのだ。'
```

#### pyopenjtalk

```python
>>> pyopenjtalk.g2p("あらゆる 現実を すべて 自分の ほうへ ねじ曲げたのだ。", kana=True)
'アラユル\u3000ゲンジツヲ\u3000スベテ\u3000ジブンノ\u3000ホーエ\u3000ネジマゲタノダ。'
>>> pyopenjtalk.g2p("あらゆる 現実を すべて 自分の ほうへ ねじ曲げたのだ。", kana=False)
'a r a y u r u pau g e N j i ts u o pau s u b e t e pau j i b u N n o pau h o o e pau n e j i m a g e t a n o d a'
```

### Vietnamese
#### vietnamese_cleaner

```python
>>> import vietnamese_cleaner.vietnamese_cleaner
```
