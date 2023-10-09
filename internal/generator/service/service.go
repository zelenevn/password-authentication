package service

import (
	"GeneratePasswordAndOverlaps/internal/generator/model"
	"context"
)

type GeneratorService interface {
	CreatePassword(ctx context.Context, pg model.Generator) (string, error)
}
