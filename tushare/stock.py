import utils
import pandas


def getStockList(pro, result_path):
    df = pro.stock_basic(
        exchange='',
        list_status='L',
        fields='''
            ts_code,symbol,name,area,
            industry,fullname,enname,market,
            exchange,curr_type,list_status,list_date,
            delist_date,is_hs
            ''')
    utils.createDirIfNotExist(result_path)
    df.to_csv(result_path)


def getTradeCal(pro, result_path, start_date, end_date):
    df = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
    utils.createDirIfNotExist(result_path)
    df.to_csv(result_path)


def getDaily(pro, result_path, ts_code, start_date, end_date):
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    utils.createDirIfNotExist(result_path)
    result = []
    if utils.fileExist(result_path):
        history = pandas.read_csv(result_path)
        result = pandas.concat([df, history], ignore_index=True)
    else:
        result = df
    result.to_csv(result_path, index=False)
