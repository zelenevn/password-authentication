package model

import "time"

type Keystrokes struct {
	Keys     []Key
	Pressed  []Key
	Released []Key
}

type Overlay struct {
	FirstKey  Key
	SecondKey Key
	Type      Type
}

type Type int

const (
	First  Type = iota
	Second      = iota
	Third       = iota
)

type Key struct {
	Name      string
	Event     Event
	EventTime time.Time
}

type Event int

const (
	Pressed Event = iota
	Released
)
