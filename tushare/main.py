import tushare as ts
import glog
import stock
from absl import flags, app
import pandas
from time import sleep
from tqdm import tqdm

FLAGS = flags.FLAGS
flags.DEFINE_string('op', None, 'operate')
flags.DEFINE_string('st', None, 'start date')
flags.DEFINE_string('ed', None, 'end date')
flags.DEFINE_string('tscd', None, 'ts code')
flags.DEFINE_string('td', None, 'trade date')
flags.DEFINE_boolean('all', False, 'all data')


def getTsToken():
    with open("token", 'rt') as f:
        return f.read()


def newTsAPI():
    pro = ts.pro_api(getTsToken())
    return pro


def getAndCheckStartAndEndDate():
    if FLAGS.st == "" or FLAGS.ed == "":
        glog.fatal("start_date or end_date should not be empty")
        exit(1)
    return FLAGS.st, FLAGS.ed


def getAndCheckTsCode():
    if FLAGS.tscd == "":
        glog.fatal("ts code should not be empty")
        exit(1)
    return FLAGS.tscd


def getAndCheckTradeDate():
    if FLAGS.td == "":
        glog.fatal("trade date should not be empty")
        exit(1)
    return FLAGS.td


def main(argv):
    op = FLAGS.op
    glog.info("tushare version: %s", ts.__version__)

    pro = newTsAPI()

    if op == 'stock_list':
        stock.getStockList(pro, "data/stock_list.csv")
    elif op == 'trade_cal':
        start_date, end_date = getAndCheckStartAndEndDate()
        result_path = "data/trade_cal/%s-%s.csv" % (start_date, end_date)
        stock.getTradeCal(pro, result_path, start_date, end_date)
    elif op == 'daily':
        start_date, end_date = getAndCheckStartAndEndDate()
        if FLAGS.all:
            # Update stock_list
            stock_list_file_path = "data/stock_list.csv"
            stock.getStockList(pro, stock_list_file_path)
            stocks = pandas.read_csv(stock_list_file_path)

            for ts_code in tqdm(stocks['ts_code']):
                # Max request 200/min
                sleep(0.5)
                result_path = "data/daily/%s.csv" % (ts_code)
                stock.getDaily(pro, result_path, ts_code, start_date, end_date)
        else:
            ts_code = getAndCheckTsCode()
            result_path = "data/daily/%s.csv" % (ts_code)
            stock.getDaily(pro, result_path, ts_code, start_date, end_date)
    else:
        glog.fatal("op is error")


if __name__ == "__main__":
    app.run(main)
