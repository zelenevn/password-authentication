package keystrokes

import (
	model "GeneratePasswordAndOverlaps/internal/keystrokes/model"
	repomodel "GeneratePasswordAndOverlaps/internal/keystrokes/repository/keystrokes/model"
	"context"
	"sync"
)

type repository struct {
	// map k -  word, v - keystrokes
	data map[string]repomodel.Keystrokes
	m    sync.RWMutex
}

func NewRepository() *repository {
	return &repository{
		data: make(map[string]repomodel.Keystrokes),
	}
}

func (r repository) CreateOverlaps(ctx context.Context, ks []*model.Key) error {
	//TODO implement me
	panic("implement me")
}

func (r repository) CountOverlaps(ctx context.Context, ks []*model.Key) (int, error) {
	//TODO implement me
	panic("implement me")
}
