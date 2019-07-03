def f(arr:List[Int]):List[Int] = { 
    
    val filter_array = scala.collection.mutable.ListBuffer.empty[Int];
            
    for ( i <- 0 until arr.length){
        if ( (i % 2) == 1) {
            
            filter_array += arr(i);
        }
    }
    return filter_array.toList
}