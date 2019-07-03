def f(delim:Int,arr:List[Int]):List[Int] = { 
    
    val filter_array = scala.collection.mutable.ListBuffer.empty[Int];
    
    for ( i <- 0 until arr.length){
        if ( arr(i) < delim) {
            
            filter_array += arr(i);
        }
    }
    return filter_array.toList
}