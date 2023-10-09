package service

import "GeneratePasswordAndOverlaps/internal/keylistener/model"

type KeyListener interface {
	StartListening() error
	StopListening() error
	Events() <-chan model.KeyEvent
}
