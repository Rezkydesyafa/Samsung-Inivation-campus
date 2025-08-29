package main

import (
	"fmt"
	"math/big"
)

func main() {
	var A, B int64
	fmt.Scan(&A, &B)

	// 25^A
	pow25 := big.NewInt(1)
	pow25.Exp(big.NewInt(25), big.NewInt(A), nil)

	// 17081945^B
	powN := big.NewInt(1)
	powN.Exp(big.NewInt(17081945), big.NewInt(B), nil)

	// powN % pow25 == 0 ?
	mod := big.NewInt(0)
	mod.Mod(powN, pow25)
	if mod.Cmp(big.NewInt(0)) == 0 {
		fmt.Println("Ya")
	} else {
		fmt.Println("Tidak")
	}
}
