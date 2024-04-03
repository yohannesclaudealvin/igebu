import streamlit as st

# Titre de l'application
st.sidebar.image("IMAGE.jpg", width=150)
st.title('ANALYSE POUR LA PRÉVISION QUOTIDIENNE')
st.sidebar.title('DEPARTEMENT DE HYDROMETEOROLOGIE ET DE L\'AGROCLIMATOLOGIE')
st.sidebar.title('Service METEO - ASSISTANCE À LA NAVIGATION AÉRIENNE')

# Fonction pour afficher les liens
def afficher_liens(titre1, lien1, titre2, lien2):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<a href="{lien1}" target="_blank">{titre1}</a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="{lien2}" target="_blank">{titre2}</a>', unsafe_allow_html=True)

# Section "Images satellitaires depuis Eumetsat"
st.header("Images satellitaires depuis Eumetsat")
st.write("Visualisez les images satellitaires IR 10.8 et RGB depuis Eumetsat.")
st.markdown('[IR 10.8](https://eumetview.eumetsat.int/static-images/MSG/IMAGERY/IR108/BW/CENTRALAFRICA/index.htm)')
st.markdown('[RGB](https://eumetview.eumetsat.int/static-images/MSG/RGB/CONVECTION/CENTRALAFRICA/index.htm)')

# Section "Flux des vents depuis Forecast Maps"
st.header("Flux des vents depuis Forecast Maps")
st.write("Consultez les flux des vents à 850 mb et à 200 mb pour l’Afrique Day1 et Day2 depuis Forecast Maps.")
st.markdown('[Vents à 850 mb](http://wxmaps.org/fcst.php)')
st.markdown('[Vents à 200 mb](http://wxmaps.org/fcst.php)')

# Section "Cartes météorologiques depuis ECMWF"
st.header("Cartes météorologiques depuis ECMWF")
st.write("Accédez aux cartes MSLP depuis ECMWF.")
st.markdown('[Cartes MSLP](https://charts.ecmwf.int/products/medium-mslp-wind850?base_time=202404030000&projection=opencharts_africa&valid_time=202404030000)')

# Section "Cartes des vents et humidité relative depuis Climate Prediction Center"
st.header("Cartes des vents et humidité relative depuis Climate Prediction Center")
st.write("Consultez les cartes des vents et d’humidité relative depuis Climate Prediction Center.")
st.markdown('[Cartes des vents](https://www.cpc.ncep.noaa.gov/products/international/cpci/data/12/fcsts_eafrica.shtml)')
st.markdown('[Humidité relative](https://www.cpc.ncep.noaa.gov/products/international/cpci/data/12/fcsts_eafrica.shtml)')

# Section "Autres données météorologiques"
st.header("Autres données météorologiques")
st.write("Consultez différentes données météorologiques.")
st.markdown('[Energie Potentielle de Convection Disponible (CAPE)](https://www.cpc.ncep.noaa.gov/products/international/cpci/data/12/fcsts_eafrica.shtml)')
st.markdown('[Précipitations en 24h selon GFS](https://www.cpc.ncep.noaa.gov/products/international/cpci/data/00/fcsts_eafrica.shtml)')
st.markdown('[Rain and mean sea level pressure depuis ECMWF](https://charts.ecmwf.int/products/medium-mslp-rain?base_time=202308100000&interval=6&projection=opencharts_africa&valid_time=202308100600)')
st.markdown('[RDT](http://rsmc.weathersa.co.za/rsmcImg/hydrogii/RDT_SADC/RDT.htm)')
st.markdown('[Indice de prévision extrême de précipitation depuis ECMWF](https://charts.ecmwf.int/products/efi2web_tp?area=Africa&base_time=202308100000&day=1&quantile=99)')
st.markdown('[Indice de prévision extrême de vitesse de vent depuis ECMWF](https://charts.ecmwf.int/products/efi2web_10ff?area=Africa&base_time=202308100000&day=1&quantile=99)')

# Section "Prévision pour le Burundi"
st.header("Prévision pour le Burundi")
st.write("Consultez ces sites pour la prévision au Burundi :")
afficher_liens("RSMC-DAR ES SALAAM", "http://tma.go.tz/portal/rsmc",
               "RSMC Pretoria", "http://rsmc.weathersa.co.za/index.php")
afficher_liens("METEOCIEL", "https://www.meteociel.fr/previsions/41954/rumonge.htm",
               "VENTUSKY", "https://www.ventusky.com/?p=-2.86;32.90;6&l=rain-3h&t=20221005/0300")
afficher_liens("Météoblue", "https://content.meteoblue.com/fr/specifications/standards/symboles-et-pictogrammes",
               "Africa web viewer", "https://www.metoffice.gov.uk/premium/vcpafrica/#/map")
afficher_liens("Windy", "https://www.windy.com/?-4.038,29.368,8,i:pressure,m:dvRagUO",
               "Sat24", "https://fr.sat24.com/fr/tz/rain")
afficher_liens("Accuweather", "https://www.accuweather.com/",
               "NWC-SAF", "https://eumetrain.org/")
afficher_liens("Lever et Coucher du soleil", "https://fr.meteocast.net/sunrise-sunset/bi/bujumbura/",
               "Meteologix", "https://meteologix.com/fr")
