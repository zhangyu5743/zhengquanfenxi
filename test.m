%% ��ȡ��ƱƷ��
clc;clear
StockList='600276.SH'   % ѡ�����ҽҩ
%% ��ȡծȯ���̼ۣ�2013��4��2�գ�
w=windmatlab
[w_data,w_codes,w_fields,w_times,w_errorid,w_reqid]=w.wsd(StockList,'open,low,high,close','2013-01-02','2013-04-02');   
fintsPrice=fints(w_times,w_data,{'Open','High','Low','Close'},1)
fintsPrice.desc='����ҽҩ�Ĺ�Ʊ��K�߼۸�'
%% ʱ�����л�ͼ����ͼ����
% ������K��ͼ
candle(fintsPrice)
title('����ҽҩ�ɼ���K��ͼ')
% ������K�߸ߵ�ͼ
figure
highlow(fintsPrice)
title('����ҽҩ�ɼ���K�߸ߵ�ͼ')
% ��ͼ
figure
bar(fintsPrice)
title('����ҽҩ�ɼ�K�߰�ͼ')
% ���ƹ�Ʊ�۸����״ͼ
figure
kagi([w_times,w_data(:,end)])
title('����ҽҩ�ɼ���״ͼ')
% �ڰ�ͼ
figure
renko([w_times,w_data(:,end)])  
title('����ҽҩ�ɼۺڰ�ͼ')
% ��������ͼ
figure
plot(fintsPrice)
title('����ҽҩ�ɼ�����ͼ')