# Quelques bouts de codes très utiles en géomatique

## Librairies importantes

Il serait important d'installer :
* Numpy
* Rasterio
* Fiona
* BeautifulSoup
* OGR/GDAL
* Pandas
* GeoPandas
* Requests
* LXML
* SqlAlchemy

L'idéal est d'installer Anaconda, car toutes ces librairies y sont incluses. On peut simplement faire : conda install ...

Le répertoire _data_ contient des données pour tester les bouts de code.

Vous pouvez voir les manipulations sur la chaîne Youtube : https://www.youtube.com/@YvesVoirin

## Lire des données

Le répertoire _Reading files_ donne du code pour lire des fichiers:
* csv -> _read_csv.py_  (avec csv)
* json -> _read_json.py_ (avec json)
* xml -> _read_from_web.py_ ou _read_xml.py_ (avec bs4)
* Gtiff (ou autres formats matriciels) -> _read_geotiff.py_ (avec gdal)
* shapefile (ou autres fichiers spatiaux) -> _read_vector.py_ (avec ogr)
* Gtiff (ou autres avec rasterio) -> _read_raster_with_rasterio.py_ (avec rasterio)
* Gtiff (ou autres avec opencv) -> _read_raster_with_opencv.py_ (avec opencv)
* Vecteurs (avec fiona) -> _read_vector_with_fiona.py_ (avec fiona)

Le répertoire _Reading from DB_ donne des exemples d'échanges avec une base de données PostgreSQL/PostGIS:
* PostgreSQL/PostGIS -> _read_from_postgis.py_ (avec ogr)
* PostgreSQL/PostGIS -> _transfer_ToFrom_PostgreSQL_PostGIS.py_ (avec pandas, geopandas, sqlalchemy)

## Écrire des données

Le répertoire _Creating files_ donne du code pour écrire des fichiers:
* Gtiff (ou autres formats matriciels) -> _write_geotiff.py_ (avec GDAL)
* Gtiff (ou autres formats matriciels) -> _write_geotiff_with_rasterio.py_ (avec rasterio)
* shapefile (ou autres fichiers spatiaux) -> _write_shpfile.py_ (avec ogr)
en utilisant GDAL/OGR on peut faire des shapefiles (ou autres fichiers spatiaux)
* shapefile (ou autres fichiers spatiaux) -> _write_shpfile_with_fiona.py_ (avec fiona)

Le répertoire _Projections_ donne des exemples de manipulations de projection:
* Reprojeter une géométrie avec OSR -> _reproject_data.py_ (avec ogr, osr)
* Reprojeter une image et rééchantillonner avec GDAL -> _resample_image.py_ (avec gdal)
* Reprojeter une image avec rasterio -> _reproject_raster_with_rasterio.py_ (avec rasterio)
* Reprojeter un vecteur avec fiona -> _reproject_vector_with_fiona.py_ (avec fiona)
## Manipuler les géométries

Le répertoire _Using shapely_ donne des exemples avec shapely :
* Quelques opérations de base avec shapely -> _some_basics_with_shapely.py_ (shapely)

## Traiter les données

Le répertoire _Using Numpy_ donne des exemples avec la lib Numpy:
* Faire une fenêtre glissante 1D -> _simple_moving_window.py_ (avec numpy)

Le répertoire _Using Pandas_ donne des exemples avec la lib Pandas:
* Faire un Dataframe à partir d'un CSV -> _read_csv_with_pandas.py_ (avec pandas)

Le répertoire _Image processing_ donne des exemples de traitements d'image :
* Appliquer MobileNet avec Opencv -> _OpenCV_MobileNet.py_ (opencv, numpy)
* Traitements de base avec Opencv -> _simple_processing_with_opencv.py_ (opencv)
* Découper une image comme un puzzle -> _simple_processing_with_pil.py_ (avec pil)
* Découper une image à partir d'un vecteur -> _clip_raster_with_vector.py_ (avec fiona et rasterio)

Le répertoire _Spatial Analysis_ donne des exemples d'analyses spatiales :
* Convertir une matrice en un vecteur -> _From_Raster_to_Vector.py_ (avec ogr, gdal, osr)
* Convertir un fichier de ligne en un réseau -> _Get_circuit.py_ (avec ogr, networkx)
* Extraire les entités sous un masque -> _Get_features_under_the_mask.py_ (avec ogr)
* Rechercher le chemin le plus court -> _Get_shortest_path.py_ (avec ogr, networkx)
* Utiliser un index spatial -> _using_rtree.py_ (avec fiona, rtree)
* Vectoriser une image -> _From_Raster_to_Vector_with_fiona_rasterio.py_ (avec fiona et rasterio)
* Rasteriser un vecteur -> _From_Vector_to_Raster_with_fiona_rasterio.py_ (avec fiona et rasterio)

Le répertoire _Using GeoNames_ donne un exemple d'usage de GeoNames
* Rechercher la position d'une entité géographique à l'aide du nom -> _search_with_geonames.py_ (avec requests, json)

## Afficher les résultats

Le répertoire _Using Matplotlib_ donne des exemples avec la lib Matplotlib
* Faire un simple graphique avec matplotlib -> _create_simple_figure.py_ (avec matplotlib)

## Faire des rapports

Le répertoire _Creating report_ donne des exemples avec la lib DocxTemplate
* Parcourir un répertoire de données spatiales et faire un rapport -> _create_report.py_ (avec glob, rasterio, fiona, docxtpl)

## Extraire des données du web avec Scrapy

Le répertoire _Using Scrapy_ donne un exemple de spider qui parcourt un site web et qui fait l'extraction de données. Il sauvegarde les résultats dans un fichier csv.

## Quelques opérations utiles en géomatique

Le répertoire _utils_ donne des exemples de scripts souvent utiles :
* Partir d'observations ponctuelles et construire une grille interpolée -> _from_vector_to_mesh.py_ (avec numpy, scipy, shapely, fiona, rasterio)
* Partir de données XML du web et construire un shapefile -> _from_xml_web_to_shp_file.py_ (bs4, fiona, shapely)
* Extraire la liste de fichiers d'un répertoire -> _get_files_in_directory.py_ (avec glob)
* Quelques astuces du langage Python -> _somebasics.py_

## Utiliser DJANGO

Le répertoire _Using django_ donne un exemple de site web en Python avec une carte