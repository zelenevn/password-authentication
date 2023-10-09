package application

import (
	generatorApi "GeneratePasswordAndOverlaps/internal/generator/api"
	passrepo "GeneratePasswordAndOverlaps/internal/generator/repository"
	generatorrepo "GeneratePasswordAndOverlaps/internal/generator/repository/generator"
	generatorService "GeneratePasswordAndOverlaps/internal/generator/service"
	"GeneratePasswordAndOverlaps/internal/generator/service/generator"
	keylistenerApi "GeneratePasswordAndOverlaps/internal/keylistener/api"
	keylistenerService "GeneratePasswordAndOverlaps/internal/keylistener/service"
	keystrokesApi "GeneratePasswordAndOverlaps/internal/keystrokes/api"
	keyrepo "GeneratePasswordAndOverlaps/internal/keystrokes/repository"
	"GeneratePasswordAndOverlaps/internal/keystrokes/repository/keystrokes"
	keystrokesService "GeneratePasswordAndOverlaps/internal/keystrokes/service"
	keystrokes2 "GeneratePasswordAndOverlaps/internal/keystrokes/service/keystrokes"
)

var T interface{}

type ServiceProvider struct {
	passwordService     generatorService.GeneratorService
	keystrokeService    keystrokesService.KeystrokeService
	keylistenerService  keylistenerService.KeyListener
	passwordRepository  passrepo.IGeneratorRepository
	keystrokeRepository keyrepo.IKeystrokeRepository
	passwordImpl        generatorApi.Implementation
	keystrokeImpl       keystrokesApi.Implementation
	keylistenerImpl     keylistenerApi.Implementation
}

func NewServiceProvider() *ServiceProvider {
	pRepo := generatorrepo.NewRepository()
	kRepo := keystrokes.NewRepository()
	pService := generator.NewService(pRepo)
	kService := keystrokes2.NewService(kRepo)
	lService := keylistenerService.CreateSpecificKeyListener()
	pImpl := generatorApi.NewImplementation(pService)
	kImpl := keystrokesApi.NewImplementation(kService)
	lImpl := keylistenerApi.NewImplementation(lService)
	return &ServiceProvider{
		passwordService:     pService,
		keystrokeService:    kService,
		keylistenerService:  lService,
		passwordRepository:  pRepo,
		keystrokeRepository: kRepo,
		passwordImpl:        *pImpl,
		keystrokeImpl:       *kImpl,
		keylistenerImpl:     *lImpl,
	}
}
func (s *ServiceProvider) PasswordRepository() passrepo.IGeneratorRepository {
	if s.passwordRepository == nil {
		s.passwordRepository = generatorrepo.NewRepository()
	}
	return s.passwordRepository
}
func (s *ServiceProvider) KeyStrokeRepository() keyrepo.IKeystrokeRepository {
	if s.keystrokeRepository == nil {
		s.keystrokeRepository = keystrokes.NewRepository()
	}
	return s.keystrokeRepository

}

func (s *ServiceProvider) PasswordService() generatorService.GeneratorService {
	if s.passwordService == nil {
		s.passwordService = generator.NewService(
			s.passwordRepository)
	}
	return s.passwordService
}

func (s *ServiceProvider) KeyStrokeService() keystrokesService.KeystrokeService {
	if s.keystrokeService == nil {
		s.keystrokeService = keystrokes2.NewService(
			s.keystrokeRepository)
	}
	return s.keystrokeService
}
func (s *ServiceProvider) KeylistenerService() keylistenerService.KeyListener {
	if s.keylistenerService == nil {
		s.keylistenerService = keylistenerService.CreateSpecificKeyListener()
	}
	return s.keylistenerService
}
func (s *ServiceProvider) PasswordImpl() generatorApi.Implementation {
	if s.passwordImpl == T {
		s.passwordImpl = *generatorApi.NewImplementation(s.PasswordService())
	}
	return s.passwordImpl
}
func (s *ServiceProvider) KeystrokeImpl() keystrokesApi.Implementation {
	if s.keystrokeImpl == T {
		s.keystrokeImpl = *keystrokesApi.NewImplementation(s.KeyStrokeService())
	}
	return s.keystrokeImpl
}

func (s *ServiceProvider) KeylistenerImpl() keylistenerApi.Implementation {
	if s.keylistenerImpl == T {
		s.keylistenerImpl = *keylistenerApi.NewImplementation(s.keylistenerService)
	}
	return s.keylistenerImpl
}
