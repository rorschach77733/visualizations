import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl

df = pd.read_csv('0.events.csv.gz', compression='gzip')

df = df[['startX', 'startY']]
df = df.dropna()
df = df.head(100)

f = open('config.json', 'r')
config = json.load(f)
f.close()

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.startX, df.startY))
map = KeplerGl(height=800, width=800, config=config)
map.add_data(data=gdf, name="Construction") #add geoenabled dataframe to map
# map.save_to_html(file_name='sf_light_1k.html') 
map
