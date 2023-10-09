package repository

import (
	"GeneratePasswordAndOverlaps/internal/generator/model"
	"context"
)

type IGeneratorRepository interface {
	CreatePassword(ctx context.Context, pg model.Generator) error
}
