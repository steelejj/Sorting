from constants import BULKY_DIM_LIMIT, HEAVY_MASS_LIMIT, BULKY_VOLUME_LIMIT

def sort(width: int, height: int, length: int, mass: int) -> str:

    # check if any inputs are less than or equal to zero
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All inputs must be greater than zero.")

    # check if the package is bulky
    if (width >= BULKY_DIM_LIMIT
            or height >= BULKY_VOLUME_LIMIT
            or length >= BULKY_VOLUME_LIMIT
            or width * height * length >= BULKY_VOLUME_LIMIT):
        bulky = True
    else:
        bulky = False

    # check if the package is heavy
    heavy = mass >= HEAVY_MASS_LIMIT

    # determine the package type
    if not bulky and not heavy:
        return "STANDARD"
    elif bulky and heavy:
        return "REJECTED"
    else:
        return "SPECIAL"