%Ѱ��synum��maxbenjin���ı�ֵ��Ӧ�ĵ������Ƿ���  ��ɫ�ͻ�ɫ
cd 'C:\Users\�����\Desktop\֤ȯ����'
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
    %Ѱ�����ӯͶ��
  maxyingtoubi=max(yingtoubi);
  maxyingtoubi=max(maxyingtoubi)
    [i1,i2]=find(yingtoubi==maxyingtoubi);
 diefu=i1/1000
 zhangfu=i2/1000
 %�����ӯͶ��������һ������
 [synum,maxbenjin,nomove,beitaojiner] = analys(diefu,zhangfu,rawdata,1,438,500,1)
  synum/maxbenjin
  rawdata(500,2)-rawdata(438,2);
  %��ʾӯͶ�ȵľ���
 figure()
  Z=yingtoubi;
  [X,Y]=meshgrid(1:chongfucishu, 1:chongfucishu);
  surf(X, Y, Z)
  %��ʾӯͶ�ȼ�ȥ�������ľ���
  figure()
    Z=yingtoubi-nomove;
  [X,Y]=meshgrid(1:chongfucishu, 1:chongfucishu);
  surf(X, Y, Z)