""""
Module to create mock data in the form of redshift (z), distance modulus (mu),
and distance modulus uncertainties (mu_error) as a function of spatial area.

This starts off with a small sample of simulated SN from the all sky Wide Fast
Deep fields of LSST where the light curves have been fitted and an estimate of
uncertainties in distance moduli as a function of redshifts have been found.

- Here we read in the results table and get rid of some bad data points
- In small redshift bins, we remove some of the outliers with very large mu
  error (these are useless to first order) and then model the distribution of
  distance modulus uncertainties as a normal distribution. This includes a
  component for the intrinsic dispersion
- We then draw samples of (z, mu_error) that respect this distribution in each
  redshift bin. We add values of mu by calculating the distance modulus for an
  assumed cosmology using astropy routines, and add a scattter consistent with
  the distribution of mu_error
"""
import sys
import gzip
import pickle
import pandas as pd
import numpy as np
from astropy.cosmology import Planck15

__all__ = ['read_mockDataPickle', 'binnedDescStat', 'drawSamples']

def read_mockDataPickle(fname, filterBadPoints=True, selectCols=('z', 'mu', 'mu_var')):
    """
    Reads the Mock data in the form of a pickle file into a `pandas.DataFrame`
    such that the properties of SN are the columns. If the default `selectCols`
    is used, the columns are `z`, `mu`, `mu_var`
    Parameters
    ----------
    fname : string, mandatory
        absolute path to location of pickle file
    filterBadPoints : bool, optional, defaults to True
        Whether to filter bad data points
    selectCols  : tuple of strings, defaults to ('z', 'mu', 'mu_var')
        tuple of column names to keep
    """
    if sys.version.startswith('2'):
        snFits = pickle.load(gzip.GzipFile(fname))
    else:
        snFits = pickle.load(gzip.GzipFile(fname),
                                           encoding='latin1')
    df = pd.DataFrame(snFits).transpose()
    totalSN = len(df)
    if filterBadPoints:
        df = df.query('mu < 19. and mu > 0.')

    if selectCols is not None:
        df = df[list(selectCols)].astype(np.float)
    return df, totalSN

def binnedDescStat(mockDataFrame,
                   binningCol='z',
                   varColumn='mu_err',
                   outlier_rejection_query='mu_err < 5.0',
                   statisticsTuple=('count', np.mean, np.std),
                   binwidth=0.1):
    """
    bin an input dataFrame with columns of `z` and `mu_var` in uniform redshift
    bins of width 0.1, rejecting outliers in `mu_var` via a simple prescription
    described below. Return descriptive statistics of the uncertainties in
    distance modulus in each bin in the form of a mean and standard deviation of
    a Gaussian.

    Parameters
    ----------
    mockDataFrame : `pd.DataFrame`
    binningCol : string, optional, defaults to `z`
    varColumn : string, optional, defaults to `mu_err`
    outlier_rejection_query : string, optional defaults to vals below 5.0
    statisticsTuple : tuple, optional, defaults to ('count', np.mean, np.std)
    binwidth : float, default to 0.1

    Returns
    -------
    dataFrame
    """
    # Since we will be modifying the dataframe, create copy
    df  = mockDataFrame.copy(deep=True)

    # keep only those records that pass the outlier rejection query
    df = df.query(outlier_rejection_query)

    # Add required columns to mockDataFrame 
    df['binindex'] = df['z'] // binwidth
    df.binindex = df.binindex.astype(int)

    # Bin using groupby and aggregate to find descriptive statistics
    grouped = df.groupby('binindex')

    # statistics of interest : How do we calculate them from columns of
    # dataframe. In this case, we use a single column of the dataframe 'mu_err'
    # and calculate three statistics provided in a tuple
    statisticsDict = dict(mu_err=statisticsTuple)

    # aggregate on the grouped object to obtain the statistics in each bin
    return grouped.agg(statisticsDict)[varColumn] 

def drawSamples(data, numSN, totalSN, rng, binwidth=0.1, minz=0., cosmo=Planck15):
    """
    Draw samples of z, mu, mu_err from the binned descriptive statisics `data`

    Parameters
    ----------
    data : `pd.DataFrame`, mandatory
        table with counts, mean(mu_err), and std(mu_err) in columns
    numSN : int, mandatory
        total number of SN in the mock data (many of these will be bad data
        points) so the total number expected is smaller 
    totalSN : int, mandatory
        total number of SN from which `data`  parameter was derived
    rng : instance of `numpy.random.RandomState`
        random number state used to draw the statistical distributions
    binwidth : float, optional, defaults to 0.1
        width of (assumed) uniform redshift bins
    minz : float, optional, defaults to 0.
        min redshift used in the data
    cosmo : instance of cosmological models in astropy.cosmology, defaults to Planck15
        cosmological model used to obtain the uncertainties in distance modulus
    """
    data['frequency'] = data['count'] / np.float(totalSN)
    data['numexpected'] = np.round(data['frequency'].values * numSN).astype(np.int)

    # The total number of objects
    numExpTot = data.numexpected.sum()
    
    # Initialize arrays with random samples
    z = rng.uniform(0., binwidth, size=numExpTot)
    mu_err = rng.normal(0., 1., size=numExpTot)
    scatter = rng.normal(0., 1.0, size=numExpTot)

    # use linear functions to change samples to have appropriate distributions
    low = 0
    for idx, row in data.iterrows():
        # to slice the numpy arrays we use the count in each bin
        high = low + row['numexpected'].astype(int)

        # to get redshift, add the minz, and idx * binwidth as upper limit
        z[low:high] += minz + idx * binwidth

        # For mu_err first rescale the standard deviation then add to mean
        mu_err[low:high] *= row['std']
        mu_err[low:high] += row['mean']

        # reset low for next iteration
        low = high
        
        # distance moduli mu
        # We use the cosmology to calculate distance moduli corresponding to the z
        # Add a scatter consistent with mu_err
        mu = cosmo.distmod(z).value + scatter * mu_err

        # return as a dataframe
        df = pd.DataFrame(dict(z=z, mu=mu, mu_err=mu_err))

    return df

