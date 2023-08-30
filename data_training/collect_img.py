import os
import glob
import shutil
import dicom2nifti

base_path = os.path.abspath(r"/data_training/mask/nifti")
find_path = os.path.abspath(r"D:\CTP_mainland")
tmp_path = os.path.abspath(r"/data_training/tmp")
out_path = os.path.abspath(r"/data_training/img")

subjects = sorted(os.listdir(base_path))

for subject in subjects:
    subject_name = subject.split(".")[0]
    src_path = os.path.join(find_path, subject_name, "perfusion")
    imgs = sorted(os.listdir(src_path))[0:37]
    os.makedirs(os.path.join(tmp_path, subject_name), exist_ok=True)
    for img in imgs:
        shutil.copy(os.path.join(src_path, img), os.path.join(tmp_path, subject_name, img))
    dicom2nifti.convert_directory(os.path.join(tmp_path, subject_name), tmp_path, compression=False, reorient=False)
    search_res = glob.glob(os.path.join(tmp_path, "*.nii"))
    if len(search_res) == 1:
        shutil.move(search_res[0], os.path.join(out_path, subject))
    # break
