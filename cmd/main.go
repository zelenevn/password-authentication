package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"pw-auth/internal"
	"strconv"
)

/*
13. Реализовать программу для генерации паролей пользователей. Программа должна формировать случайную последовательность
символов длины L, при этом должен использоваться алфавит из A символов. Составить частотный словарь вхождения символов
алфавита в парольную фразу.

Пример запуска: main.exe 20 30 100 bar-20-30-100.html
*/

func main() {
	if len(os.Args) >= 5 {
		l, err := strconv.ParseUint(os.Args[1], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		count, err := strconv.ParseUint(os.Args[2], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		iterations, err := strconv.ParseUint(os.Args[3], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		filename := os.Args[4]
		if len(filename) == 0 {
			log.Fatal(errors.New("filename is too low"))
		}

		alphabet := internal.LettersLowerCase + internal.Numbers + internal.SpecialChars
		alphabet = alphabet[:count]
		result := internal.FrequentDict(uint(l), alphabet, uint(iterations))

		f, err := os.Create(filename)
		if err != nil {
			log.Fatal(err)
		}
		internal.OutputToHtml(result, f)
	} else {
		fmt.Println("too few arguments")
		fmt.Println("usage: <launch command> <L:int> <A:int> <Iterations:int> <OutputFilename>")
	}
}
