#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
from mtgsdk import Set
from mtgsdk import Card

class downloadClass:

    def downloadSets:
        #Downloading all sets name in one file
        sets = Set.all()

        with open('dataSet/allSets.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'code', 'mkm_id', 'mkm_name', 'release_date'])
            for set in sets:
                writer.writerow([set.name, set.code, set.mkm_id, set.mkm_name, set.release_date])

    def downloadCards:
        #Downloading the cards from each set based in the sets list
        with open('dataSet/allSets.csv', 'r', encoding='utf-8') as setsFile:
            reader = csv.DictReader(setsFile)
            totalRows = sum(1 for row in reader)
            setsFile.seek(0)
            downloadedRows = 0
            for row in reader:
                cards = Card.where(set= row['code']).all()
                filename = re.sub(r'[\\/:"*?<>|]+', '', row['name'])
                with open('dataSet/sets/'+filename+ '.csv', 'w', encoding='utf-8') as exSetFile:
                    writerCard = csv.writer(exSetFile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writerCard.writerow(['name','multiverse_id','layout','names','mana_cost','cmc','colors',
                                         'color_identity','type','supertypes','subtypes','rarity','text','flavor',
                                         'artist','number','power','toughness','loyalty','variations','watermark','border',
                                         'timeshifted','hand','life','reserved','release_date','starter','rulings','foreign_names',
                                         'printings','original_text','original_type','legalities','source','image_url',
                                         'set','set_name','id'])
                    for card in cards:
                        writerCard.writerow([card.name,card.multiverse_id,card.layout,card.names,card.mana_cost,card.cmc,card.colors,
                                             card.color_identity,card.type,card.supertypes,card.subtypes,card.rarity,card.text,card.flavor,
                                             card.artist,card.number,card.power,card.toughness,card.loyalty,card.variations,card.watermark,card.border,
                                             card.timeshifted,card.hand,card.life,card.release_date,card.starter,card.rulings,card.foreign_names,
                                             card.printings,card.original_text,card.original_type,card.legalities,card.source,card.image_url,
                                             card.set,card.set_name,card.id])

                downloadedRows = downloadedRows + 1
                print('Downloaded '+ str(downloadedRows) + ' from ' + str(totalRows) + ' total sets')
