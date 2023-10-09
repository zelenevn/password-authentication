package api

import (
	"GeneratePasswordAndOverlaps/internal/keystrokes/converter"
	"GeneratePasswordAndOverlaps/internal/keystrokes/model"
	"GeneratePasswordAndOverlaps/internal/keystrokes/service"
	"context"
	"time"
)

type Implementation struct {
	keystrokeService service.KeystrokeService
}

func NewImplementation(keystrokeService service.KeystrokeService) *Implementation {
	return &Implementation{
		keystrokeService: keystrokeService,
	}
}
func (i *Implementation) CountOverlaps(ctx context.Context, keyNames []string,
	keyEvents []string, keyTimes []time.Time) (int, int, int, error) {
	stroke := converter.ToKeysFromKeyListener(keyNames, keyEvents, keyTimes)
	zxc := i.keystrokeService.CreateKeystrokes(ctx, stroke)
	first, second, third, err := i.keystrokeService.CountOverlaps(ctx, &zxc)
	if err != nil {
		return -1, -1, -1, err
	}
	return first, second, third, nil
}

func (i *Implementation) CreateKeystrokes(ctx context.Context, keyNames []string,
	keyEvents []string, keyTimes []time.Time) model.Keystroke {
	keys := []model.Key{}
	for i := 0; i < len(keyNames); i++ {
		temp := converter.ToKeyFromKeyListener(keyNames[i], keyEvents[i], keyTimes[i])
		keys = append(keys, temp)
	}
	return i.keystrokeService.CreateKeystrokes(ctx, keys)
}
