import pandas as pd
from Collect_index_data import DownloadingCompanyIndex


class Modifing_csv_data:


    def modifing_reuters_date(self, filename):

        art_data = pd.read_csv(filename)
        art_data = art_data.drop(columns="Unnamed: 0")
        index = 0
        for date_not_modif in art_data["date"]:
            date_semi_modified = date_not_modif.split("/")
            date_modified = pd.to_datetime(date_semi_modified[0])
            art_data.iat[index, 1] = date_modified
            index += 1
        art_data["date"] = art_data['date'].astype('datetime64[ns]')
        art_data = art_data.set_index(["date"])
        art_data.to_csv("art_body_text_2.csv", header = True, index= True)


    def mergingstooqwithart(self, filename):
        art_data = pd.read_csv(filename)
        company_index = DownloadingCompanyIndex().DownloadFromStooq("GOOGL")
        company_index["date"]=company_index.index
        art_data["date"] = art_data['date'].astype('datetime64[ns]')
        frames = [art_data, company_index]
        merged_data = pd.merge(art_data, company_index, on="date", how="left")
        merged_data.to_csv("merged_data.csv", header=True, index=True)


################# Przykładowe wywołanie #######################

# Modifing_csv_data().modifing_reuters_date("art_body_text.csv")
# Modifing_csv_data().mergingstooqwithart("art_body_text_2.csv")
