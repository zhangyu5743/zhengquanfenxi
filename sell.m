function [mairumat,symat,synum,k] = sell(sellnum,feerate, mairumat,symat,synum,k)
%%��������������
restsell=sellnum;
if(restsell<=sum(mairumat))%%�ж���������ǲ���С���ܽ�
    while(restsell>0)
        if(restsell>=mairumat(k))
             restsell=restsell-mairumat(k);
            synum=synum + mairumat(k)*symat(k)*(1-feerate)- mairumat(k);%feerate�ǳ�ȥ�����ѵ�
            mairumat(k)=0;
            symat(k)=1;
            k=k-1;
        else
            synum=synum + restsell*symat(k)*(1-feerate)-restsell;%feerate�ǳ�ȥ�����ѵ�
            mairumat(k)=mairumat(k)-restsell;
            restsell=0;
        end
    end
else
    error('�����������ܽ��');
end
end