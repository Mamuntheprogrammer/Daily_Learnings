package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"strconv"
)

var pl = fmt.Println

func main(){
	pl("What is your name")
	reader:= bufio.NewReader(os.Stdin)
	name,err := reader.ReadString('\n')
	if err == nil{
		pl("Hello ", name)
	}else {
		log.Fatal(err)
	}

	// variable declaration 

	var name1 string = "mamun"
	var age = 35
	var id,roll = 5,25
	pl(name1,age,id,roll)

	// Data types 
	// int , float64 , bool, string, rune
	// default type : 0,0.0,false,""

	// check type 
	pl(reflect.TypeOf(25))


	// casting 

	va1 := 5.36
	va2:= int(va1)
	pl(va2)

	va3 := "500000"
	va4 ,err := strconv.Atoi(va3)
	pl(va4,err)

	// string to float with different way of error handling

	cv7 := "3.14"
	if cv8 ,err := strconv.ParseFloat(cv7,64); err==nil{
		pl(cv8)
	}

}
