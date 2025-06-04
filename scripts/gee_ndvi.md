This is a GEE script for generating NDVI for the taal lidar project. Written in markdown for documentation purposes.

<!-- 
// ====== SETTINGS ======
// Load your tile shapefile uploaded as an asset (replace with your actual asset ID)
var aoi: Table projects/ee-jcasisirano/assets/taal-lidar

// Date range for dry season NDVI (March–May 2017)
var start = '2017-03-01';
var end = '2017-05-31';

// ====== NDVI PROCESSING ======
// Load Sentinel-2 Surface Reflectance data (Level 2A)
var s2 = ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
  .filterBounds(aoi)
  .filterDate(start, end)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .map(function(img) {
    var ndvi = img.normalizedDifference(['B8', 'B4']).rename('NDVI');
    return ndvi.copyProperties(img, ['system:time_start']);
  });

print("NDVI collection size:", s2.size());


// Generate NDVI mean composite
var ndviMean = s2.mean().clip(aoi);

// ====== DISPLAY IN MAP ======
Map.centerObject(aoi, 12);
Map.addLayer(ndviMean, {min: 0, max: 1, palette: ['white', 'green']}, 'NDVI Mean (Mar–May 2017)');

// ====== EXPORT TO GOOGLE DRIVE ======
Export.image.toDrive({
  image: ndviMean,
  description: 'NDVI_MarMay2017_Taal_100m',
  folder: 'GEE_exports',
  fileNamePrefix: 'ndvi_mar_may_2017',
  region: aoi.geometry(),
  scale: 10,
  crs: 'EPSG:32651',
  maxPixels: 1e13
}); -->
