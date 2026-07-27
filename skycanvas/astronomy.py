from skyfield.api import load, Star
from skyfield.data import hipparcos

#DISCLAIMER: THIS IS NOT WORKING YET AT ALL.
ts = load.timescale()

with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

def get_star_position(star_name: str):
    """
        Get star coordinates from Hipparcos catalogue.
    """

    star = stars[stars["proper"] == star_name]

    if star.empty:
        return None
    return {
        "name": star_name,
        "ra": float(star.iloc[0]["ra"]),
        "dec": float(star.iloc[0]["dec"])
    }

def get_constellation_stars(star_list: list):
    """
        Get coordinates for all stars in a constellation.
    """

    result = []

    for star in star_list:
        data = get_star_position(star)

        if data:
            result.append(data)
        return result