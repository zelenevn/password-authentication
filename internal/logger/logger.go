package logger

import (
	"GeneratePasswordAndOverlaps/internal/config"
	"log"
	"os"
)

// Logger структура для логирования событий приложения
type Logger struct {
	logger *log.Logger
}

// NewLogger функция для создания нового экземпляра логгера
func NewLogger() *Logger {
	logger := log.New(os.Stdout, "", log.Ldate|log.Ltime|log.Lshortfile)
	return &Logger{
		logger: logger,
	}
}

// LogInfo метод для логирования информационных сообщений
func (l *Logger) LogInfo(message string) {
	l.logger.Printf("[INFO] %s\n", message)
}

// LogError метод для логирования сообщений об ошибках
func (l *Logger) LogError(message string) {
	l.logger.Printf("[ERROR] %s\n", message)
}

// LogDebug метод для логирования отладочной информации
func (l *Logger) LogDebug(message string) {
	l.logger.Printf("[DEBUG] %s\n", message)
}

// InitLogging функция для инициализации логгера на основе конфигурации
func InitLogging(cfg *config.LogConfiguration) *Logger {
	logger := NewLogger()

	switch cfg.Level {
	case "info":
		// Логгировать только информационные сообщения
	case "error":
		// Логгировать только сообщения об ошибках
	case "debug":
		// Логгировать отладочную информацию
	default:
		// По умолчанию, логгировать только информационные сообщения
	}

	return logger
}
