from numpy import array
from newtonpy import solve as _root


def _hx(v1, v2):
    return (v1 + v2 / 2) ** 2 + (3 / 4) * v2 ** 2


def _fx(v):
    return array([_hx(v[0], v[1]), _hx(v[1], v[2]), _hx(v[2], v[0])])


def _dfdv1(v1, v2):
    return 2 * v1 + v2


def _dfdv2(v1, v2):
    return 2 * v2 + v1


def _jac(vx):
    return array(
        [
            [_dfdv1(vx[0], vx[1]), _dfdv2(vx[0], vx[1]), 0],
            [0, _dfdv1(vx[1], vx[2]), _dfdv2(vx[1], vx[2])],
            [_dfdv2(vx[2], vx[0]), 0, _dfdv1(vx[2], vx[0])],
        ]
    )


def _get_gx(v_esp):
    return lambda vx: _fx(vx) - v_esp


def solve(v_mens, tol=0.01, verbose=True):
    gx = _get_gx(v_mens ** 2)
    v0 = v_mens / (3 ** 0.5)
    return _root(gx, _jac, v0, tol=tol, verbose=verbose)
