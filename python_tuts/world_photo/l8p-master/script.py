import os
import numpy as np
import rasterio as rio
import rasterio.mask as rmask
import fiona as fio
import matplotlib.pyplot as plt

def read_landsat_images(folder_name):
    """Funckcja zwraca słownik (dict) z parami NUMBER KANAŁU:
    ścieżka_do_pliku
    return: {numer_kanału, ścieżka_do_pliku}"""
    file_list = os.listdir(folder_name)
    channel_list = []
    for f in file_list:
        if (f.startswith('LC') and f.endswith('.tif')):
            if 'band' in f:
                channel_list.append(folder_name + f)
    channel_list.sort()
    channel_numbers = np.arange(1, 8)
    bands_dictionary = dict(zip(channel_numbers, channel_list))
    return bands_dictionary

def show_band(band, color_map='gray', remove_negative=True):
    matrix = band.astype(float)
    if remove_negative:
        matrix[matrix <= 0] = np.nan
    fig = plt.figure(figsize=(8,8))
    image_layer = plt.imshow(band)
    image_layer.set_cmap(color_map)
    plt.colorbar()
    plt.show()

def clip_area(vector_file, raster_file, save_image_to):
    with fio.open(vector_file, 'r') as clipper:
        geometry = [feature["geometry"] for feature in clipper]

    with rio.open(raster_file, 'r') as raster_source:
        clipped_image, transform = rmask.mask(raster_source, geometry, crop=True)
        metadata = raster_source.meta.copy()

    metadata.update({"driver":"GTiff",
        "height":clipped_image.shape[1],
        "width":clipped_image.shape[2],
        "transform": transform})

    with rio.open(save_image_to, 'w', **metadata) as g_tiff:
        g_tiff.write(clipped_image)

def calculate_index(index_name, landsat8_bands):
    indexes = {
        'ndvi':(5,4),
        'ndbi':(6,5),
        'ndwi':(3,6),
    }
    if index_name in indexes:
        bands = indexes[index_name]
        with rio.open(landsat8_bands[bands[0]]) as a:
            band_a = (a.read()[0]/1000).astype(np.float)
        with rio.open(landsat8_bands[bands[1]]) as b:
            band_b = (b.read()[0]/1000).astype(np.float)

        numerator = band_a - band_b
        denominator = band_a + band_b

        idx = numerator/denominator
        idx[idx > 1] = 1
        idx[idx < -1] = -1

        return idx
    else:
        raise ValueError('Brak wskaźnika do wyboru, dostępne wskaźniki to ndbi, ndvi  i ndwi')


bands = read_landsat_images('photos/')

vector = 'vector/krakow_krakowskie.shp'
clipped_folder = 'clipped/'

for band in bands:
    destination = clipped_folder + 'LC_clipped_band' + str(band) + '.tif'
    clip_area(vector, bands[band], destination)

clipped_bands = read_landsat_images('clipped/')
for band in clipped_bands:
    print(clipped_bands[band])

with rio.open(clipped_bands[5], 'r') as src:
    band_matrix = src.read(1)

show_band(band_matrix)


ndvi = calculate_index('ndvi', clipped_bands)
ndvi[ndvi == 0] = -1
show_band(ndvi, color_map='viridis', remove_negative=True)

ndwi = calculate_index('ndwi',clipped_bands)
ndwi[ndwi  == 0] = np.nan
show_band(ndwi, color_map='viridis', remove_negative=False)

ndbi = calculate_index('ndbi', clipped_bands)
ndbi[ndbi==0] = np.nan
show_band(ndbi, color_map='viridis', remove_negative=False)

show_band(ndbi-ndvi, color_map='viridis', remove_negative=False)