import os
import sys
current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(current_dir_path)
sys.path.append(parent_dir_path)

from exr_reader import OpenEXRReader


if __name__=='__main__':
    filepath = os.path.join(current_dir_path,'0001.exr')
    filepath_missing = os.path.join(current_dir_path,'0001_missing.exr')

    # Open the file with the default loader and load the R,G and B channels
    chstr = 'rgb'
    with OpenEXRReader(filepath, chstr) as exr:
        print('\nHeader of the exr file:{}\n'.format(exr.header))
        print('Channel names: {} (using chstr "{}")'.format(exr.channel_names, chstr))
        print('Data type of channel with default loader: {}\n'.format(type(exr.r)))


    # When accessing an unloaded channel, AttributeError is thrown
    try:
        chstr = 'c'
        with OpenEXRReader(filepath, chstr) as exr:
            print('Data type of channel with default loader: {}\n'.format(type(exr.a)))
    except AttributeError:
        print('Could not access channel(s) "{}", because they are not loaded!'.format(chstr))


    # When trying to load a channel that is not in the file TypeError is thrown
    try:
        chstr = 'd'
        with OpenEXRReader(filepath_missing, chstr) as exr:
            print('Data type of channel with default loader: {}\n'.format(type(exr.d)))
    except TypeError:
        print('Cannot load channel(s) with key(s) "{}" from file {}, because the channel is missing!'.format(chstr, filepath_missing))


    import numpy as np
    import matplotlib.pyplot as plt

    # Open the file with NumPy as the loader and load the surface normal channels
    with OpenEXRReader(filepath,'nxnynz', np) as exr:
        print('Data type of channel with numpy loader: {}'.format(type(exr.nx)))
        r = np.reshape(exr.nx,(exr.resolution))
        g = np.reshape(exr.ny,(exr.resolution))
        b = np.reshape(exr.nz,(exr.resolution))
        plt.imshow(np.moveaxis(np.stack([r,g,b]),[0],[2]))
        plt.show()
    

    import torch

    # Open the file with PyTorch as the loader and load the forward optical flow channels
    with OpenEXRReader(filepath,'fxfy', torch) as exr:
        print('Data type of channel with torch loader: {}'.format(type(exr.fx)))