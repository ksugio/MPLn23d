# MPLn23d
Python library to measure the 2-dimensional local number (LN2D) and the 3-dimensional local number (LN3D).

# Install

```
> pip install MPLn23d
```

# References
## class ln2d_new(nsmax)
+ nsmax : maximum number of section

### Methods :
#### add_gc(sid, x, y, r)
add gc (gravity center)
+ sid : section id
+ x, y : position of gc
+ r : radius

#### add_gc_random(sid, ngc, sd, r)
add gc randomly
+ sid : section id
+ ngc : number of gc
+ sd : standard deviation of random number, if sd <= 0.0 uniform random
+ r : radius

#### add_sec(step, sx, sy)
add section
+ step : allocation step of gc
+ sx : size of section in x direction
+ sy : size of section in y direction

#### area_fraction()
calculate area fraction

#### cut(step, ln3d, cid, dir, pos)
cut ln3d cell
+ step : allocation step of gc
+ ln3d : ln3d cell
+ cid : cell id
+ dir : direction of cut plane, x:0, y:1, z:2
+ pos : position of cut plane

#### cut_random(nsec, step, ln3d, cid)
cut ln3d cell randomly
+ nsec : number of sections
+ step : allocation step of gc
+ ln3d : ln3d cell
+ cid : cell id

#### measure_gc(f)
measure ln2d on gc
+ f : numpy dimension for result, dtype=np.uint32

#### measure_random(f, nsample)
measure ln2d on random point
+ f : numpy dimension for result, dtype=np.uint32
+ nsample : number of sample

### Data descriptors :
#### nsec
number of section

#### nsec_max
maximum number of section

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

#### add_gc(cid, x, y, z, r)
add gc (gravity center)
+ cid : cell id
+ x, y, z : position of gc
+ r : radius

#### add_gc_random(cid, ngc, sd, r)
add gc randomly
+ cid : cell id
+ ngc : number of gc
+ sd : standard deviation of random number, if sd <= 0.0 uniform random
+ r : radius

#### measure_gc(f)
measure ln3d on gc
+ f : numpy dimension for result, dtype=np.uint32

#### measure_random(f, nsample)
measure ln3d on random point
+ f : numpy dimension for result, dtype=np.uint32
+ nsample : number of sample

#### volume_fraction()
calculate volume fraction

### Data descriptors :
#### ncell
number of cell

#### ncell_max
maximum number of cell

#### seed
seed of random number (settable)
