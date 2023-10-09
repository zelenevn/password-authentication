package windows

import (
	"GeneratePasswordAndOverlaps/internal/keylistener/model"
	"fmt"
	"github.com/moutend/go-hook/pkg/keyboard"
	"github.com/moutend/go-hook/pkg/types"
	"os"
	"os/signal"
	"time"
)

// service/windows_keyboard_listener.go
const (
	keyUp   = 0x0101
	keyDown = 0x0100
)

type WindowsKeyboardListener struct {
	events chan model.KeyEvent
}

func NewWindowsKeyboardListener() *WindowsKeyboardListener {
	return &WindowsKeyboardListener{
		events: make(chan model.KeyEvent),
	}
}

func (l *WindowsKeyboardListener) StartListening() error {
	keyboardChan := make(chan types.KeyboardEvent, 100)

	if err := keyboard.Install(nil, keyboardChan); err != nil {
		return err
	}

	defer func() {
		err := keyboard.Uninstall()
		if err != nil {
			panic(err)
		}
	}()

	signalChan := make(chan os.Signal, 1)
	signal.Notify(signalChan, os.Interrupt)

	fmt.Println("start capturing keyboard input")

	for {
		select {
		case <-time.After(5 * time.Minute):
			fmt.Println("Received timeout signal")
			return nil
		case <-signalChan:
			fmt.Println("Received shutdown signal")
			return nil
		case k := <-keyboardChan:
			zxc := -1
			if k.Message == keyUp {
				zxc = 0
			}
			if k.Message == keyDown {
				zxc = 1
			}
			l.events <- model.KeyEvent{
				Key:       k.VKCode.String(),
				EventType: model.Event(zxc),
				Time:      time.Now(),
			}
			fmt.Printf("Received %v %v\n", k.Message, k.VKCode)
			continue
		}
	}
	return nil
}

func (l *WindowsKeyboardListener) StopListening() error {
	close(l.events)
	return nil
}

func (l *WindowsKeyboardListener) Events() <-chan model.KeyEvent {
	return l.events
}
