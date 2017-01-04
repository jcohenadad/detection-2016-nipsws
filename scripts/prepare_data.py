# !/usr/bin/env python
#
# Prepare training and testing datasets from MRI.
# MRI data need to have a label at C2-C3 disc.
# Julien Cohen-Adad

import sys
import os
import numpy as np
import nipy
from matplotlib.pylab import *

# Path to SCT
path_sct = '/Users/julien/code/sct/'  # slash at the end
sys.path.append(path_sct + 'scripts/')
from isct_test_function import generate_data_list
from sct_image import Image
import sct_utils as sct

# Parameters
path_data = '/Users/julien/data/sct_test_function/'  # Path to MRI data (slash at the end)
contrast = 't2'  # contrast to use


def resample_to_1mm(nii):
    """
    Resample to 1mm iso
    :param nii: input nipy image
    :return: resampled nipy image
    """
    # from nipy.algorithms.registration import resample
    # from nipy.core.api import Image, AffineTransform
    import numpy as np
    from nipy.algorithms import registration
    interp_order = 2  # spline
    # Load data
    data = nii.get_data()
    # Get dimensions of data
    p = nii.header.get_zooms()
    n = nii.header.get_data_shape()
    # Calculate new dimensions
    new_size = [1, 1, 1]
    # compute new shape as: n_r = n * (p / p_r)
    n_r = tuple([int(round(n[i] * float(p[i]) / float(new_size[i]))) for i in range(len(n))])
    # get_base_affine()
    affine = nii.coordmap.affine
    # create ref image
    arr_r = np.zeros(n_r)
    R = np.eye(len(n) + 1)
    for i in range(len(n)):
        R[i, i] = n[i] / float(n_r[i])
    affine_r = np.dot(affine, R)
    coordmap_r = nii.coordmap
    coordmap_r.affine = affine_r
    nii_r = nipy.core.api.Image(arr_r, coordmap_r)
    # create affine transformation
    transfo = R
    # translate to account for voxel size (otherwise resulting image will be shifted by half a voxel). Modify the three first rows of the last column, corresponding to the translation.
    transfo[:3, -1] = np.array(((R[0, 0] - 1) / 2, (R[1, 1] - 1) / 2, (R[2, 2] - 1) / 2), dtype='f8')
    # resample data
    nii_r = registration.resample(nii, transform=transfo, reference=nii_r, mov_voxel_coords=True,
                                              ref_voxel_coords=True, dtype='double', interp_order=interp_order,
                                              mode='nearest')
    return nii_r


def onclick(event):
    """
    get click from figure
    :param event:
    :return:
    """
    global ix, iy
    ix, iy = event.xdata, event.ydata
    # print 'x = %d, y = %d' % (
    #     ix, iy)

    global coords
    coords.append((ix, iy))
    # quit after one click
    if len(coords) == 1:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return coords

if __name__ == "__main__":

    # generate subject list
    list_path_subjects, list_name_subjects = generate_data_list(path_data)

    # remove subjects without data
    for path_subject in list_path_subjects:
        if not os.path.exists(path_subject + contrast + '/' + contrast + '.nii.gz'):
            list_path_subjects.pop(list_path_subjects.index(path_subject))

    # Loop across subjects
    for path_subject in list_path_subjects:

        # Open MRI data
        fname_data = path_subject + contrast + '/' + contrast + '.nii.gz'
        im = Image(fname_data)

        # Reorient to RPI
        im.change_orientation('RPI')
        # TODO: do not save! instead, pass as nibabel object for resampling
        im.setFileName('temp.nii.gz')
        im.save()

        # Resample to 1mm iso
        # TODO: do not open data another time (here we do it to have nibabel objects)
        nii = nipy.load_image('temp.nii.gz')
        data1mm = resample_to_1mm(nii).get_data()

        # Average from mid-plane across R-L direction
        data2d = np.sum(data1mm, axis=0)

        # Open label data
        fig = plt.figure()
        matshow(data2d, fignum=1, cmap=cm.gray)
        coords = []
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        plt.show(1)
        print coords


        # Get bounding box from label

        # Save image

        # Save Annotation as json file