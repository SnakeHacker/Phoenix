import tushare as ts
import glog
import utils


def getTsToken():
    return utils.loadFile('token')


def newTsAPI():
    pro = ts.pro_api(getTsToken())
    return pro


def main():
    glog.info(ts.__version__)
    newTsAPI()


if __name__ == "__main__":
    main()
