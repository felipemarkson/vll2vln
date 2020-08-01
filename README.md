# Convert VLL to VLN

This package attempts to convert the 3-phases line-to-line voltages module measurements into line-to-neutral voltage module.


## Assumptions

This package assumes that the voltages are 120 degrees out of phase with each other.


## How to use

```python
from vll2vln import solve
import numpy as np

v_mens = np.array([13.8, 13.6, 13.9])

(isConverged, error_values, v_ln) = solve(v_mens, tol=0.01, verbose=True)

```

## Dependencies

Python 3.8.x

Numpy 1.19.x

NewtonPy = 0.1.x


## License and Copyright
 
MIT License

Copyright (c) 2020 Felipe M. S. Monteiro (<fmarkson@outlook.com>)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
