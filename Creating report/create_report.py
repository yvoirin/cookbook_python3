# le but de ce script est de générer un fichier docx avec des infos
# qui viennent d'une donnée matricielle ou vectorielle
# le document aura toujours la même forme
# Ce script est très utile si vous devez générer une multitude de documents Word

# on importe les libs
import glob
import os
import fiona
from fiona.crs import to_string
import rasterio
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import shapely.wkt
import pyproj
from shapely import ops

# mon répertoire à analyser
workdir = r'data'
# tous les fichiers du répertoire
files = glob.glob(workdir + '\*.*')

# une fonction pour reprojeter les bornes d'une donnée
def reproject(proj_src, x0,y0, x1, y1):
    # on va créer un polygone
    polygon = shapely.wkt.loads(f'POLYGON(({x0} {y0}, {x1} {y0}, {x1} {y1}, {x0} {y1}, {x0} {y0}))')
    proj_src = pyproj.Proj(proj_src)
    proj_dest = pyproj.Proj(init='EPSG:4326')
    # on projète
    transformer = pyproj.Transformer.from_proj(proj_src, proj_dest)
    # on va récupérer la nouvelle région projetée
    projpoly = ops.transform(transformer.transform, polygon)
    return projpoly

# une fonction pour générer une image qui représente la région de la donnée
def generateImage(filename, bounds, crs):
    # on utilise Matplotlib et cartopy
    ax = plt.axes(projection=ccrs.PlateCarree())
    # on place une image en fond
    ax.stock_img()
    # on ajoute les lignes de côtes
    ax.coastlines()
    # on ajoute une grille
    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    x0,y0,x1,y1 = bounds
    # on récupère la région projetée
    newpoly = reproject(crs, x0, y0, x1, y1)
    polybounds = newpoly.bounds
    # on ajoute la région
    ax.add_geometries([newpoly], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red', linewidth=2.5)
    ax.set_xlim(left=polybounds[0]-2, right=polybounds[2]+2)
    ax.set_ylim(bottom=polybounds[1]-2, top=polybounds[3]+2)
    # on sauvegarde la figure sous la forme d'une image
    plt.savefig(filename)
    plt.close()


# corps du programme
# on parcourts les fichiers
for index, file in enumerate(files):
    # on a besoin de plusieurs infos sur les fichiers dans notre rapport
    filename = os.path.basename(file)
    driver = '?'
    crs = '?'
    bounds = '?'
    # si c'est un shapefile, on doit lire avec fiona
    if '.shp' == filename[-4:]:
        with fiona.open(file) as src:
            # on récupère les infos
            driver = src.driver
            crs = to_string(src.crs)
            bounds = str(src.bounds)
            image = 'image%d.jpg' % index
            generateImage(image, src.bounds, to_string(src.crs))
    # si c'est un tiff, on doit lire avec rasterio
    elif '.tiff' == filename[-5:]:
        with rasterio.open(file) as src:
            # on récupère les infos
            driver = src.driver
            crs = to_string(src.crs)
            bounds = str(tuple(src.bounds))
            image = 'image%d.jpg' % index
            generateImage(image, tuple(src.bounds), to_string(src.crs))
    
    # on va générer le rapport docx
    if driver != '?':
        # on lit le modèle avec les balises
        doc = DocxTemplate(workdir + r'\template_word.docx')
        # on envoie les infos
        context = {
            'filename': filename, 'format': driver, 'bounds': bounds, 'crs': crs
        }
        # on ajoute l'image
        context['image'] = InlineImage(doc, image, width=Mm(100))
        doc.render(context)
        # on génère le fichier pour une donnée
        doc.save('generated_doc_%i.docx' % index)
