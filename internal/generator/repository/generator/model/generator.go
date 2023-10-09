package model

type Generator struct {
	UId            string
	PasswordLength int
	Language       string
	Options        []Option
}

type Option struct {
	Name       string
	Characters string
}
