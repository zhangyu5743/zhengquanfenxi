function [synum,maxbenjin,nomove,beitaojiner] = analys(diefu,zhangfu,rawdata,kaolvbeitao,kaishiriqi,jiesuriqi,displayquxian)
%����ָ���ǵ����پ����Ƿ�ָ�����Ƕ��پ�����rawdata�ǹ�Ʊÿ���ǵ������Ǳ���ָ���Ǳ��������棬ͬʱ���������һ����������ʼ����ָ���Ǽ��㿪ʼ��displayָҪ��Ҫ��ʾ��ͼ��
%ÿ������ĵ�һ���е�����Ҳ������Ϊk=1��ʼ�ģ��´���Ҫ�����������
%����ͼ��û���Ǳ��׶���Ǯ���㶨
%�����ʾ���������Ҫ��Ҫ���������߼��е���ң�Ӧ�õ�������һ�������������㶨
%�����������ѡ��㶨
%���������ǹ�����Ҫ��Ҫ��������׬���ࣿ�㶨
%��������������������������㶨
%���ɿ����ֶ������ġ�
%����Ӧ���Զ��ٹ��������������������
%ϣ��ʵ�ֶ�̬��ͬһ���������Ƿ��ڲ�ͬʱ�ڵ������ԡ�
%Ӧ���ڰ����������������ϲ���һ���������ӻ��������һЩ
enddata=size(rawdata,1);
totaldata=size(rawdata,1);
begindata=1;
if(exist('kaishiriqi','var'))
    enddata=jiesuriqi;
    begindata=kaishiriqi;
end
symat(1:100)=1;%�������
mairumat(1:100)=0;%�������
%jycishu=0;%���״���
benjin(1:enddata-begindata)=0;%��ʾ��Ҫ�������
synum=0;%������
bencishouyi=0;%��������
k=1;
%tradejiluxianshi;%�����ڣ�����������������ڻ�ͼ�õ�
m=1;
danweijiner=10000;
%rawdata=[-0.05;-0.05;0.10;-0.05;0.10;-0.05;0.10];

for i=begindata:enddata
    bencishouyi=rawdata(i,1);
    symat=symat*(1+bencishouyi);
    %С��0.96����
    if symat(k)<1-diefu
        [mairumat,symat,k]=buy(danweijiner, mairumat,symat,k);
        tradejiluxianshi(m,1:3)=[i,1,danweijiner];
        m=m+1;
    end
    while (symat(k)>1+zhangfu)
        %�ж��Ƿ���Ͷ��
        if k>1%�������ʾ�У�������
            sellnum=mairumat(k);
            [mairumat,symat,synum,k] =sell(sellnum,0.005, mairumat,symat,synum,k);
            tradejiluxianshi(m,1:3)=[i,-1,sellnum];
           m=m+1;
        else%����ǵ�һ��Ҫ�ָ���1
            symat(1:100)=1;
        end
    end
    benjin(i)=sum(mairumat);
end
maxbenjin= max(benjin);
beitaojiner=sum(mairumat);

%����ʣ�µġ�
if(exist('kaolvbeitao','var'))
        %�ж��Ƿ���Ͷ��
        if(sum(mairumat)~=0)
        sellnum=sum(mairumat);
        [mairumat,symat,synum,k] =sell(sellnum,0.005, mairumat,symat,synum,k);
         tradejiluxianshi(m,1:3)=[i,-1,sellnum];
         m=m+1;
        end
end
%������˹���Ԥ���Ϳ�ͷ���β������׬���١�
nomove=rawdata(enddata,2)-rawdata(begindata,2);


%�ж��Ƿ���ʾ
if(exist('displayquxian','var'))
    a=figure(1);
    subplot(2,1,1)
    plot(benjin(1,:))
    subplot(2,1,2)
    plot(rawdata(:,1))
    %��ʾma��ԭʼ����ͼ
    b=figure();
    [ma5,ma20,ma120] =displayma(rawdata);
    %�󵼡�
    [dma5,dma20,dma120] = diffma(ma5,ma20,ma120);
    %��ʾ�����ط���
    dadian(tradejiluxianshi,rawdata(:,2),b,1)
end
end