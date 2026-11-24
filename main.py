import os
import shutil

with open(os.path.join(os.path.dirname(__file__), "entry.txt"), "rb") as f:
    data = f.read()

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
    f.write(data)
