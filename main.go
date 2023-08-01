package main

import "fmt"

func foldArray(arr *[]int, runs int) {
	for i := 0; i < runs; i++ {
		folding(arr)
	}
}

func folding(arr *[]int) {
	length := len(*arr)
	half := length/2 + length%2

	for i := 0; i < half-len(*arr)%2; i++ {
		(*arr)[i] += (*arr)[length-i-1]
	}

	(*arr) = (*arr)[:half]
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
 	foldArray(&arr1, 1)
	fmt.Println(arr1) 

	arr2 := []int{1, 2, 3, 4, 5}
	foldArray(&arr2, 2)
	fmt.Println(arr2) 
}

