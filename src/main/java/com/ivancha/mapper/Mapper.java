package com.ivancha.mapper;

public interface Mapper <F, T> {

    T map(F object);
}
