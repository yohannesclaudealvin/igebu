import streamlit as st

# En-tête de l'application
st.sidebar.image("IMAGE.jpg", width=150)
st.sidebar.title('INSTITUT GEOGRAPHIQUE DU BURUNDI')
st.sidebar.title('DEPARTEMENT DE HYDROMETEOROLOGIE ET DE L\'agroclimatologie')
st.sidebar.title('Service météo - ASSISTANCE À LA NAVIGATION AÉRIENNE')

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
st.markdown('Importe l’image satellitaire à 600Z du jour depuis Eumetsat RGB composite, puis convection dans la zone centrale de l’Afrique : [EUMETSAT Image Gallery Animation - Meteosat 0 degree Convection Central Africa](https://eumetview.eumetsat.int/static-images/MSG/RGB/CONVECTION/CENTRALAFRICA/index.htm)')
st.markdown('Real time satellite image : [Real time satellite image](https://science.ncas.ac.uk/swift/resources/summary/429%2C612%2C483%2C767%2C1623/0)')
# Ajout du lien vers le graphique météorologique ECMWF
st.markdown('Graphique météorologique ECMWF : [Graphique ECMWF](https://charts.ecmwf.int/products/opencharts_meteogram?base_time=202404050000&epsgram=classical_10d&lat=51.4333&lon=-1.0&station_name=Reading)')
# Section "Flux des vents depuis Forecast Maps"
st.header("Flux des vents depuis Forecast Maps")
st.write("Consultez les flux des vents à 850 mb et à 200 mb pour l’Afrique Day1 (on choisit Day0.5) et Day2 (on choisit Day1.5) depuis Forecast Maps.")
st.markdown('[Vents à 850 mb](http://wxmaps.org/fcst.php)')
st.markdown('[Vents à 200 mb](http://wxmaps.org/fcst.php)')

# Section "Cartes MSLP depuis ECMWF"
st.header("Cartes MSLP depuis ECMWF")
st.write("Accédez aux cartes MSLP depuis ECMWF.")
st.markdown('[Cartes MSLP pour Day1 et Day2](https://charts.ecmwf.int/products/medium-mslp-wind850?base_time=202308100000&projection=opencharts_africa&valid_time=202308111200)')

# Section "Cartes des vents et humidité relative depuis Climate Prediction Center"
st.header("Cartes des vents et humidité relative depuis Climate Prediction Center")
st.write("Consultez les cartes des vents et d’humidité relative depuis Climate Prediction Center.")
st.markdown('[Cartes des vents et humidité relative pour Day1 et Day2](https://www.cpc.ncep.noaa.gov/products/international/cpci/data/12/fcsts_eafrica.shtml)')

# Section "Prévision pour le Burundi"
st.header("Prévision pour le Burundi")
st.write("Consultez ces sites pour la prévision au Burundi :")
afficher_liens("RSMC-DAR ES SALAAM", "http://tma.go.tz/portal/rsmc",
               "RSMC Pretoria", "http://rsmc.weathersa.co.za")
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
afficher_liens("ICPAC", "https://www.icpac.net/"
               )
# Section "Prévision pour le Burundi"


# Fonction pour afficher les liens
def afficher_liens(liens):
    for nom, url in liens.items():
        st.write(f"- [{nom}]({url})")

# Liens pour les produits satellitaires d'EUMETSAT 3ème génération
liens_eumetsat = {
    "EUMETRAIN (ePort/ePort Pro)": "https://eumetrain.org/",
    "EUMETSAT (View)": "https://view.eumetsat.int",
    "Swift": "https://science.ncas.ac.uk/swift/",
    "ACMAD": "http://sgbd.acmad.org:8080/thredds/fileServer/RDT/index.html"
}

# Section "NWC-SAF (Produits satellitaires d’EUMETSAT 3ème génération)"
st.header("NWC-SAF (Produits satellitaires d’EUMETSAT 3ème génération)")
st.write("Voici les liens vers les produits satellitaires d’EUMETSAT 3ème génération :")
afficher_liens(liens_eumetsat)

# Fonction pour afficher les liens
def afficher_liens(liens):
    for nom, url in liens.items():
        st.write(f"- [{nom}]({url})")

# Liens pour Africa Web Viewer et les indices MUCAPE, Kindex, Totalx
liens_Burundi_web_viewer = {
    "Burundi Web Viewer (metoffice.gov.uk)": "https://www.metoffice.gov.uk/weather/world/burundi/list",
    " Africa MUCAPE index, Kindex, Totalx": "https://charts.ecmwf.int/products/medium-indices?base_time=202307250000&layer_name=mucape&projection=opencharts_africa&valid_time=202307250000"
}

# Section "Burundi Web Viewer et les indices MUCAPE, Kindex, Totalx"
st.header("Burundi Web Viewer et les indices MUCAPE, Kindex, Totalx")
st.write("Voici les liens vers Africa Web Viewer et les indices MUCAPE, Kindex, Totalx :")
afficher_liens(liens_Burundi_web_viewer)
