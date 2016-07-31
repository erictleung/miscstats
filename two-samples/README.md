# Two-sample tests

Similar to the t-test, a two sample t-test will test the differences between
two datasets.

Example:

```R
> summary(discoveries)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    0.0     2.0     3.0     3.1     4.0    12.0 
> summary(eurodist)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    158     808    1312    1505    2064    4532 
> t.test(discoveries, eurodist)

        Welch Two Sample t-test

data:  discoveries and eurodist
t = -24.218, df = 209.01, p-value < 2.2e-16
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -1624.317 -1379.778
sample estimates:
mean of x mean of y
    3.100  1505.148
```

The above is assuming each dataset has different variances.

To assume the same variances and to perform a "normal" t-test, you need to
specify this.

```R
> t.test(discoveries, eurodist, var.equal = TRUE)

        Two Sample t-test

data:  discoveries and eurodist
t = -16.698, df = 308, p-value < 2.2e-16
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -1679.052 -1325.044
sample estimates:
mean of x mean of y
    3.100  1505.148
```
