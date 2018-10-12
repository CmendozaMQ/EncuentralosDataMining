# from models import scrapdata
# import pandas as pd
# import numpy as np
# import csv, sqlite3
#
#
#
# dataset = pd.read_csv('../EncuentralosDataMining/155727921303318_facebook_statuses.csv')
# csvRows = dataset.iloc[:, :-9].values
# for datacsv in csvRows:
#   infocsv = np.asarray(datacsv)
#   p = scrapdata(status_id=infocsv[0], status_message=infocsv[1], status_author=infocsv[2], link_name=infocsv[3], status_type=infocsv[4], status_link=infocsv[5], permalink_url=infocsv[6], status_published=infocsv[7])
#   print(p)
#   p.save()