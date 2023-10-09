package unix

import "GeneratePasswordAndOverlaps/internal/keylistener/model"

// todo implementlater
type UnixKeyboardListener struct {
	events chan model.KeyEvent
}

func NewUnixKeyboardListener() *UnixKeyboardListener {
	return &UnixKeyboardListener{
		events: make(chan model.KeyEvent),
	}
}

func (u UnixKeyboardListener) StartListening() error {
	//TODO implement me
	panic("implement me")
}

func (u UnixKeyboardListener) StopListening() error {
	//TODO implement me
	panic("implement me")
}

func (u UnixKeyboardListener) Events() <-chan model.KeyEvent {
	return u.events
}
