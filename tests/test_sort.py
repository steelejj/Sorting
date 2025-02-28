from constants import BULKY_DIM_LIMIT, BULKY_VOLUME_LIMIT, HEAVY_MASS_LIMIT
from main import sort

def test_sort_standard_limits():
    # test standard limits for width, height, and length
    assert sort(BULKY_DIM_LIMIT - 1, 1, 1, HEAVY_MASS_LIMIT - 1) == "STANDARD"
    # test standard limits for mass
    assert sort(1, 1, 1, HEAVY_MASS_LIMIT - 1) == "STANDARD"

def test_sort_bulky_limits():
    # test bulky limits for width, height, and length
    assert sort(BULKY_DIM_LIMIT, 1, 1, HEAVY_MASS_LIMIT - 1) == "SPECIAL"
    # test bulky limits for volume
    assert sort(BULKY_VOLUME_LIMIT - 1, BULKY_VOLUME_LIMIT - 1, BULKY_VOLUME_LIMIT - 1, HEAVY_MASS_LIMIT - 1) == "SPECIAL"
    # test bulky limits for mass
    assert sort(1, 1, 1, HEAVY_MASS_LIMIT) == "SPECIAL"

def test_sort_rejected_limits():
    # test rejected limits for width, height, and length
    assert sort(BULKY_DIM_LIMIT + 1, 1, 1, HEAVY_MASS_LIMIT) == "REJECTED"

def test_sort_invalid_inputs_0_width():
    # Test for inputs less than or equal to zero

    # Width is zero
    try:
        sort(0, 1, 1, 1)
    except ValueError as e:
        assert str(e) == "All inputs must be greater than zero."
    else:
        assert False, "ValueError not raised for width = 0"

def test_sort_invalid_inputs_negative_width():
    # Width is negative
    try:
        sort(-1, 1, 1, 1)
    except ValueError as e:
        assert str(e) == "All inputs must be greater than zero."
    else:
        assert False, "ValueError not raised for width = -1"

# I would continue to write tests for these cases or create a pytest fixture to test all of these cases given more time