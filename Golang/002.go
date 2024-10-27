package main

import "fmt"

var lim = 4000000
var soma = 0
func main() {
	a := 1
	b := 2
	for b < lim {
		if b % 2 == 0 {
			soma = soma + b
		}
		temp := b
		b = a + temp
		a = temp 
	}
	fmt.Println(soma)
}
