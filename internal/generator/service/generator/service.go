package generator

import (
	"GeneratePasswordAndOverlaps/internal/generator/model"
	passrepo "GeneratePasswordAndOverlaps/internal/generator/repository"
	"context"
	crypto "crypto/rand"
	"math/big"
	"strings"
)

type service struct {
	passwordRepository passrepo.IGeneratorRepository
}

func NewService(passwordRepo passrepo.IGeneratorRepository) *service {
	return &service{passwordRepository: passwordRepo}
}

func (s service) CreatePassword(ctx context.Context, pg model.Generator) (string, error) {
	alphabet := ""
	for _, v := range pg.Options {
		alphabet += v.Characters
	}
	chars := strings.Split(alphabet, "")
	maxR := big.NewInt(int64(len(chars)))
	pass := ""
	for i := 0; i < pg.PasswordLength; i++ {
		ind, err := crypto.Int(crypto.Reader, maxR)
		if err != nil {
			return "", err
		}
		pass += chars[ind.Int64()]
	}
	/*	err := s.passwordRepository.CreatePassword(ctx, pg)
		if err != nil {
			log.Printf("ошибка сохранения пароля: %v\n", err)
			return "", err
		}*/
	return pass, nil
}
