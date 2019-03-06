import tushare as ts
import glog
import stock
from absl import flags, app

FLAGS = flags.FLAGS
flags.DEFINE_string('op', None, 'operate')


def getTsToken():
    with open("token", 'rt') as f:
        return f.read()


def newTsAPI():
    pro = ts.pro_api(getTsToken())
    return pro


def main(argv):
    op = FLAGS.op
    glog.info("tushare version: %s", ts.__version__)

    pro = newTsAPI()

    if op == 'stock_list':
        stock.getStockList(pro, "data/stock_list.csv")
    elif op == 'trade_cal':
        start_date = '20180101'
        end_date = '20180110'
        file_path = "data/trade_cal/%s-%s.csv" % (start_date, end_date)
        stock.getTradeCal(pro, file_path, start_date, end_date)
    else:
        glog.fatal("op is error")


if __name__ == "__main__":
    app.run(main)
