#!/bin/awk

# Usage: ls -v path/ | awk -f getGaps.awk > output.txt

BEGIN{
  FS="_";
  first = 1;
  x = 0;
}
{
  if(first == 1){
    first = 0;
    x = $4 + 1;
  }
  else{
    while(x != $4 && $4 != ""){
      print x;
      x = x + 1;
      if(x == 1010) break;
    }
    x = x + 1;
  }
}
