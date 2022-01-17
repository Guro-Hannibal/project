import data_pusher
import data_puller
from relation_connector import relation_connector
import data_distributor


def __init__class_objects():
    pusher = data_pusher.DataPusher()
    puller = data_puller.DataPuller()
    distributor = data_distributor.Distributor()

