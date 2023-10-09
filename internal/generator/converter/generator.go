package converter

import (
	zxc "GeneratePasswordAndOverlaps/internal/generator/model"
	"log"
	"strconv"
	"strings"
)

//todo add converters from json/protobuff/ to model

func ToPasswordGeneratorFromUserInput(length string, language string, options map[string]string) zxc.Generator {
	tempArr := make([]zxc.Option, 0)
	_, ok := options["uppercase"]
	if ok {
		options["uppercase"] = strings.ToUpper(options[language])
	}
	for k, v := range options {
		if v == "" {
			continue
		}
		tempArr = append(tempArr, zxc.Option{
			Name:       k,
			Characters: v,
		})
	}
	tempLength, err := strconv.Atoi(length)
	if err != nil {
		log.Panic(err)
	}
	return zxc.Generator{
		PasswordLength: tempLength,
		Language:       language,
		Options:        tempArr,
	}
}
