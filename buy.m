function [mairumat,symat,k] = buy(num, mairumat,symat,k)
  k=k+1;
  mairumat(k)=num;
   symat(k)=1;
end