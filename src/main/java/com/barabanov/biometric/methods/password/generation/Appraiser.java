package com.barabanov.biometric.methods.password.generation;

import lombok.experimental.UtilityClass;


@UtilityClass
public class Appraiser
{
    // pswdExpirationDate - in millisecond
    // pswdSearchSpeed - millisecond per 1 password
    public double quantificationOfDurability(int alphabetSize, int pswdLen, long pswdExpirationDate, double pswdSearchSpeed)
    {
        long pswdCombinationNum = (long) Math.pow(alphabetSize, pswdLen);

        return pswdExpirationDate / (pswdSearchSpeed * pswdCombinationNum);
    }
}
