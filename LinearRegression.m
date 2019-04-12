
input = [1,2;2,4;3,6;4,8;]
totalcost = 0;
cost = 0;
finaltotalcost = 100;
finalIndex = 100;

for i = -10:10;
  totalcost = 0;
  for index = input;
    cost = i - index(1);
    totalcost = cost * cost;
    cost2 = i - index(2);
    totalcost  = totalcost + cost2 * cost2;
  endfor;

  if(totalcost < finaltotalcost)
    finaltotalcost = totalcost;
    finalIndex = i(1);
   endif;
endfor;  
  disp(finalIndex);