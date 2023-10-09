// config.go
package config

import (
	"github.com/spf13/viper"
	"log"
)

// Configuration структура для хранения настроек приложения
type Configuration struct {
	UI              string `mapstructure:"ui"`
	App             AppConfiguration
	Log             LogConfiguration
	Database        DatabaseConfiguration
	PasswordLangs   map[string]PasswordLangConfiguration    `mapstructure:"password_languages"`
	PasswordOptions map[string]PasswordOptionsConfiguration `mapstructure:"password_options"`
}

// AppConfiguration структура для хранения настроек приложения
type AppConfiguration struct {
	Name    string
	Version string
}

// LogConfiguration структура для хранения настроек логирования
type LogConfiguration struct {
	Level string
}

// DatabaseConfiguration структура для хранения настроек базы данных
type DatabaseConfiguration struct {
	Host     string
	Port     int
	User     string
	Password string
	DBName   string
}

// PasswordLangConfiguration структура для хранения настроек языков пароля
type PasswordLangConfiguration struct {
	Name       string
	Characters string
}

type PasswordOptionsConfiguration struct {
	Name       string
	Characters string
}

// LoadConfig функция для загрузки настроек из config.yaml
func LoadConfig() (*Configuration, error) {
	viper.SetConfigName("config")
	viper.SetConfigType("yaml")
	viper.AddConfigPath("/home/kikiki/GolandProjects/Biometria/GeneratePasswordAndOverlaps")

	if err := viper.ReadInConfig(); err != nil {
		log.Fatalf("Failed to read config file: %v", err)
		return nil, err
	}

	var config Configuration
	if err := viper.Unmarshal(&config); err != nil {
		log.Fatalf("Failed to unmarshal config: %v", err)
		return nil, err
	}

	return &config, nil
}
