package main

import (
	"fmt"
)

var pl = fmt.Println
  
func main(){
	for x:=1;x<6;x++{
		pl(x)
	}
	arr := [] int{1,2,3,4}
	for i,num := range arr{
		pl(i,":",num)
	}

	str := "Hello, 世界"
for _, r := range str {
    pl("%c", r)
}
}