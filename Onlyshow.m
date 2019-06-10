cd 'C:\Users\’¬”„∏Á\Desktop\÷§»Ø∑÷Œˆ'
rawdata=readdata('001986.xlsx');
 totaldata=size(rawdata,1);
[ma5,ma20,ma120]=countma(rawdata);
 ma0_20=1:totaldata;
    for i=1:totaldata
        ma0_20=rawdata(:,2)-ma20(:);
    end
    ma0_20ave5=1:totaldata;
     for i=20:totaldata
        ma0_20ave5(i)=sum(ma0_20(i-4:i))/20;
    end
    for i=1:19
        ma0_20ave5(i)=sum(ma0_20(1:i))/i;
    end
     a=figure(1);
       hold on
    plot(rawdata(:,2))
     plot(ma120)
     plot(ma20)
     plot(ma5)
     a=figure(2);
      hold on
     plot(ma0_20)
    plot(ma0_20ave5)
