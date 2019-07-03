
def f(arr:List[Int]):Int = {
     
    arr.filter(x => Math.abs(x % 2) != 0).sum
 }