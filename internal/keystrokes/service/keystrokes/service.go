package keystrokes

import (
	"GeneratePasswordAndOverlaps/internal/keystrokes/model"
	keyrepo "GeneratePasswordAndOverlaps/internal/keystrokes/repository"
	"context"
)

type service struct {
	keyStrokeRepo keyrepo.IKeystrokeRepository
}

func NewService(keyStrokeRepo keyrepo.IKeystrokeRepository) *service {
	return &service{
		keyStrokeRepo: keyStrokeRepo,
	}
}

func (s service) CountOverlaps(ctx context.Context, ks *model.Keystroke) (int, int, int, error) {
	overlayCount := map[model.Type]int{
		model.First:  0,
		model.Second: 0,
		model.Third:  0,
	}

	var activeKeys = make(map[string]model.Key)

	for _, key := range ks.Keys {
		switch key.Event {
		case model.Pressed:
			activeKeys[key.Name] = key
		case model.Released:
			if activeKey, ok := activeKeys[key.Name]; ok {
				delete(activeKeys, key.Name)

				switch activeKey.Name {
				case "FirstKey":
					switch key.Name {
					case "SecondKey":
						overlayCount[model.First]++
					}
				case "SecondKey":
					switch key.Name {
					case "FirstKey":
						overlayCount[model.Second]++
					}
				}
			}
		}
	}

	return overlayCount[model.First], overlayCount[model.Second], overlayCount[model.Third], nil
}

func (s service) CreateOverlaps(ctx context.Context, first model.Key, second model.Key) (model.Overlay, error) {
	panic("implement me")
}

func (s service) CreateKeystrokes(ctx context.Context, keys []model.Key) model.Keystroke {
	pressed := make([]model.Key, 0)
	released := make([]model.Key, 0)
	for _, v := range keys {
		if v.Event == model.Pressed {
			pressed = append(pressed, v)
		}
		if v.Event == model.Released {
			released = append(released, v)
		}
	}
	return model.Keystroke{
		Keys:     keys,
		Pressed:  pressed,
		Released: released,
	}
}
