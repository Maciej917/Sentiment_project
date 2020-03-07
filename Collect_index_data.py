import pandas_datareader.data as web


class DownloadingCompanyIndex:
    """ Clasa odpowiedzialna za pobieranie dziennych cen danej firmy. """
    def DownloadFromStooq(self, CompanyInStooq):
        """ Metoda pobiera ceny danej firmy ze stooq'a"""
        company_index = web.DataReader("{}".format(CompanyInStooq), 'stooq' )
        return company_index















#print(DownloadingCompanyIndexFromStooq().DownloadIndex("GOOGL.US"))


