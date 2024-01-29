import os
import sys
current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.dirname(current_dir_path)
sys.path.append(parent_dir_path)

from exr_reader import OpenEXRReader


if __name__=='__main__':
    filepath = os.path.join(current_dir_path,'0001.exr')

    with OpenEXRReader(filepath,'rgb') as exr:
        print('Header of the exr file:\n{}'.format(exr.header))
        print('Channel names: {}'.format(exr.channel_names))
        print('Data type of channel with default loader: {}\n'.format(type(exr.r)))


    import numpy as np
    import matplotlib.pyplot as plt

    with OpenEXRReader(filepath,'nxnynz', np) as exr:
        print('Data type of channel with numpy loader: {}'.format(type(exr.nx)))
        r = np.reshape(exr.nx,(exr.resolution))
        g = np.reshape(exr.ny,(exr.resolution))
        b = np.reshape(exr.nz,(exr.resolution))
        plt.imshow(np.moveaxis(np.stack([r,g,b]),[0],[2]))
        plt.show()
    
    import torch
    with OpenEXRReader(filepath,'c', torch) as exr:
        print('Data type of channel with torch loader: {}'.format(type(exr.c)))

    with OpenEXRReader(filepath,'fxfyfzfw', np) as exr:
        fx = np.reshape(exr.fx,(exr.resolution))
        fy = np.reshape(exr.fy,(exr.resolution))
        fz = np.reshape(exr.fz,(exr.resolution))
        fw = np.reshape(exr.fw,(exr.resolution))
        print(fx.max(),fy.max(),fz.max(),fw.max())