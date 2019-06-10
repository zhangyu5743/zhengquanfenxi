function[dma5,dma20,dma120] = diffma(ma5,ma20,ma120)
    %Çóµ¼¡£
    x=1:totaldata;
    dma5=diff(ma5)./diff(x);
    dma20=diff(ma20)./diff(x);
    dma120=diff(ma120)./diff(x);
end