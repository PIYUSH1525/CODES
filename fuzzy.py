import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from fontTools.ttLib.sfnt import sfntDirectorySize


def defuzzify(x, mfx, method):
    """
    Defuzzifies the fuzzy set using the specified method.

    Parameters:
    x: Universe of discourse.
    mfx: Membership function of the fuzzy set.
    method: Defuzzification method ('centroid', 'bisector', 'mom', 'som', 'lom').

    Returns:
    Defuzzified value.
    """
    if method == 'centroid':
        return fuzz.defuzz(x, mfx, 'centroid')
    elif method == 'bisector':
        return fuzz.defuzz(x, mfx, 'bisector')
    elif method == 'mom':
        return fuzz.defuzz(x, mfx, 'mom')
    elif method == 'som':
        return fuzz.defuzz(x, mfx, 'som')
    elif method == 'lom':
        return fuzz.defuzz(x, mfx, 'lom')
    else:
        raise ValueError("Invalid defuzzification method.")


x = np.arange(0, 11, 1)
mfx = fuzz.trimf(x, [2, 5, 8])

# Defuzzify using different methods
defuzz_centroid = defuzzify(x, mfx, 'centroid')
defuzz_bisector = defuzzify(x, mfx, 'bisector')
defuzz_mom = defuzzify(x, mfx, 'mom')
defuzz_som = defuzzify(x, mfx, 'som')
defuzz_lom = defuzzify(x, mfx, 'lom')

print("Centroid:", defuzz_centroid)
print("Bisector:", defuzz_bisector)
print("MOM (Mean of Maximum):", defuzz_mom)
print("SOM (Smallest of Maximum):", defuzz_som)
print("LOM (Largest of Maximum):", defuzz_lom)

plt.plot(x, mfx, 'b', label='Membership function')
plt.axvline(defuzz_centroid, color='r', linestyle='--', label='Centroid')
plt.axvline(defuzz_bisector, color='g', linestyle='--', label='Bisector')
plt.axvline(defuzz_mom, color='m', linestyle='--', label='MOM')
plt.axvline(defuzz_som, color='y', linestyle='--', label='SOM')
plt.axvline(defuzz_lom, color='c', linestyle='--', label='LOM')
plt.title('Defuzzification Methods')
plt.legend()
plt.show()

