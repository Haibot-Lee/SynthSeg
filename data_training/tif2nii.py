import os
from skimage.io import imread
import SimpleITK as sitk

base_path = "mask/tif"

subjects = os.listdir(base_path)
skip_list = ['CHEN_XUE_LING_3791087',
             'CHEN_ZAO_DE_3341618',
             'CUI_YI_NAN_3827857',
             'DU_QING_DONG_3850819',
             'HUI_FENG_CHENG_3459726',
             'JIANG_ZI_BIN_3498866',
             'JIE_XIAN_TAO_3221488',
             'LIANG_JUN_FENG_1899684',
             'LIU_SONG_TANG_3331335',
             'LI_QING_MING_3199299',
             'MENG_QING_SHENG_502',
             'MENG_XIAN_SHENG_3539540',
             'SUN_JIA_HUA_3250813',
             'SUN_QIN_YI_3303660',
             'WANG_HUA_RONG_3829685',
             'YANG_AI_GUI_3802950',
             'YANG_FANG_YONG_3631151',
             'ZHANG_LEI_3475891',
             'ZHANG_LIAN_QI_3223151',
             'ZHANG_TAI_XIN_3290140',
             'ZHANG_ZHI_SHEN_3195647',
             ]

for subject in subjects:
    if subject == 'nifti' or subject == '.DS_store':
        continue
    if subject.split(".")[0] in skip_list:
        continue

    img = imread(os.path.join(base_path, subject))
    if img.shape[0] != 37:
        print(subject, img.shape)
    # nii_file = sitk.GetImageFromArray(img)

    # out_f = os.path.join(base_path, "nifti", subject.split(".")[0] + ".nii")
    # if os.path.exists(out_f):
    #     continue
    #
    # sitk.WriteImage(nii_file, out_f)
