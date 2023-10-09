package main

/*import (
	gui "GeneratePasswordAndOverlaps/UI/GUI"
	"GeneratePasswordAndOverlaps/UI/TUI"
	"GeneratePasswordAndOverlaps/internal/config"
	"GeneratePasswordAndOverlaps/internal/logger"
	"GeneratePasswordAndOverlaps/internal/services/keystroke"
	"GeneratePasswordAndOverlaps/internal/services/password"
	"log"
)

func main() {
	// Загрузка конфигурации из файла config.yaml
	appConfig, err := config.LoadConfig()
	if err != nil {
		log.Fatalf("Failed to load config: %v", err)
	}

	// Инициализация логгера на основе конфигурации
	appLogger := logger.InitLogging(&appConfig.Log)

	// Инициализация службы генерации паролей
	passwordSvc := password.NewPasswordGenerator()

	// Инициализация службы считывания клавиш
	keystrokeSvc := keystroke.NewKeystrokeLogger()

	// Запуск интерфейса пользователя (TUI или GUI) в зависимости от настройки
	if appConfig.UI == "TUI" {
		tuiApp := tui.NewTUIApp(appConfig, passwordSvc, keystrokeSvc)
		tuiApp.Run()
	} else if appConfig.UI == "GUI" {
		guiApp := gui.NewGUIApp(appConfig, passwordSvc, keystrokeSvc)
		guiApp.Run()
	} else {
		appLogger.LogError("Invalid UI configuration")
		return
	}
}*/
