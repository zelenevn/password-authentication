package com.ivancha.dto;

public record UserReadDto(Integer id,
                          String nickname,
                          PasswordReadDto passwordReadDto)
{ }
