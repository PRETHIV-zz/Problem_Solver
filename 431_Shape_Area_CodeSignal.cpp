/*

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

Please chek with the screenshot in this repo for visual problem statement

[execution time limit] 0.5 seconds (cpp)

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer

The area of the n-interesting polygon.


PC: I didn't put DP ...if u want put DP to optimize it further

*/

int shapeArea(int n) {
    if(n==1){
        return 1;
    }
    else{
        return (n-1)*4+shapeArea(n-1);
    }
}
