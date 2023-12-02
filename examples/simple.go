package main

import "fmt"

func main() {
    sum := 0

    for i := 1; i <= 10; i++ {
        sum += i
    }

    fmt.Printf("The sum of numbers from 1 to 10 is: %d\n", sum)
}