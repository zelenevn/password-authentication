package internal

import "math/rand"

type RandomStringGenerator struct {
	letters []rune
}

const LettersAnyCase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
const LettersLowerCase = "abcdefghijklmnopqrstuvwxyz"
const LettersUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const Numbers = "0123456789"
const SpecialChars = "!@#$%^&*()_"

func New(letters string) *RandomStringGenerator {
	return &RandomStringGenerator{
		letters: []rune(letters),
	}
}

func (gen *RandomStringGenerator) String(length int) string {
	b := make([]rune, length)
	l := len(gen.letters)
	for i := range b {
		b[i] = gen.letters[rand.Intn(l)]
	}
	return string(b)
}
