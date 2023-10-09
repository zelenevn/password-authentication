package converter

import (
	"GeneratePasswordAndOverlaps/internal/keystrokes/model"
	"time"
)

func ToKeyFromKeyListener(name string, eventName string, time time.Time) model.Key {
	return model.Key{
		Name:      name,
		Event:     ToEventFromString(eventName),
		EventTime: time,
	}
}
func ToKeysFromKeyListener(names []string, eventNames []string, times []time.Time) []model.Key {
	keys := make([]model.Key, 0)
	for i := 0; i < len(names); i++ {
		temp := ToKeyFromKeyListener(names[i], eventNames[i], times[i])
		keys = append(keys, temp)
	}
	return keys
}

func ToEventFromString(name string) model.Event {
	if name == "Pressed" {
		return model.Pressed
	}
	if name == "Released" {
		return model.Released
	}
	return model.Event(0)
}
