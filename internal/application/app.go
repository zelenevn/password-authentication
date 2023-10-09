package application

import (
	"context"
)

type App struct {
	serviceProvider *ServiceProvider
}

func (a App) init(ctx context.Context) error {
	inits := []func(ctx2 context.Context) error{
		a.initConfig,
		a.initServiceProvider,
	}

	for _, f := range inits {
		if err := f(ctx); err != nil {
			return err
		}
	}
	return nil
}

func (a App) initConfig(ctx context.Context) error {
	return nil
}

func (a App) initServiceProvider(ctx context.Context) error {
	a.serviceProvider = NewServiceProvider()
	return nil
}

func NewApp(ctx context.Context) (*App, error) {
	a := &App{}
	err := a.init(ctx)
	if err != nil {
		return nil, err
	}
	return a, nil
}
