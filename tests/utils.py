from PIL import Image
import numpy as np

from metrodraw.render import render_to_pillow
from metrodraw.schemes import MBTA, Retro, Terminal


testing = False

schemes = [MBTA(), Retro(), Terminal()]


def produce_or_check_image(rm, name, scheme):
    fullname = f"{name}-{scheme.__class__.__name__}"
    im = render_to_pillow(rm, scheme=scheme, font_size=10, lw=0.25)
    if testing:
        im2 = Image.open(f"eg/{fullname}.png")
        if np.array_equal(np.array(im), np.array(im2)):
            return
        # produce delta image
        delta = np.array(im) != np.array(im2)
        delta = delta.any(axis=2)
        delta = delta.astype(np.uint8) * 255
        delta = Image.fromarray(delta)
        delta.save(f"eg/{fullname}-delta.png")
        raise AssertionError(f"image mismatch: {fullname}; see eg/{fullname}-delta.png")
    else:
        im.save(f"eg/{fullname}.png")


def produce_or_check_images(rm, name):
    for scheme in schemes:
        produce_or_check_image(rm, name, scheme)
