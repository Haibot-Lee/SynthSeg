import os
import pandas as pd
import numpy as np
import nibabel as nib


def print_labels(p):
    print(os.path.basename(p))
    labels = np.load(p)
    print(labels)
    print(labels.shape)
    print()


# data_path = '../data_training/nifti'
# all_vals = np.ndarray([]).astype(int)
# for file in os.listdir(data_path):
#     img = nib.load(os.path.join(data_path, file))
#     img_fdata = img.get_fdata()
#     union_val = np.unique(
#         (img_fdata.reshape([img_fdata.shape[0] * img_fdata.shape[1] * img_fdata.shape[2]]))).astype(int)
#     all_vals = np.union1d(all_vals, union_val)
#
# print(all_vals)
# print(len(all_vals))
# np.save('../data_training/labels/generation_labels.npy', all_vals)

mapping_df = pd.read_csv('labels/SynthSeg_Idx_parc.csv')

self_def_gen_labels = np.array(mapping_df['index'].tolist())
# np.save('labels/generation_labels.npy', self_def_gen_labels)
print_labels('labels/generation_labels.npy')

seg_names = np.array(mapping_df['label'].tolist())
# np.save('labels/segmentation_names.npy', seg_names)
print_labels('labels/segmentation_names.npy')

output_labes = np.array(mapping_df['output'].tolist())
# np.save('labels/output_labels.npy', output_labes)
print_labels('labels/output_labels.npy')

gen_classes = np.array(mapping_df['class'].tolist()).astype(int)
np.save('labels/generation_classes.npy', gen_classes)
print_labels('labels/generation_classes.npy')
