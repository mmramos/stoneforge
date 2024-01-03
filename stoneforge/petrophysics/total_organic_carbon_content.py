import numpy.typing as npt
import numpy as np

def passey(dt, rt, dtbaseline, logrtbaseline, lom=10.6):

    """Estimate the Total Organic Carbon Content by Passey method using Sonic log and Resistivy log _.

    Parameters
    ----------
    dt : array_like
        Sonic log reading (acoustic transit time (μsec/ft))
    rt : array_like
        Resistivity log reading (formation resistivity (ohm/m))
    dtbaseline : int, float
        Sonic log base line (μsec/ft)
    logrtbaseline : int, float
        Resistivity log base line (ohm/m)
    lom : int, float
        Level of maturity
              
    Returns
    -------
    TOC : array_like
        Total organic carbon content calculated from passey method.

    References
    ----------
    Passey, O.R., F.U. Moretti, and J.D. Stroud, 1990, A practical modal for organic richness from porosity and resistivity logs: AAPG Bulletin, v. 
    74, p. 1777–1794.


    """
    rt = np.log10(rt)
    dlogrt = (rt - logrtbaseline) + 0.02*(dt - dtbaseline)
    toc = dlogrt*10**(2.297 - 0.1688*lom)
    clipped_toc = np.clip(toc, 0.0, 100.0)
    return clipped_toc
    

_toc_methods = {
    "passey": passey,
}

def calculate_toc(dt: npt.ArrayLike, rt: npt.ArrayLike, dtbaseline: float, logrtbaseline: float, lom: float, method: str = "passey", **kwargs) -> np.ndarray:
    """Compute water saturation from resistivity log.

    This is a façade for the methods:
        - passey

    Parameters
    ----------
    dt : array_like
        Sonic log reading (acoustic transit time (μsec/ft))
    rt : array_like
        Resistivity log reading (formation resistivity (ohm/m))
    dtbaseline : int, float
        Sonic log base line (μsec/ft)
    logrtbaseline : int, float
        Resistivity log base line (ohm/m)
    lom : int, float
        Level of maturity
    method : str, optional
        Name of the method to be used.  Should be one of
            - 'passey'
            
        If not given, default method is 'passey'

    Returns
    -------
    toc : array_like
        Total organic carbon content for the aimed interval using the defined method.

    """


    toc = passey(dt, rt, dtbaseline, logrtbaseline, lom)
    
    return toc
