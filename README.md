<p style="text-align: center;"><h1>Card</h1></p>

Special Request: <a href="">Albi</a>
## install library
<ul>
<li>Github</li>

```bash
$ python3 -m pip install wellcome
```
<li>Pypi</li>

```bash
$ python3 -m pip install git+https://github.com/krypton-byte/wellcome
```
</ul>

## Library

<ul>

```python
from wellcome import Wellcome
wellcome=Wellcome()
im=wellcome.create('images.png','krypton-byte')
# show Image
im.show()
#save Image
im.save('result.png')
```
</ul>

## Command Line
<ul>
<li>File</li>

```bash
$ python3 -m wellcome --capt="krypton-byte" --pic=image.png --out=out.png
```
<li>Base64</li>

```bash
$ python3 -m wellcome --capt="krypton-byte" --pic=image.png --base64
```
<li>run as server</li>

```python
$ python3 -m wellcome --server
```
</ul>

## Deploy
<ul>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/krypton-byte/wellcome/tree/master)
</ul>


## Result
<ul><img src="result.png"></ul>