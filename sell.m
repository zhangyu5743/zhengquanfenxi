function [mairumat,symat,synum,k] = sell(sellnum,feerate, mairumat,symat,synum,k)
%%可以卖出任意金额
restsell=sellnum;
if(restsell<=sum(mairumat))%%判断卖出金额是不是小于总金额。
    while(restsell>0)
        if(restsell>=mairumat(k))
             restsell=restsell-mairumat(k);
            synum=synum + mairumat(k)*symat(k)*(1-feerate)- mairumat(k);%feerate是除去手续费的
            mairumat(k)=0;
            symat(k)=1;
            k=k-1;
        else
            synum=synum + restsell*symat(k)*(1-feerate)-restsell;%feerate是除去手续费的
            mairumat(k)=mairumat(k)-restsell;
            restsell=0;
        end
    end
else
    error('卖出金额大于总金额');
end
end