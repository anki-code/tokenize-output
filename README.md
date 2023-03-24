<p align="center">
Get identifiers, names, paths, URLs and words from the command output.<br> 
The <a href="https://github.com/anki-code/xontrib-output-search">xontrib-output-search</a> for <a href="https://xon.sh/">xonsh shell</a> is using this library.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned by watching releases.
</p>

## Install
```shell script
pip install -U tokenize-output
```

## Usage

You can use `tokenize-output` command as well as export the tokenizers in Python:
```python
from tokenize_output.tokenize_output import *
tokenizer_split("Hello world!")
# {'final': set(), 'new': {'Hello', 'world!'}}
```

#### Words tokenizing
```shell script
echo "Try https://github.com/xxh/xxh" | tokenize-output -p
# Try
# https://github.com/xxh/xxh
```

#### JSON, Python dict and JavaScript object tokenizing
```shell script
echo '{"Try": "xonsh shell"}' | tokenize-output -p
# Try
# shell
# xonsh
# xonsh shell
```    

#### env tokenizing
```shell script
echo 'PATH=/one/two:/three/four' | tokenize-output -p
# /one/two
# /one/two:/three/four
# /three/four
# PATH
```    

## Development

### Tokenizers
Tokenizer is a functions which extract tokens from the text.

| Priority | Tokenizer  | Text  | Tokens |
| ---------| ---------- | ----- | ------ |
| 1        | **dict**   | `{"key": "val as str"}` | `key`, `val as str` |
| 2        | **env**    | `PATH=/bin:/etc` | `PATH`, `/bin:/etc`, `/bin`, `/etc` |   
| 3        | **split**  | `Split  me \n now!` | `Split`, `me`, `now!` |   
| 4        | **strip**  | `{Hello}` | `Hello` |   

You can create your tokenizer and add it to `tokenizers_all` in `tokenize_output.py`.

Tokenizing is a recursive process where every tokenizer returns `final` and `new` tokens. 
The `final` tokens directly go to the result list of tokens. The `new` tokens go to all 
tokenizers again to find new tokens. As result if there is a mix of json and env data 
in the output it will be found and tokenized in appropriate way.  

### How to add tokenizer

You can start from `env` tokenizer:

1. [Prepare regexp](https://github.com/tokenizer/tokenize-output/blob/25b930cfadf8291e72a72144962e411e47d28139/tokenize_output/tokenize_output.py#L10)
2. [Prepare tokenizer function](https://github.com/tokenizer/tokenize-output/blob/25b930cfadf8291e72a72144962e411e47d28139/tokenize_output/tokenize_output.py#L57-L70)
3. [Add the function to the list](https://github.com/tokenizer/tokenize-output/blob/25b930cfadf8291e72a72144962e411e47d28139/tokenize_output/tokenize_output.py#L139-L144) and [to the preset](https://github.com/tokenizer/tokenize-output/blob/25b930cfadf8291e72a72144962e411e47d28139/tokenize_output/tokenize_output.py#L147).
4. [Add test](https://github.com/tokenizer/tokenize-output/blob/25b930cfadf8291e72a72144962e411e47d28139/tests/test_tokenize.py#L34-L35).
5. Now you can test and debug (see below).

### Test and debug
Run tests:
```shell script
cd ~
git clone https://github.com/anki-code/tokenize-output
cd tokenize-output
python -m pytest tests/
```
To debug the tokenizer:
```shell script
echo "Hello world" | ./tokenize-output -p
```

## Related projects
* [xontrib-output-search][XONTRIB_OUTPUT_SEARCH] for [xonsh shell][XONSH]

[XONTRIB_OUTPUT_SEARCH]: https://github.com/anki-code/xontrib-output-search
[XONSH]: https://xon.sh/
