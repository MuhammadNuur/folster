""" Main Folium Map Module """

# import module
import pandas as pd
import geopandas
import folium


dftr_kolom = ("NAMA", "SISTEM", "TIPE", "TEGANGAN", "DAYA", "STATUS", "TAHUN", "KOTA",
              "KAPASITAS", "PROV", "Longitude", "Latitude")

try :
    data = pd.read_excel("docs/TestGI.xlsx",  index_col = None,  sheet_name='DataGardu')
except :
    print("File Gagal d load")

mentah = data.loc[:, dftr_kolom]
mentah = mentah.dropna(subset=['Longitude']).reset_index(drop=True)
mentahan = mentah.copy(deep=True)
# print (mentahan.head())

# Create point geometries
geometry = geopandas.points_from_xy(mentahan.Longitude, mentahan.Latitude)
geo_df = geopandas.GeoDataFrame(
    mentahan[["TAHUN", "NAMA","SISTEM", "Latitude", "Longitude", "TIPE", "KAPASITAS"]], geometry=geometry)
# print (geo_df.head())

map = folium.Map(location=[-1.3571968467313706, 128.295928330537], tiles="OpenStreetMap", zoom_start=6.5)
tw_tms = folium.FeatureGroup(name="Tower Transmission", show=False).add_to(map)
ln_tms = folium.FeatureGroup(name="Line Transmission", show=False).add_to(map)

# Create a geometry list from the GeoDataFrame
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]

# sudah dibuat list kosong sesuai dengan nama-nama sistem yang tipe SUTT
def buat_list_kosong(list_of_names):
    for name in list_of_names:
        return {name: [] for name in list_of_names}

sutt_sistem_data = geo_df[geo_df['TIPE'] == 'SUTT Tower']['SISTEM'].unique()
dftr_line_trans = list(sutt_sistem_data)
dict_list_trans = buat_list_kosong(dftr_line_trans)

# Fungsi menentukan warna marker
def get_type_color(tipe):
    color_mapping = {
        "GI": "green",
        "GIS": "orange",
        "IBT": "beige",
        "MOBILE": "pink",
        "SUTT Tower": "red"}
    return color_mapping.get(tipe, "gray")

# MAPPING
for coordinates, row in zip(geo_df_list, geo_df.itertuples()):
    type_color = get_type_color(row.TIPE)
    tipe = row.TIPE

    if 'SUTT' in row.TIPE :
        dict_list_trans[row.SISTEM].append(coordinates)

    if tipe == "SUTT Tower":
        folium.CircleMarker(
            location=coordinates,
            fill_color="green",
            fill=False,
            tooltip=f"Nama: {row.NAMA}<br>TIPE: {row.TIPE}<br>Daya: {row.KAPASITAS}",
            icon=folium.Icon(color=type_color)
        ).add_to(tw_tms)
    else:
        folium.Marker(
            location=coordinates,
            radius=3,
            popup=f"Nama: {row.NAMA}",
            icon=folium.Icon(icon="star", color=type_color)
        ).add_to(map)

for key in dict_list_trans:
    folium.PolyLine(locations = dict_list_trans[key], tooltip=key, line_opacity = 0.5).add_to(ln_tms)

folium.LayerControl().add_to(map)
map.add_child(folium.LatLngPopup())



def main() -> None:
    map.show_in_browser()

if __name__ == "__main__":
    main()
