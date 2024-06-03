TITLE       = "Kohler illumination"
DESCRIPTION = """
"""

import envexamples
from raytracing import *

def exampleCode():
	path = ImagingPath()
	path.name = "Kohler illumination with 1 mm wide lamp and 0.25 NA"
	path.append(Space(d=50))
	path.append(Lens(f=50,diameter=25, label='Collector'))
	path.append(Space(d=50+100))
	path.append(Lens(f=100, diameter=25, label='Condenser'))
	path.append(Space(d=100))
	path.append(Space(d=18))
	path.append(Lens(f=18, diameter=9, label='Objective'))
	path.append(Space(d=18))
	path.showLabels=True
	print(path.fieldStop())
	print(path.fieldOfView())
	path.display(ObjectRays(diameter=1, H=3, T=3, halfAngle=0.125), onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)
	#path.saveFigure("Illumination.png", onlyPrincipalAndAxialRays=True, limitObjectToFieldOfView=True)

if __name__ == "__main__":
    exampleCode()
