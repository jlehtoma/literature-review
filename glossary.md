## Glossary

__Analysis feature/Biodiversity feature__ = Input data that Zonation uses, in this study equals the index rasters.  

__Data source__ = One of the three data sources that are used to produce __input data sets__ (see below): MS-NFI (Finnish Forest Resarch Institute), stand-based data on public non-production land (Metsähallitus Natural Heritage Services), and  stand-based data on private land (Finnish Forest Centre).

__Forest type__ = A class created by how the indices are built, i.e. a combination of tree species group (e.g. birch) and soil fertility class (e.g. herb-rich) creates a forest type of "birch-herb-rich".

__Index raster__ = A raster with values of index describing the perceived conservation value of a given location (pixel). Index value determined by average diameter and volume of standing stock by tree species. There are 4 tree species groups (pine, spruce, birch, other deciduous) and thus there are 4 index rasters in the most basic situation. There 4 index rasters may be further divided into discrete classes based on soil fertility classes (n=5) in which case the number of index layers is 20.

__Input data set__ = Data set in which a Zonation analysis is based. In this work, we are using 3 different input data sets (MSNFI, MSNFI with classes, and detailed with classes) of increasing detail to compare the performance of freely available, but less accurate data to more detailed, but less available inventory data.

__Landscape__ = The study area, or the whole area for which the spatial conservation prioritization is done for.

__Site fertility class__ = One of "herb-rich", "herb-rich-like" (__CHECK__), "mesic", "semi-xeric", "xeric".

__Tree species group__ = One of "pine", "spruce", "birch", or "other broadleafed". A categorization following the one used in MS-NFI. More detailed data is pooled into these groups according to... 

__Validation data sets__ = Three data sets that are used to validate and comparte the Zonation resulta: 1) Protected areas (PAs), 2) Woodland key-habitats (WKHs), and 3) METSO-deals (MD). 

__Validation sites__ = Sites (spatially separate locations, polygons) included in the validation data sets. Each site can constitute of several polygons in the original data.

__Variant__ = A Zonation analysis version with A) given input data set, and B) given Zonation analytical options (such as connectivity) enabled. In this study, we have Zonation analysis based on 3 different input data sets and for each we have 2 different Zonation setups: with and without connectivity. Hence, this study has 6 different variants (V1-V6).