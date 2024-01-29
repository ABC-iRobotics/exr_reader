# Read EXR files exported with BAT

The OpenEXR library should be installed on the system before using this code. The installation can be done by:
```
sudo apt-get install libopenexr-dev zlib1g-dev
pip install --no-binary openexr openexr
```

## Usage

Use the `OpenEXRReader` in a with statement:
```python
with OpenEXRReader(PATH, CHSTR) as exr:
    ...
```

The data in the EXR file can be accessed through the attributes of the `exr` variable. The existence of these attributes depends on the channel string (`CHSTR`).

For example, when loading the R,G and B channels:
```python
with OpenEXRReader(PATH, 'rgb') as exr:
    r_channel = exr.r
    g_channel = exr.g
    b_channel = exr.b
```
will work fine, but
```python
with OpenEXRReader(PATH, 'rgb') as exr:
    r_channel = exr.r
    g_channel = exr.g
    b_channel = exr.b
    a_channel = exr.a
```
will result in an `AttributeError` because the alpha channel is not loaded (for that, the channel string should be `'rgba'`). See the `OpenEXRReader` class description for the list of all channel keys that can be used in the channel string.

Additionally, a loader can be specified. When using the default loader (`None`), the channels will be loaded as 1D Python lists (using the built-in `array.array`).
NumPy and PyTorch can also be used as loaders, in which case, the loaded channels will be 1D NumPy arrays or PyTorch tensors, respectively:

```python
with OpenEXRReader(PATH, 'a') as exr:
    type(exr.a)  # list
```

```python
import numpy as np
with OpenEXRReader(PATH, 'a', np) as exr:
    type(exr.a)  # np.array
```

```python
import torch
with OpenEXRReader(PATH, 'a', torch) as exr:
    type(exr.a)  # torch.Tensor
```


See [test/test.py](test/test.py) for further examples.