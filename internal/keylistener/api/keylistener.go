package api

import (
	"GeneratePasswordAndOverlaps/internal/keylistener/service"
	"context"
)

type Implementation struct {
	keyListener service.KeyListener
}

func NewImplementation(keylistenerService service.KeyListener) *Implementation {
	return &Implementation{
		keyListener: keylistenerService,
	}
}

func (i *Implementation) StartListening(ctx context.Context) error {
	return i.keyListener.StartListening()
}

func (i *Implementation) StopListening(ctx context.Context) error {
	return i.keyListener.StopListening()
}

func (i *Implementation) Events(ctx context.Context) (keyNames []string, eventName []string,
	eventTimes []string, err error) {
	events := i.keyListener.Events()
	keyNames = make([]string, 0)
	eventName = make([]string, 0)
	eventTimes = make([]string, 0)
	for v := range events {
		keyNames = append(keyNames, v.Key)
		eventName = append(eventName, v.EventType.String())
		eventTimes = append(eventTimes, v.Time.String())
	}
	return keyNames, eventName, eventTimes, err
}
