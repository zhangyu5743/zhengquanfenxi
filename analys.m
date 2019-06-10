function [synum,maxbenjin,nomove,beitaojiner] = analys(diefu,zhangfu,rawdata,kaolvbeitao,kaishiriqi,jiesuriqi,displayquxian)
%跌幅指的是跌多少就买，涨幅指的是涨多少就卖，rawdata是股票每日涨跌，考虑被套指的是被套在里面，同时按照最后那一天卖出，开始日期指的是计算开始，display指要不要显示出图表。
%每个矩阵的第一个有点问题也就是因为k=1开始的，下次需要处理这个问题
%还有图像，没考虑被套多少钱。搞定
%收益率矩阵来决定要不要买这样子逻辑有点混乱，应该单独独立一个变量出来。搞定
%考虑了手续费。搞定
%计算在上涨过程中要不要操作可以赚更多？搞定
%买入卖出函数单独抽象出来，搞定
%做成可以手动操作的。
%买卖应该以多少股来看，这样子容易理解
%希望实现动态，同一个跌幅和涨幅在不同时期的适用性。
%应该在把买入矩阵和收益矩阵合并成一个，这样子或许或许会好一些
enddata=size(rawdata,1);
totaldata=size(rawdata,1);
begindata=1;
if(exist('kaishiriqi','var'))
    enddata=jiesuriqi;
    begindata=kaishiriqi;
end
symat(1:100)=1;%收益矩阵
mairumat(1:100)=0;%买入矩阵
%jycishu=0;%交易次数
benjin(1:enddata-begindata)=0;%表示需要本金多少
synum=0;%总收益
bencishouyi=0;%本次收益
k=1;
%tradejiluxianshi;%【日期，买入或卖出，金额】用于画图用的
m=1;
danweijiner=10000;
%rawdata=[-0.05;-0.05;0.10;-0.05;0.10;-0.05;0.10];

for i=begindata:enddata
    bencishouyi=rawdata(i,1);
    symat=symat*(1+bencishouyi);
    %小于0.96就买
    if symat(k)<1-diefu
        [mairumat,symat,k]=buy(danweijiner, mairumat,symat,k);
        tradejiluxianshi(m,1:3)=[i,1,danweijiner];
        m=m+1;
    end
    while (symat(k)>1+zhangfu)
        %判断是否有投资
        if k>1%大于零表示有，则卖出
            sellnum=mairumat(k);
            [mairumat,symat,synum,k] =sell(sellnum,0.005, mairumat,symat,synum,k);
            tradejiluxianshi(m,1:3)=[i,-1,sellnum];
           m=m+1;
        else%如果是第一个要恢复成1
            symat(1:100)=1;
        end
    end
    benjin(i)=sum(mairumat);
end
maxbenjin= max(benjin);
beitaojiner=sum(mairumat);

%卖出剩下的。
if(exist('kaolvbeitao','var'))
        %判断是否有投资
        if(sum(mairumat)~=0)
        sellnum=sum(mairumat);
        [mairumat,symat,synum,k] =sell(sellnum,0.005, mairumat,symat,synum,k);
         tradejiluxianshi(m,1:3)=[i,-1,sellnum];
         m=m+1;
        end
end
%如果不人工干预，就开头买结尾卖可以赚多少。
nomove=rawdata(enddata,2)-rawdata(begindata,2);


%判断是否显示
if(exist('displayquxian','var'))
    a=figure(1);
    subplot(2,1,1)
    plot(benjin(1,:))
    subplot(2,1,2)
    plot(rawdata(:,1))
    %显示ma和原始曲线图
    b=figure();
    [ma5,ma20,ma120] =displayma(rawdata);
    %求导。
    [dma5,dma20,dma120] = diffma(ma5,ma20,ma120);
    %显示买卖地方。
    dadian(tradejiluxianshi,rawdata(:,2),b,1)
end
end