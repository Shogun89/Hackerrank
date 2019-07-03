def f(arr:List[Int]):Int = {
    
    
      var total = 0.0;
      
      for ( i <- 0 to (arr.length - 1)) {
         total += 1;
      }
      return total.toInt;
}