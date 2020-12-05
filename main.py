import sched, time
from raspberry_prog import on_off

# Librairies for Degiro API
import degiroapi
from degiroapi.product import Product
from degiroapi.utils import pretty_json
from datetime import datetime, timedelta

degiro = degiroapi.DeGiro()
degiro.login("Username", "Password")

# Choisir l'action à traquer
first_product = degiro.search_products("AIRBUS")
second_product = degiro.search_products("Total")

def action_1(action):
    # Récupérer le dernier prix de l'action
    last_product_price = degiro.real_time_price(Product(action[0]).id, degiroapi.Interval.Type.One_Day)
    lpp = last_product_price[0]['data']['lastPrice']

    # Choisir le pourcentage de baisse de l'action
    perc = 0.5

    # Choisir l'interval de baisse de l'action
    interval = "1W"

    if interval == "1D":
        interval_type = degiroapi.Interval.Type.One_Day
    elif interval == "1W":
        interval_type = degiroapi.Interval.Type.One_Week
    elif interval == "1M":
        interval_type = degiroapi.Interval.Type.One_Month
    elif interval == "1Y":
        interval_type = degiroapi.Interval.Type.One_Year
    elif interval == "3Y":
        interval_type = degiroapi.Interval.Type.Three_Years
    elif interval == "5Y":
        interval_type = degiroapi.Interval.Type.Five_Years
    elif interval == "Max":
        interval_type = degiroapi.Interval.Type.Max
    else:
        print("Fais un effort, c'est toi qui crée le prog")

    # Récupérer le premier prix de l'action en fonction de l'interval
    first_product_price = degiro.real_time_price(Product(action[-1]).id, interval_type)
    fpp = first_product_price[1]['data'][0][-1]

    if ((100 - (lpp * 100 / fpp)) > perc):
        print("Intéresse toi à cette action")
        on_off()


def action_2(action):
    # Récupérer le dernier prix de l'action
    last_product_price = degiro.real_time_price(Product(action[0]).id, degiroapi.Interval.Type.One_Day)
    lpp = last_product_price[0]['data']['lastPrice']

    # Choisir le pourcentage de baisse de l'action
    perc = 20

    # Choisir l'interval de baisse de l'action
    interval = "1W"

    if interval == "1D":
        interval_type = degiroapi.Interval.Type.One_Day
    elif interval == "1W":
        interval_type = degiroapi.Interval.Type.One_Week
    elif interval == "1M":
        interval_type = degiroapi.Interval.Type.One_Month
    elif interval == "1Y":
        interval_type = degiroapi.Interval.Type.One_Year
    elif interval == "3Y":
        interval_type = degiroapi.Interval.Type.Three_Years
    elif interval == "5Y":
        interval_type = degiroapi.Interval.Type.Five_Years
    elif interval == "Max":
        interval_type = degiroapi.Interval.Type.Max
    else:
        print("Fais un effort, c'est toi qui crée le prog")

    # Récupérer le premier prix de l'action en fonction de l'interval
    first_product_price = degiro.real_time_price(Product(action[-1]).id, interval_type)
    fpp = first_product_price[1]['data'][0][-1]

    if ((100 - (lpp * 100 / fpp)) > perc):
        print("Intéresse toi à cette action")
        on_off()


# Initialiser les trackers

while True:
    action_1(first_product)
    action_2(second_product)
    time.sleep(60)
