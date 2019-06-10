function[ma5,ma20,ma120] = countma(rawdata)
 %显示趋势图,和ma5，ma20，ma120
    totaldata=size(rawdata,1);

    ma5=1:totaldata;
    ma20=1:totaldata;
    ma120=1:totaldata;
    for i=5:totaldata
        ma5(i)=sum(rawdata(i-4:i,2))/5;
    end
    for i=1:4
        ma5(i)=sum(rawdata(1:i,2))/i;
    end
    
    for i=20:totaldata
        ma20(i)=sum(rawdata(i-19:i,2))/20;
    end
    for i=1:19
        ma20(i)=sum(rawdata(1:i,2))/i;
    end
    
    for i=120:totaldata
        ma120(i)=sum(rawdata(i-119:i,2))/120;
    end
    for i=1:119
        ma120(i)=sum(rawdata(1:i,2))/i;
    end
    %求导。
    x=1:totaldata;
    a=diff(ma120)./diff(x)*100;
    %  plot(a)
end