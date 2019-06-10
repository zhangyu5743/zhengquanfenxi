function [NUM] = readdata(wenjian)
%readdata('001302.xlsx')
cd 'C:\Users\章鱼哥\Desktop\证券分析'


[~,~,RAW]=xlsread(wenjian);
for i=2:size(RAW,1)
NUM(i,1)=str2double(RAW{i,4});
end
%处理数据读取出现NAN
NUM(isnan(NUM)) = 0;
%上下翻转
NUM=flipud(NUM);
for i=1:size(NUM,1)
NUM(i,2)=sum(NUM(1:i,1));
end
NUM=NUM/100;
end