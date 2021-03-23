import json, requests

url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/" \
      "FeatureServer/0/query?where=OBJECTID%3D121&outFields=OBJECTID%2CEWZ%2Clast_update%2C" \
      "death_rate%2Ccases%2Cdeaths%2Ccases_per_100k%2Ccounty%2Ccases7_lk%2Cdeath7_lk%2" \
      "Ccases7_per_100k_txt&returnGeometry=false&f=json"


def update_data():
    response = requests.get(url)
    corona_data = json.loads(response.text)
    h_read = corona_data["features"][0]["attributes"]
    return h_read


def get_incident():
    return update_data()["cases7_per_100k_txt"]


def get_deaths():
    return update_data()["deaths"]


def get_update():
    return update_data()["last_update"]


def main():
    update_data()
    print(F"At {get_update()}")
    print("------------------------")
    print(F"Deaths:\t\t{get_deaths()}")
    print(F"Incidents:\t{get_incident()}")


if __name__ == '__main__':
    main()
