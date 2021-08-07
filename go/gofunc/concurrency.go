package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printA(a int) {
	defer wg.Done()
	fmt.Println(a)
}

func main() {
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go printA(i)
	}
	wg.Wait()
}
