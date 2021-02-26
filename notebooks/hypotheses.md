### First Hypothesis

   Scientific Question
    
    Are the the mean fastball spin rate between deGrom and Cole the same?


   Null Hypothesis
    
    The mean fastball spin rate between deGrom and Cole are the same.


   Alternative Hypothesis
    
    The mean fastball spin rate between deGrom and Cole are not the same.


   Type of Test and Test Statistic
    
        I would like to use a Welch's t-test. In order to perform a Welch's t-test I will need the mean and standard deviation of my two populations. Or just use scipy's function ttest_ind 


   What is the distribution under the null hypothesis?
    
    The distribution of the null hypothesis represents the difference between the mean of the two distributions. So, if we are comparing the spin rates for fastballs, it is the distribution of the difference of samples means where the assumption is that the mean of this distribution is zero.:
    𝜇FFdeGrom - 𝜇FFCole = 0


   Significance level
    
    I will select a standard significance level of 0.05. I will also use a bonferonni correction to account for the fact that I will be comparing multiple means.


   p-value

    Cole mean: 2505
    deGrom mean: 2477
    t-stat: 3.899
    p-value: 0.0001

   Conclusion

    Ok, now that we have a p-value we need to compare it to our significance level. Since I am performing multiple hypothesis test, I will include a Bonferroni correction. There for my signficance for each individual test will be 𝛼=0.05/3
    
    0.01666

All p-values are less than my significance level. There for my conclusion is:

    I reject the null hypothesis that the means are the same.

