import os
import glob
import shutil

base_path = os.path.abspath(r"Z:\output\ML")
out_path = os.path.abspath(r"C:\Users\User\Desktop\synthseg-training")

subjects = sorted(os.listdir(base_path))

for subject in subjects:
    search_res = glob.glob(os.path.join(base_path, subject, "RegMsk2CTP", "CTP_msk_ss2.tif"))

    if len(search_res) > 1:
        print("Multiple", subject)
        continue
    elif len(search_res) == 0:
        print("None", subject)
        continue
    dest_path = os.path.join(out_path, subject + ".tif")
    if os.path.exists(dest_path):
        continue

    print("copying {} ...".format(subject))
    shutil.copy(search_res[0], dest_path)
    # break
