package service

import (
	"GeneratePasswordAndOverlaps/internal/keylistener/service/windows"
	"runtime"
)
import "GeneratePasswordAndOverlaps/internal/keylistener/service/unix"

func CreateSpecificKeyListener() KeyListener {
	if runtime.GOOS == "windows" {
		return windows.NewWindowsKeyboardListener()
	} else if runtime.GOOS == "linux" {
		return unix.NewUnixKeyboardListener()
	} else {
		return nil
	}
}
