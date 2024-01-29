# exr_reader
Read EXR files exported with BAT

## Usage

Use the `OpenEXRReader` in a with statement:
```python
with OpenEXRReader(PATH, CHSTR) as exr:
    ...
```

See the `OpenEXRReader` class description for detailed usage, and [test.py](https://github.com/karolyartur/exr_reader/blob/ee6ca3a057a1faebd7341cb01cf2d2740390075e/test/test.py) for an example