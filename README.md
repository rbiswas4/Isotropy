# Isotropy
A project to investigate the requirements for constraining Isotropy of the metric at low redshifts using SNIa

## Background
As we all know, modern cosmology is built on the well studied model of the expanding universe. The consensus picture based on data from many surveys and theoretical understanding is that the universe expanded from early times with the rate of expansion dropping with time due to gravity, till a fairly recent time when the rate of expansion started increasing again. Understaning the physical driver for such increase in one of the major goals of current and future surveys.
 
One of the major axiomatic tenets of modern cosmology is the large scale statistical symmetry of the universe. The universe is taken to be statistically isotropic and homogeneous. Such symmetries are well explained by inflationary models, and to the extent that they have been tested, these assumptions have been affirmed. In particular, isotropy of the universe at very early times has been well tested at certain scales by observations of the cosmic microwave background (CMB). The only potential anomalies are at extremely large scales, where the results are uncertain due to a lack of possible samples (there is only one universe to observe). Thus such results will not improve even with better observations of the CMB.

At low redshift, the situation is different. First, the physics may be different, because the large scale evolution is driven by new components like dark energy. Second the set of potential observations that may be used to study isotropy are also different, making it possible to get new insights into this question. Thus it is possible to ask if low redshift (very late time observations) can tell us more about isotropy. A way of doing this is using supernovae Type Ia (SNIa). These are actually exploding stars of a particular kind, which have the interesting property that they are  'standardizbale candles'. This means that given a sufficient set of observations of a supernova Type Ia, one can infer the intrinsic luminosity of the observations. This property is usually used in inferring the expansion history of the universe since the time at which the SNIa exploded. One can think of these results as telling us What the expansion rate was at different times.

It turns out that with the sky area (about half of the sky) covered by the Large Synoptic Sky Telescope (LSST), it could be possible do this using Supernovae Type Ia. This is about ~20,000 square degrees which is much larger than the areas surveyed by current and previous SNIa surveys. Using this we may try to ask if the expansion history of the universe was different in different directions of the sky. This would be a test of isotropy.

## What will the Project Entail ? 

### Basic Questions we will ask
While this project has been talked about as a possibility (See the Science Book for LSST), the exact requirements for the project have not been ascertained. Thus, what we would like to do in this project is 
- Examine the possibility of how precisely such a violation of statistical isotropy at low redshifts might be constrained with the current baseline cadence of LSST. This is essentially a question of how many SN might be well observed enough to aid in determination of the expansion history in small enough patches of the sky.
- Are there potential changes (that are not huge) that might increase the efficacy of such a study?

### How  will we do such a project?

- LSST provides a simulation of possible observations during its ten year span. This is a realization based on extrapolation of some weather data and program called Operation Simulation (OpSim) that is used to plan observations for LSST. We have used this output and our knowledge of SNIa from previous surveys to simulate realizations of supernova observations similar to the quality expected for LSST. 
- We have software that can infer model parameters given the observations of a supernova. We will use this on the simulated observations of LSST SNIa at low redshift across the sky.
- We will divide the Southern sky into a number of parts (we will vary this number).  A smaller number of parts will give us more supernova per part of the sky. Since one can average over SNIa, having more SNIa enables one to constrain the expansion rate better for smaller numbers of division. This will enable one to say with more confidence whether the expansion history match for different parts of the sky. Higher numbers of division, on the other hand can probe more modes of variation across the sky. 
- We will use these results to study how well LSST will do in answering questions related to isotropy using supernovae

