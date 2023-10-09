package api

import (
	"GeneratePasswordAndOverlaps/internal/generator/converter"
	"GeneratePasswordAndOverlaps/internal/generator/service"
	"context"
	"fmt"
)

type Implementation struct {
	passwordGenerator service.GeneratorService
}

func NewImplementation(passwordGenerator service.GeneratorService) *Implementation {
	return &Implementation{
		passwordGenerator: passwordGenerator,
	}
}

func (i *Implementation) CreatePassword(ctx context.Context, length string,
	language string, options map[string]string) (string, error) {
	pg := converter.ToPasswordGeneratorFromUserInput(length, language, options)
	pass, err := i.passwordGenerator.CreatePassword(ctx, pg)
	if err != nil {
		return "", fmt.Errorf("failed to generate password: %w", err)
	}
	return pass, nil

}
