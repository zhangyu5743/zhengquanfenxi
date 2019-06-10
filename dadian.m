function dadian(tradejiluxianshi,rawdata,tuceng,chuangkou)
x=tradejiluxianshi(:,1);
maiormai=tradejiluxianshi(:,2);
xianshizhi=tradejiluxianshi(:,3);
figure(tuceng);
    subplot(1,1,chuangkou)
  hold on;
  y=rawdata;
for i = 1:length(x)
     if(maiormai(i)==1)
           plot(x(i),y(x(i)),'*','Color','red')
    text(x(i),y(x(i)),{['(' num2str(x(i)) ',' num2str(y(x(i))) ',' num2str(xianshizhi(i)) ')' ] },'Color','red','FontSize',10,'FontWeight','bold');
     end
          if(maiormai(i)==-1)
                        plot(x(i),y(x(i)),'*','Color','blue')
    text(x(i),y(x(i)),{['(' num2str(x(i)) ',' num2str(y(x(i))) ',' num2str(xianshizhi(i)) ')' ] },'Color','blue','FontSize',10,'FontWeight','bold');
          end
end
end