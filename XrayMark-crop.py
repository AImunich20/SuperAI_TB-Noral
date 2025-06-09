import os
import cv2
import numpy as np
from tqdm import tqdm

# path
xray_folder = "/home/maybe/Downloads/TB"
mask_folder = "/home/maybe/Downloads/mark_TB"
output_folder = "/home/maybe/Downloads/xray_TB"

os.makedirs(output_folder, exist_ok=True)

processed_count = 0
failed_count = 0

for filename in tqdm(os.listdir(xray_folder)):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        xray_path = os.path.join(xray_folder, filename)
        mask_path = os.path.join(mask_folder, filename)
        output_path = os.path.join(output_folder, filename)
      
        xray = cv2.imread(xray_path, cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        binary_mask = mask > 127

        xray_lung_only = np.ones_like(xray) * 255
        xray_lung_only[binary_mask] = xray[binary_mask]

        cv2.imwrite(output_path, xray_lung_only)
        processed_count += 1

print(f"✅ เสร็จสิ้น! ประมวลผลสำเร็จ {processed_count} รูป")
if failed_count > 0:
    print(f"error {failed_count} รูป")
