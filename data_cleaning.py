import pandas as pd

fileLocation = '/home/mahendra/ALDA/Pokemon/300k.csv'
columnDropList = ['pokemonId','latitude', 'longitude', 'appearedLocalTime', '_id', 'cellId_90m','cellId_180m','cellId_370m',
                  'cellId_730m','cellId_1460m', 'cellId_2920m', 'cellId_5850m', 'appearedTimeOfDay', 'appearedHour',
                  'appearedMinute', 'appearedDayOfWeek', 'appearedMonth', 'appearedYear', 'class', 'continent','pokestopDistanceKm']

coocColumnsDropList = ['cooc_1', 'cooc_2', 'cooc_3', 'cooc_4', 'cooc_5', 'cooc_6', 'cooc_7', 'cooc_8', 'cooc_9', 'cooc_10',
                       'cooc_11', 'cooc_12', 'cooc_13', 'cooc_14', 'cooc_15', 'cooc_16', 'cooc_17', 'cooc_18', 'cooc_19',
                       'cooc_20', 'cooc_21', 'cooc_22', 'cooc_23', 'cooc_24', 'cooc_25', 'cooc_26', 'cooc_27', 'cooc_28',
                       'cooc_29', 'cooc_30', 'cooc_31', 'cooc_32', 'cooc_33', 'cooc_34', 'cooc_35', 'cooc_36', 'cooc_37',
                       'cooc_38', 'cooc_39', 'cooc_40', 'cooc_41', 'cooc_42', 'cooc_43', 'cooc_44', 'cooc_45', 'cooc_46',
                       'cooc_47', 'cooc_48', 'cooc_49', 'cooc_50', 'cooc_51', 'cooc_52', 'cooc_53', 'cooc_54', 'cooc_55',
                       'cooc_56', 'cooc_57', 'cooc_58', 'cooc_59', 'cooc_60', 'cooc_61', 'cooc_62', 'cooc_63', 'cooc_64',
                       'cooc_65', 'cooc_66', 'cooc_67', 'cooc_68', 'cooc_69', 'cooc_70', 'cooc_71', 'cooc_72', 'cooc_73',
                       'cooc_74', 'cooc_75', 'cooc_76', 'cooc_77', 'cooc_78', 'cooc_79', 'cooc_80', 'cooc_81', 'cooc_82',
                       'cooc_83', 'cooc_84', 'cooc_85', 'cooc_86', 'cooc_87', 'cooc_88', 'cooc_89', 'cooc_90', 'cooc_91',
                       'cooc_92', 'cooc_93', 'cooc_94', 'cooc_95', 'cooc_96', 'cooc_97', 'cooc_98', 'cooc_99', 'cooc_100',
                       'cooc_101', 'cooc_102', 'cooc_103', 'cooc_104', 'cooc_105', 'cooc_106', 'cooc_107', 'cooc_108',
                       'cooc_109', 'cooc_110', 'cooc_111', 'cooc_112', 'cooc_113', 'cooc_114', 'cooc_115', 'cooc_116',
                       'cooc_117', 'cooc_118', 'cooc_119', 'cooc_120', 'cooc_121', 'cooc_122', 'cooc_123', 'cooc_124',
                       'cooc_125', 'cooc_126', 'cooc_127', 'cooc_128', 'cooc_129', 'cooc_130', 'cooc_131', 'cooc_132',
                       'cooc_133', 'cooc_134', 'cooc_135', 'cooc_136', 'cooc_137', 'cooc_138', 'cooc_139', 'cooc_140',
                       'cooc_141', 'cooc_142', 'cooc_143', 'cooc_144', 'cooc_145', 'cooc_146', 'cooc_147', 'cooc_148',
                       'cooc_149', 'cooc_150', 'cooc_151']


columnDropList += coocColumnsDropList

weather_mapping = {'Breezy':0, 'BreezyandMostlyCloudy':1, 'BreezyandOvercast':2,'BreezyandPartlyCloudy':3,'Clear':4,'DangerouslyWindy':5,
                    'Drizzle':6,'DrizzleandBreezy':7,'Dry':8,'DryandMostlyCloudy':9,'DryandPartlyCloudy':10,'Foggy':11,
                    'HeavyRain':12,'Humid':13,'HumidandOvercast':14, 'HumidandPartlyCloudy':15,'LightRain':16,'LightRainandBreezy':17,'MostlyCloudy':18,'Overcast':19,
                    'PartlyCloudy':20,'Rain':21,'RainandWindy':22,'Windy':23,'WindyandFoggy':24,'WindyandPartlyCloudy':25}

weatherIconMapping = {'clear-day':0,'clear-night':1,'cloudy':2,'fog':3, 'partly-cloudy-day':4,
                'partly-cloudy-night':5,'rain':6,'wind':7}

pokemonIdToTypeMapping = {1: 'Grass', 2: 'Grass', 3: 'Grass', 4: 'Fire', 5: 'Fire', 6: 'Fire', 7: 'Water', 8: 'Water', 9: 'Water', 10: 'Bug', 11: 'Bug', 12: 'Bug', 13: 'Bug', 14: 'Bug', 15: 'Bug', 16: 'Normal', 17: 'Normal', 18: 'Normal', 19: 'Normal', 20: 'Normal', 21: 'Normal', 22: 'Normal', 23: 'Poison', 24: 'Poison', 25: 'Electric', 26: 'Electric', 27: 'Ground', 28: 'Ground', 29: 'Poison', 30: 'Poison', 31: 'Poison', 32: 'Poison', 33: 'Poison', 34: 'Poison', 35: 'Fairy', 36: 'Fairy', 37: 'Fire', 38: 'Fire', 39: 'Normal', 40: 'Normal', 41: 'Poison', 42: 'Poison', 43: 'Grass', 44: 'Grass', 45: 'Grass', 46: 'Bug', 47: 'Bug', 48: 'Bug', 49: 'Bug', 50: 'Ground', 51: 'Ground', 52: 'Normal', 53: 'Normal', 54: 'Water', 55: 'Water', 56: 'Fighting', 57: 'Fighting', 58: 'Fire', 59: 'Fire', 60: 'Water', 61: 'Water', 62: 'Water', 63: 'Psychic', 64: 'Psychic', 65: 'Psychic', 66: 'Fighting', 67: 'Fighting', 68: 'Fighting', 69: 'Grass', 70: 'Grass', 71: 'Grass', 72: 'Water', 73: 'Water', 74: 'Rock', 75: 'Rock', 76: 'Rock', 77: 'Fire', 78: 'Fire', 79: 'Water', 80: 'Water', 81: 'Electric', 82: 'Electric', 83: 'Normal', 84: 'Normal', 85: 'Normal', 86: 'Water', 87: 'Water', 88: 'Poison', 89: 'Poison', 90: 'Water', 91: 'Water', 92: 'Ghost', 93: 'Ghost', 94: 'Ghost', 95: 'Rock', 96: 'Psychic', 97: 'Psychic', 98: 'Water', 99: 'Water', 100: 'Electric', 101: 'Electric', 102: 'Grass', 103: 'Grass', 104: 'Ground', 105: 'Ground', 106: 'Fighting', 107: 'Fighting', 108: 'Normal', 109: 'Poison', 110: 'Poison', 111: 'Ground', 112: 'Ground', 113: 'Normal', 114: 'Grass', 115: 'Normal', 116: 'Water', 117: 'Water', 118: 'Water', 119: 'Water', 120: 'Water', 121: 'Water', 122: 'Psychic', 123: 'Bug', 124: 'Ice', 125: 'Electric', 126: 'Fire', 127: 'Bug', 128: 'Normal', 129: 'Water', 130: 'Water', 131: 'Water', 132: 'Normal', 133: 'Normal', 134: 'Water', 135: 'Electric', 136: 'Fire', 137: 'Normal', 138: 'Rock', 139: 'Rock', 140: 'Rock', 141: 'Rock', 142: 'Rock', 143: 'Normal', 144: 'Ice', 145: 'Electric', 146: 'Fire', 147: 'Dragon', 148: 'Dragon', 149: 'Dragon', 150: 'Psychic', 151: 'Psychic'}

upokemonTypeToId = {'Ghost': 0, 'Electric': 1, 'Normal': 3, 'Fire': 4, 'Psychic': 5, 'Fighting': 9, 'Ice': 2, 'Dragon': 7, 'Water': 8, 'Poison': 6, 'Rock': 10, 'Fairy': 11, 'Grass': 12, 'Bug': 13, 'Ground': 14}

def headers(data):
    columns = list(data.columns.values)
    num = range(1, 208)
    print zip(num,columns)

def dropColumns(data, dropColumnList):
    axis = 1 #Column wise deletion
    for column in dropColumnList:
      data.drop(column, axis, inplace=True)
    return data

def getData(fileLocation):
    global columnDropList
    data = pd.read_csv(fileLocation, low_memory=False)
    data = dropColumns(data, columnDropList)
    data = mapStringsToLabels(data)
    return data

def filterDataBasedOnCity(data, city):
    newData = data[data.city == city]
    return dropColumns(newData, ['city'])

def getLabel(fileLocation, city='New_York'):
    data = pd.read_csv(fileLocation, low_memory=False)
    data = data[data.city == city]
    data = data.replace({'pokemonId': pokemonIdToTypeMapping})
    data = data.replace({'pokemonId':upokemonTypeToId})
    return data[[0]]

def mapStringsToLabels(data):
    global weather_mapping
    global weatherIconMapping
    return data.replace({'weather': weather_mapping, 'weatherIcon':weatherIconMapping})


if __name__ == '__main__':
    data = getData(fileLocation)
    target = getLabel(fileLocation)
    nydata = filterDataBasedOnCity(data, 'New_York')
    print nydata
