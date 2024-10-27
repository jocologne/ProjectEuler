package main

import "fmt"

var res = 0
func main() {
	i := 0
	for i < 1000 {
		if i % 3 == 0 || i % 5 == 0 {
			res = res + i
		}
		i++
	}
	fmt.Println(res)
}
