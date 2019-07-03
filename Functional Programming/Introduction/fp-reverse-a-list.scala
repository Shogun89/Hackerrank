def f(arr:List[Int]):List[Int] = {
    
    val reverse = scala.collection.mutable.ListBuffer.empty[Int];
    
    for ( i <- arr.length -1 to 0 by -1){
        
        reverse += arr(i);
    }
    return reverse.toList
}