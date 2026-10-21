# MPLn23d
Python library to measure the 2-dimensional local number (LN2D) and the 3-dimensional local number (LN3D).

# Install

```
> pip install MPLn23d
```

Requires Python 3.9 or later and numpy. Prebuilt wheels are available for Windows (x64), macOS (x86_64, arm64) and Linux (x86_64, aarch64).

# References
## function stat_calc(f)
calculate statistics of frequency
+ f : 1-dimensional numpy array of frequency, dtype=np.uint32

Returns ((total, average, variance), rf).
+ total : total number of counts
+ average : average of local number
+ variance : variance of local number
+ rf : numpy array of relative frequency, dtype=np.float64

If all values of f are 0, average, variance and rf are nan.

## class ln2d_new(nsmax)
+ nsmax : maximum number of section

### Methods :
#### add_gc(sid, x, y, r)
add gc (gravity center)
+ sid : section id
+ x, y : position of gc, 0 <= x < sx and 0 <= y < sy
+ r : radius

Returns the number of gc in the section, or -1 if the position is out of the section.

#### add_gc_random(sid, ngc, sd, r)
add gc randomly
+ sid : section id
+ ngc : number of gc
+ sd : if sd > 0.0, positions follow a normal distribution centered on the section whose standard deviation is sd times the section size (position = size * (0.5 + sd * N(0, 1))); if sd <= 0.0, uniform random
+ r : radius

Returns the number of gc in the section.

#### add_sec(step, sx, sy)
add section
+ step : allocation step of gc
+ sx : size of section in x direction
+ sy : size of section in y direction

Returns the section id (0, 1, ...).

#### area_fraction()
calculate area fraction

Returns the area fraction, or -1.0 if there is no section.

#### cut(step, ln3d, cid, dir, pos)
cut ln3d cell and add the cross section as a new section
+ step : allocation step of gc
+ ln3d : ln3d cell
+ cid : cell id
+ dir : direction of cut plane, x:0, y:1, z:2
+ pos : position of cut plane

Returns the number of gc in the new section, or -99 if nsmax is exceeded (no exception is raised).

#### cut_random(nsec, step, ln3d, cid)
cut ln3d cell randomly and add nsec sections
+ nsec : number of sections, must fit within nsmax
+ step : allocation step of gc
+ ln3d : ln3d cell
+ cid : cell id

The direction of the cut plane cycles x, y, z and the position is uniform random.
Returns the total number of gc in the new sections, or -99 if nsmax is exceeded (no exception is raised).

#### measure_gc(f)
measure ln2d on gc
+ f : 1-dimensional numpy array for result, dtype=np.uint32

Results are added to f (f is not reset). Local numbers of len(f) or more are ignored.

#### measure_random(f, nsample)
measure ln2d on random point
+ f : 1-dimensional numpy array for result, dtype=np.uint32
+ nsample : number of sample

Results are added to f (f is not reset). Local numbers of len(f) or more are ignored.

### Data descriptors :
#### nsec
number of section (read only)

#### nsec_max
maximum number of section (read only)

#### seed
seed of random number (settable)

## class ln3d_new(ncmax)
+ ncmax : maximum number of cell

### Methods :
#### add_cell(step, sx, sy, sz)
add cell
+ step : allocation step of gc
+ sx : size of cell in x direction
+ sy : size of cell in y direction
+ sz : size of cell in z direction

Returns the cell id (0, 1, ...).

#### add_gc(cid, x, y, z, r)
add gc (gravity center)
+ cid : cell id
+ x, y, z : position of gc, 0 <= x < sx, 0 <= y < sy and 0 <= z < sz
+ r : radius

Returns the number of gc in the cell, or -1 if the position is out of the cell.

#### add_gc_random(cid, ngc, sd, r)
add gc randomly
+ cid : cell id
+ ngc : number of gc
+ sd : if sd > 0.0, positions follow a normal distribution centered on the cell whose standard deviation is sd times the cell size (position = size * (0.5 + sd * N(0, 1))); if sd <= 0.0, uniform random
+ r : radius

Returns the number of gc in the cell.

#### measure_gc(f)
measure ln3d on gc
+ f : 1-dimensional numpy array for result, dtype=np.uint32

Results are added to f (f is not reset). Local numbers of len(f) or more are ignored.

#### measure_random(f, nsample)
measure ln3d on random point
+ f : 1-dimensional numpy array for result, dtype=np.uint32
+ nsample : number of sample

Results are added to f (f is not reset). Local numbers of len(f) or more are ignored.

#### volume_fraction()
calculate volume fraction

Returns the volume fraction, or -1.0 if there is no cell.

### Data descriptors :
#### ncell
number of cell (read only)

#### ncell_max
maximum number of cell (read only)

#### seed
seed of random number (settable)
