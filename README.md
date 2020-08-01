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
python = "^3.8"
numpy = "^1.19.1"
newtonpy = "^0.1.0"
