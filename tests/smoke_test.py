import numpy as np
import MPLn23d

ln3d = MPLn23d.ln3d_new(1)
cid = ln3d.add_cell(100, 1.0, 1.0, 1.0)
ln3d.add_gc_random(cid, 1000, 0.0, 0.01)
f3 = np.zeros(20, dtype=np.uint32)
ln3d.measure_gc(f3)
assert f3.sum() > 0
print("ln3d:", MPLn23d.stat_calc(f3)[0], "volume fraction", ln3d.volume_fraction())

ln2d = MPLn23d.ln2d_new(10)
ln2d.cut_random(10, 100, ln3d, cid)
buf = np.zeros(40, dtype=np.uint32)
f2 = buf[::2]  # non-contiguous view is copied and must be written back
ln2d.measure_gc(f2)
assert f2.sum() > 0
print("ln2d:", MPLn23d.stat_calc(f2)[0], "area fraction", ln2d.area_fraction())
