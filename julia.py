import time; import array; import numpy as np
from calc_z_cython import calc_z

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8    
c_real, c_imag = -0.476536, 0.578511

def calc_Julia(show, length, max_iter):
    xs = np.linspace(x1, x2, length)
    ys = np.linspace(y1, y2, length)
    zs = []; c = complex(c_real, c_imag)
    for x in xs:
         for y in ys:
             zs.append(complex(x, y))
    start_time = time.time()
    output = calc_z(max_iter, zs, c)
    end_time = time.time()
    print("%.4fs" % (end_time - start_time))  
    if show: show_image(output, length, max_iter)

from PIL import Image
def show_image(output_raw, length, max_iter):
    
    max_value = float(max(output_raw))
    output_raw_limited = [int(float(o) / max_value * 215) \
                          for o in output_raw]
    rgb = array.array('B')
    for o in output_raw_limited:
        r = o // 36; o = o % 36; g = o // 6; b = o % 6
        rgb.append(r*50); rgb.append(g*50); rgb.append(b*50);
    im = Image.new("RGB", (length, length));
    im.frombytes(rgb.tobytes(), "raw", "RGB")
    im.show()
    im.save("julia.jpg")

calc_Julia(show=True, length=5000, max_iter=500)