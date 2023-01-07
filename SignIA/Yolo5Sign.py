
import os
import sys
try : from ..MyModules.GestionImages import *
except : 
    sys.path.append("../MyModules/")
    from xmlGestion import *

path_to_xml = './data/imagesxml/'
list_of_xml = os.listdir(path_to_xml) 
labels = ['trafficlight', 'speedlimit', 'crosswalk', 'stop']

labels_in_french = {
    'trafficlight' : 'feux de signalisation',
    'speedlimit' : 'limitation de vitesse', 
    'crosswalk' : 'pieton', 
    'stop' : 'stop'
}

labels_in_french = {
    0 : 'feux de signalisation',
    1 : 'limitation de vitesse', 
    2 : 'pieton', 
    3 : 'stop'
}
