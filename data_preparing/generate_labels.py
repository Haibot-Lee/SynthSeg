import os
import pandas as pd
import numpy as np
import nibabel as nib


def print_labels(p):
    labels = np.load(p)
    print(type(labels))
    print(labels)
    print(labels.shape)
    print()


print("generation labels")
# print_labels('../data/labels_classes_priors/generation_labels.npy')

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
self_def_gen_labels = np.array([
    0,
    16,
    2,
    1001,
    1002,
    1003,
    1005,
    1006,
    1007,
    1008,
    1009,
    1010,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    1018,
    1019,
    1020,
    1021,
    1022,
    1023,
    1024,
    1025,
    1026,
    1027,
    1028,
    1029,
    1030,
    1031,
    1032,
    1033,
    1034,
    1035,
    7,
    8,
    10,
    11,
    12,
    13,
    17,
    18,
    26,
    28,
    41,
    2001,
    2002,
    2003,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
    2025,
    2026,
    2027,
    2028,
    2029,
    2030,
    2031,
    2032,
    2033,
    2034,
    2035,
    47,
    49,
    50,
    51,
    52,
    53,
    54,
    58,
    60
])
print(self_def_gen_labels)
print(self_def_gen_labels.shape)
# np.save('../data_training/labels/generation_labels.npy', self_def_gen_labels)

print("output labels")
# print_labels('../data/labels_classes_priors/synthseg_segmentation_labels.npy')


print("generation classes")
# print_labels('../data/labels_classes_priors/generation_classes.npy')

mapping_df = pd.read_csv('../data_training/labels/labels_table.csv')
mapping_df.set_index("labels", inplace=True)
classes_list = [mapping_df.loc[i, "classes"] for i in self_def_gen_labels]
self_def_gen_classes = np.array(classes_list)
print(self_def_gen_classes)
print(self_def_gen_classes.shape)
np.save('../data_training/labels/generation_classes.npy', self_def_gen_classes)
