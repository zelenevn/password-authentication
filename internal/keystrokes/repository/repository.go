package repository

import (
	model "GeneratePasswordAndOverlaps/internal/keystrokes/model"
	"context"
)

type IKeystrokeRepository interface {
	CreateOverlaps(ctx context.Context, ks []*model.Key) error
	CountOverlaps(ctx context.Context, ks []*model.Key) (int, error)
}
