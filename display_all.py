import matplotlib.pyplot as plt
from datetime import datetime
import os
sfrooturl = "C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/"
for root, dirs, files in os.walk(sfrooturl):
    sfsrcfile_name = [m[:-4] for m in files]
    print(sfsrcfile_name)  # 当前路径下所有非目录子文件

strooturl = "C:/Users/章鱼哥/Desktop/证券分析/gpdata/data/"
for root, dirs, files in os.walk(strooturl):

    print(files)  # 当前路径下所有非目录子文件
    stsrcfile_name =  [m[:-4] for m in files]
def st_show_data_kmm(fundnum, rooturl, a):
    if fundnum not in stsrcfile_name:
        print("找不到该代码的理财产品")
        return
    res = open(rooturl + fundnum + '.csv', "r", errors='ignore')
    reslines = res.readlines()  # 读取文件中的内容所有内容
    res.close()
    # 去除第一行
    if (reslines):
        reslines = reslines[1:]
        # 数组颠倒
        reslines = reslines[::-1]
        # 分割成二维数组
        for i in range(len(reslines)):
            reslines[i] = reslines[i].split(',')
        # 获取单位净值
        net_asset_value = [i[7] for i in reslines]
        for i in range(len(net_asset_value)):
            net_asset_value[i] = float(net_asset_value[i])
        # print(net_asset_value)
        # 获取日期
        date = [i[0] for i in reslines]
        print(date[0])
        print(date[-1])
        # 计算ma
        ma5 = net_asset_value[:];
        ma20 = net_asset_value[:];
        ma120 = net_asset_value[:];
        for i in range(5, len(net_asset_value)):
            ma5[i] = sum(net_asset_value[i - 4:i + 1]) / 5;
        for i in range(0, 5):
            ma5[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(20, len(net_asset_value)):
            ma20[i] = sum(net_asset_value[i - 19:i + 1]) / 20;
        for i in range(0, 20):
            ma20[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(120, len(net_asset_value)):
            ma120[i] = sum(net_asset_value[i - 119:i + 1]) / 120;
        for i in range(0, 120):
            ma120[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        kmm_value20 = net_asset_value[:];
        for i in range(0, len(net_asset_value)):
            kmm_value20[i] = net_asset_value[i] - ma20[i];

        kmm_value5 = net_asset_value[:];
        for i in range(0, len(net_asset_value)):
            kmm_value5[i] = net_asset_value[i] - ma5[i];

        y0 = [0 for i in range(len(net_asset_value))]
        # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
        xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
        a.set_title(fundnum)
        wide = '2'
        a.plot(xs, y0, '-', linewidth=wide)
        a.plot(xs, kmm_value20, '-', linewidth=wide, label="kmm20")
        a.plot(xs, kmm_value5, '-', linewidth=wide, label="kmm5")
        a.legend(loc='upper left')
        a.set_xlabel('Date')
        a.set_ylabel('value')
        a.text(xs[-1], net_asset_value[-1], net_asset_value[-1], ha='right', va='bottom', fontsize=10)
        print(fundnum)

        return





def st_show_data_ma(fundnum, rooturl, a):
    if fundnum not in stsrcfile_name:
        print("找不到该代码的理财产品")
        return
    res = open(rooturl + fundnum + '.csv', "r", errors='ignore')
    reslines = res.readlines()  # 读取文件中的内容所有内容
    res.close()
    # 去除第一行
    if (reslines):
        reslines = reslines[1:]
        # 数组颠倒
        reslines = reslines[::-1]
        # 分割成二维数组
        for i in range(len(reslines)):
            reslines[i] = reslines[i].split(',')
        # 获取单位净值
        net_asset_value = [i[7] for i in reslines]
        for i in range(len(net_asset_value)):
            net_asset_value[i] = float(net_asset_value[i])
        # print(net_asset_value)
        # 获取日期
        date = [i[0] for i in reslines]
        print(date[0])
        print(date[-1])
        # 计算ma
        ma5 = net_asset_value[:];
        ma20 = net_asset_value[:];
        ma120 = net_asset_value[:];
        for i in range(5, len(net_asset_value)):
            ma5[i] = sum(net_asset_value[i - 4:i + 1]) / 5;
        for i in range(0, 5):
            ma5[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(20, len(net_asset_value)):
            ma20[i] = sum(net_asset_value[i - 19:i + 1]) / 20;
        for i in range(0, 20):
            ma20[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(120, len(net_asset_value)):
            ma120[i] = sum(net_asset_value[i - 119:i + 1]) / 120;
        for i in range(0, 120):
            ma120[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        #        # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
        # plt.rcParams['savefig.dpi'] = 100 #图片像素
        # a.rcParams['figure.dpi'] = 200#分辨率
        xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
        a.set_title(fundnum)
        wide = '1'
        a.plot(xs, net_asset_value, '-', linewidth=wide, label="net_asset_value")
        a.plot(xs, ma5, '-', linewidth=wide, label="ma5")
        a.plot(xs, ma20, '-', linewidth=wide, label="ma20")
        a.plot(xs, ma120, '-', linewidth=wide, label="ma120")
        a.legend(loc='upper left')
        a.set_xlabel('Date')
        a.set_ylabel('value')
        a.text(xs[-1], net_asset_value[-1], net_asset_value[-1], ha='right', va='bottom', fontsize=10)
        # a.plt.margins(0, 0)
        print(fundnum)

        return


def sf_show_data_ma(fundnum, rooturl, a):
    if fundnum not in sfsrcfile_name:
        print("找不到该代码的理财产品")
        return
    res = open(rooturl + fundnum + '.txt', "r", errors='ignore')
    reslines = res.readlines()  # 读取文件中的内容所有内容
    res.close()
    # 去除第一行
    if (reslines):
        reslines = reslines[1:]
        # 数组颠倒
        reslines = reslines[::-1]
        # 分割成二维数组
        for i in range(len(reslines)):
            reslines[i] = reslines[i].split(' ')
        # 获取单位净值
        net_asset_value = [i[1] for i in reslines]
        for i in range(len(net_asset_value)):
            net_asset_value[i] = float(net_asset_value[i])
        # print(net_asset_value)
        # 获取日期
        date = [i[0] for i in reslines]
        print(date[0])
        print(date[-1])
        # 计算ma
        ma5 = net_asset_value[:];
        ma20 = net_asset_value[:];
        ma120 = net_asset_value[:];
        for i in range(5, len(net_asset_value)):
            ma5[i] = sum(net_asset_value[i - 4:i + 1]) / 5;
        for i in range(0, 5):
            ma5[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(20, len(net_asset_value)):
            ma20[i] = sum(net_asset_value[i - 19:i + 1]) / 20;
        for i in range(0, 20):
            ma20[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(120, len(net_asset_value)):
            ma120[i] = sum(net_asset_value[i - 119:i + 1]) / 120;
        for i in range(0, 120):
            ma120[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        #        # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
        # plt.rcParams['savefig.dpi'] = 100 #图片像素
        # a.rcParams['figure.dpi'] = 200#分辨率
        xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
        a.set_title(fundnum)
        wide = '2'
        a.plot(xs, net_asset_value, '-', linewidth=wide, label="net_asset_value")
        a.plot(xs, ma5, '-', linewidth=wide, label="ma5")
        a.plot(xs, ma20, '-', linewidth=wide, label="ma20")
        a.plot(xs, ma120, '-', linewidth=wide, label="ma120")
        a.legend(loc='upper left')
        a.set_xlabel('Date')
        a.set_ylabel('value')
        a.text(xs[-1], net_asset_value[-1], net_asset_value[-1], ha='right', va='bottom', fontsize=10)
        print(fundnum)

        return
def sf_show_data_kmm(fundnum, rooturl, a):
    if fundnum not in sfsrcfile_name:
        print("找不到该代码的理财产品")
        return
    res = open(rooturl + fundnum + '.txt', "r", errors='ignore')
    reslines = res.readlines()  # 读取文件中的内容所有内容
    res.close()
    # 去除第一行
    if (reslines):
        reslines = reslines[1:]
        # 数组颠倒
        reslines = reslines[::-1]
        # 分割成二维数组
        for i in range(len(reslines)):
            reslines[i] = reslines[i].split(' ')
        # 获取单位净值
        net_asset_value = [i[1] for i in reslines]
        for i in range(len(net_asset_value)):
            net_asset_value[i] = float(net_asset_value[i])
        # print(net_asset_value)
        # 获取日期
        date = [i[0] for i in reslines]
        print(date[0])
        print(date[-1])
        # 计算ma
        ma5 = net_asset_value[:];
        ma20 = net_asset_value[:];
        ma120 = net_asset_value[:];
        for i in range(5, len(net_asset_value)):
            ma5[i] = sum(net_asset_value[i - 4:i + 1]) / 5;
        for i in range(0, 5):
            ma5[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(20, len(net_asset_value)):
            ma20[i] = sum(net_asset_value[i - 19:i + 1]) / 20;
        for i in range(0, 20):
            ma20[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        for i in range(120, len(net_asset_value)):
            ma120[i] = sum(net_asset_value[i - 119:i + 1]) / 120;
        for i in range(0, 120):
            ma120[i] = sum(net_asset_value[:(i + 1)]) / (i + 1);

        kmm_value20 = net_asset_value[:];
        for i in range(0, len(net_asset_value)):
            kmm_value20[i] = net_asset_value[i] - ma20[i];

        kmm_value5 = net_asset_value[:];
        for i in range(0, len(net_asset_value)):
            kmm_value5[i] = net_asset_value[i] - ma5[i];

        y0 = [0 for i in range(len(net_asset_value))]
        # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
        xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
        a.set_title(fundnum)
        wide = '2'
        a.plot(xs, y0, '-', linewidth=wide)
        a.plot(xs, kmm_value20, '-', linewidth=wide, label="kmm20")
        a.plot(xs, kmm_value5, '-', linewidth=wide, label="kmm5")
        a.legend(loc='upper left')
        a.set_xlabel('Date')
        a.set_ylabel('value')
        a.text(xs[-1], net_asset_value[-1], net_asset_value[-1], ha='right', va='bottom', fontsize=10)
        print(fundnum)

        return