package generator

import (
	model "GeneratePasswordAndOverlaps/internal/generator/model"
	repomodel "GeneratePasswordAndOverlaps/internal/generator/repository/generator/model"
	"context"
	"sync"
)

type repository struct {
	// K - UUID, V- REPOMODEL GENERATOR
	data map[string]repomodel.Generator
	m    sync.RWMutex
}

func NewRepository() *repository {
	return &repository{
		data: make(map[string]repomodel.Generator),
	}
}

func (r repository) CreatePassword(ctx context.Context, pg model.Generator) error {
	//TODO implement me
	panic("implement me")
}
