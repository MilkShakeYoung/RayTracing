TITLE       = "Aperture behind lens acting as Field Stop"
DESCRIPTION = """ An object at z=0 (front edge of ImagingPath) is used with
default properties. Notice the aperture stop (AS) identified at the lens which
blocks the cone of light. The second aperture, after the lens, is the Field Stop
(FS) and limits the field of view."""


# f1 = 30mm; f2=150mm Illumination system

from raytracing import *

def exampleCode(comments=None):
    path = ImagingPath()
    path.label = TITLE
    path.append(Space(d=30))
    path.append(Lens(f=30, diameter=25))
    path.append(Space(d=100))
    path.append(Aperture(diameter=25))
    path.append(Lens(f=150, diameter=25))
    path.append(Space(d=150))
    path.display(ObjectRays(diameter=1, halfAngle=0.5),comments=comments)

if __name__ == "__main__":
    exampleCode()