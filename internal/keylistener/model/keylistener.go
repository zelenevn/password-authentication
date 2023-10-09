package model

import "time"

type KeyEvent struct {
	Key       string
	EventType Event
	Time      time.Time
}

type Event int

const (
	Pressed Event = iota
	Released
)

func (e Event) String() string {
	return [...]string{"Pressed", "Released"}[e]
}
