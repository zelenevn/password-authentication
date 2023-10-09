package service

import (
	model "GeneratePasswordAndOverlaps/internal/keystrokes/model"
	"context"
)

type KeystrokeService interface {
	CountOverlaps(ctx context.Context, ks *model.Keystroke) (int, int, int, error)
	CreateOverlaps(ctx context.Context, first model.Key, second model.Key) (model.Overlay, error)
	CreateKeystrokes(ctx context.Context, keys []model.Key) model.Keystroke
}
