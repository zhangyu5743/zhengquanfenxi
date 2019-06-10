%寻找synum与maxbenjin最大的比值对应的跌幅和涨幅。  紫色和黄色
cd 'C:\Users\章鱼哥\Desktop\证券分析'
rawdata=readdata('001986.xlsx');
    chongfucishu=100;
    yingtoubi(1:chongfucishu,1:chongfucishu)=1;
    for i=1:chongfucishu
        for j=1:chongfucishu
            diefu=i/1000;
            zhangfu=j/1000;
             [synum,maxbenjin] = analys(diefu,zhangfu,rawdata,1,438,500);
            yingtoubi(i,j)=synum/maxbenjin;
        end
    end
    %寻找最大盈投比
  maxyingtoubi=max(yingtoubi);
  maxyingtoubi=max(maxyingtoubi)
    [i1,i2]=find(yingtoubi==maxyingtoubi);
 diefu=i1/1000
 zhangfu=i2/1000
 %以最大盈投比来进行一次运算
 [synum,maxbenjin,nomove,beitaojiner] = analys(diefu,zhangfu,rawdata,1,438,500,1)
  synum/maxbenjin
  rawdata(500,2)-rawdata(438,2);
  %显示盈投比的矩阵
 figure()
  Z=yingtoubi;
  [X,Y]=meshgrid(1:chongfucishu, 1:chongfucishu);
  surf(X, Y, Z)
  %显示盈投比减去不操作的矩阵
  figure()
    Z=yingtoubi-nomove;
  [X,Y]=meshgrid(1:chongfucishu, 1:chongfucishu);
  surf(X, Y, Z)