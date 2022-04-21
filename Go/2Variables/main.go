/*
1.Basic type: Numbers, strings, and booleans
2.Aggregate type: Array and structs
3.Reference type: Pointers, slices, maps, functions, and channels
4.Interface type
*/

package main

import "fmt"

const LogInToken string = "public variable start with variable first letter capital "

func main() {
	// learning about variable
	var username string = "GO"
	fmt.Println(username)
	fmt.Printf("The variable type is %T \n ", username)

	var isLoggedIn bool = true
	fmt.Println(isLoggedIn)
	fmt.Printf("The variable type is %T \n ", isLoggedIn)

	var smalValue uint8 = 254
	fmt.Println(smalValue)
	fmt.Printf("The variable type is %T \n ", smalValue)

	var smalFloat float32 = 254.36
	fmt.Println(smalFloat)
	fmt.Printf("The variable type is %T \n ", smalFloat)

	// Find the default value of a variable declaration

	var anotherVariable int
	fmt.Println(anotherVariable)
	fmt.Printf("The variable type is %T \n ", anotherVariable)

	// implicit type

	var uName = "Mamun"
	fmt.Println(uName)

	// no var style (Note : This will not work in out side of function )

	uName2 := "Farhan"
	fmt.Println(uName2)

}
