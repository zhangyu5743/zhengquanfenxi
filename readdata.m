function [NUM] = readdata(wenjian)
%readdata('001302.xlsx')
cd 'C:\Users\�����\Desktop\֤ȯ����'


[~,~,RAW]=xlsread(wenjian);
for i=2:size(RAW,1)
NUM(i,1)=str2double(RAW{i,4});
end
%�������ݶ�ȡ����NAN
NUM(isnan(NUM)) = 0;
%���·�ת
NUM=flipud(NUM);
for i=1:size(NUM,1)
NUM(i,2)=sum(NUM(1:i,1));
end
NUM=NUM/100;
end