"""
test_measure.py
"""

import numpy as np
import pytest

import molecool


def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


def test_calculate_distance_typerror():

    r1 = [0, 0, 0]
    r2 = [0, 1, 0]

    with pytest.raises(TypeError):
        molecool.calculate_distance(r1, r2)


@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
])
def test_calculate_angles(p1, p2, p3, expected_angle):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)
    assert calculated_angle == pytest.approx(expected_angle)
