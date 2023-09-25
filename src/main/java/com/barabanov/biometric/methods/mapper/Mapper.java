package com.barabanov.biometric.methods.mapper;

public interface Mapper<F, T>
{
    T mapFrom(F object);
}

