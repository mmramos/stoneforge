import warnings
import numpy.typing as npt
import numpy as np

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]

def density_porosity(rhob: float, rhom: float, rhof: float) -> np.ndarray:
    """
    Estimate the porosity from the bulk density log [1]_.

    Parameters
    ----------
    rhob : array_like
        Bulk density log.
    rhom : int, float
        Matrix density.
    rhof : int, float
        Density of the fluid saturating the rock (Usually 1.0 for water and 1.1 for saltwater mud).
       
    Returns
    -------
    phi : array_like
        Total porosity for the aimed interval using the bulk density.

    References
    ----------      
    .. [1] Schön, J. H. (2015). Physical properties of rocks: Fundamentals and 
    principles of petrophysics. Elsevier.


    """
    if rhom == rhof:
        warnings.warn(UserWarning("This will result in a division by zero"))

        return 0

    else:
        if rhom < rhof or rhom <= rhob:
            warnings.warn(UserWarning("rhom must be greater than rhof and rhob"))

            phi = (rhom - rhob) / (rhom - rhof)

            return 0
        
        elif rhom - rhob > rhom - rhof:
            warnings.warn(UserWarning("phi must be a value between 0 and 1"))

            return 0
        
        else: 
            phi = (rhom - rhob) / (rhom - rhof)

            return phi

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass