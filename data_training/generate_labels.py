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
    return list(labels)


mapping_df = pd.read_csv('labels/SynthSeg_Idx_parc.csv')

self_def_gen_labels = np.array(mapping_df['index'].tolist())
np.save('labels/generation_labels.npy', self_def_gen_labels)
print_labels('labels/generation_labels.npy')

seg_names = np.array(mapping_df['label'].tolist())
np.save('labels/segmentation_names.npy', seg_names)
print_labels('labels/segmentation_names.npy')

output_labes = np.array(mapping_df['output'].tolist())
np.save('labels/output_labels.npy', output_labes)
print_labels('labels/output_labels.npy')

gen_classes = np.array(mapping_df['class'].tolist()).astype(int)
np.save('labels/generation_classes.npy', gen_classes)
print_labels('labels/generation_classes.npy')


# labels = print_labels('../data/labels_classes_priors/synthseg_segmentation_labels_2.0.npy')
# classes = print_labels('../data/labels_classes_priors/synthseg_topological_classes_2.0.npy')
# names = print_labels('../data/labels_classes_priors/synthseg_segmentation_names_2.0.npy')
#
# df = pd.DataFrame({'labels': labels, 'classes': classes, 'names': names})
# print(df)
