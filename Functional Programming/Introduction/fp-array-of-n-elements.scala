object Solution extends App {

    def f(num:Int) : List[Int] = {
        val result : Array[Int] = new Array[Int](num);
        for ( i <- 0 until num) {
            result(i) = i;
        }
    
        return result.toList;
    }

    println(f(readInt))
}