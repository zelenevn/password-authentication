package model

type Generator struct {
	PasswordLength int
	Language       string
	Options        []Option
}

type Option struct {
	Name       string
	Characters string
}

func NewOption(name string, characters string) *Option {
	return &Option{Name: name, Characters: characters}
}
