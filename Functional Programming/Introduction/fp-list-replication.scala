def f(num : Int, arr : List[Int]) : List[Int] = {
    
    val array_length : Int = arr.length;
    val result : Array[Int] = new Array[Int](num*array_length);
    
    for( i <- 0 until array_length) {
        val z : Int = i*num;
        
        for(n <- 0 until num) {
            result(z + n) = arr(i);
        }
    }
    
    return result.toList;
}






