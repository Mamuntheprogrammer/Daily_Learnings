package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	reader := bufio.NewReader(os.Stdin)

	// input , err := reader.ReadString('\n')

	input, _ := reader.ReadString('\n')

	fmt.Println("Whats your Name : ", input)
}
