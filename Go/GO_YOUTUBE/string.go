package main

import (
	"fmt"
	"strings"
)
var pl = fmt.Println

func main(){

	sv1 := "A word oof ok"
	// replacer := strings.NewReplacer("A","Another")
	sv2 := strings.Replace(sv1,"o","0",-1)
	pl(sv2)
}