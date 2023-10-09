package model

import (
	"time"
)

type Keystroke struct {
	Keys     []Key
	Pressed  []Key
	Released []Key
}

type Key struct {
	Name      string
	Event     Event
	EventTime time.Time
}

type Overlay struct {
	FirstKey  Key
	SecondKey Key
	Type      Type
}

type Event int

const (
	Pressed Event = iota
	Released
)

type Type int

const (
	//K1 press,K2 press,K1 release,K2 release
	First Type = iota
	//K2 press,K1 press,K2 release,k1 release
	Second
	//K2 press,k1 press,K1 release,k2 release
	Third
)
