package main

import (
	"GeneratePasswordAndOverlaps/internal/application"
	"GeneratePasswordAndOverlaps/internal/config"
	"context"
	"fmt"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
	"log"
)

func main() {
	conf, err := config.LoadConfig()
	if err != nil {
		panic(err)
	}
	provider := application.NewServiceProvider()
	langs := make([]string, 0)
	for k, _ := range conf.PasswordLangs {
		langs = append(langs, k)
	}
	options := make([]string, 0)
	for k, _ := range conf.PasswordOptions {
		options = append(options, k)
	}
	myApp := app.New()
	myWindow := myApp.NewWindow("Password Generator")

	passwordLabel := widget.NewLabel("Generated Password Will Appear Here")

	// Создаем элементы интерфейса
	lengthEntry := widget.NewEntry()
	langsCheck := widget.NewRadioGroup(langs, func(keys string) {
		fmt.Println(keys)
	})
	optionsCheck := widget.NewCheckGroup(options, func(keys []string) {
		for _, key := range keys {
			fmt.Println(key)
		}
	})
	generateButton := widget.NewButton("Generate Password", func() {
		fmt.Println(optionsCheck.Options)
		fmt.Println(optionsCheck.Selected)
		opt := make(map[string]string)
		for k, v := range optionsCheck.Selected {
			opt[v] = conf.PasswordOptions[v].Characters
			fmt.Println("add to map", optionsCheck.Selected[k], v)
		}
		opt[langsCheck.Selected] = conf.PasswordLangs[langsCheck.Selected].Characters
		fmt.Println("add to map", langsCheck.Selected)
		impl := provider.PasswordImpl()
		password, passwordError := impl.CreatePassword(context.TODO(), lengthEntry.Text, langsCheck.Selected,
			opt)
		if passwordError != nil {
			log.Fatal(err, "Failed to generate password")
		}
		//TODO ADD LOGGER FOR ERRORS
		passwordLabel.SetText(password)
	})

	// Создаем макет интерфейса
	content := container.NewVBox(
		widget.NewLabel("Password Generator"),
		container.NewVBox(
			widget.NewLabel("Length:"),
			lengthEntry,
			widget.NewLabel("Language: "),
			langsCheck,
			widget.NewLabel("Options: "),
			optionsCheck,
		),
		generateButton,
		passwordLabel,
	)

	// Устанавливаем макет в окно
	myWindow.SetContent(content)

	// Запускаем приложение
	myWindow.ShowAndRun()
}

// GeneratePassword - функция для генерации пароля
func GeneratePassword(length string) string {
	// Здесь вы можете реализовать генерацию пароля
	// на основе введенной длины и других параметров
	// В этом примере просто возвращаем фиксированный пароль
	return "GeneratedPassword123"
}
