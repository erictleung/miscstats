# One-sample *t* test

Assume normal distribution.

**Null hypothesis**: sample data has same mean as distribution
**Alt hypothesis**: sample data has different mean than distribution

Example:

```R
> t.test(rnorm(10, mean = 0, sd = 1), mu = 0)

        One Sample t-test

data:  rnorm(10, mean = 0, sd = 1)
t = -0.51016, df = 9, p-value = 0.6222
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 -0.8867880  0.5604176
sample estimates:
 mean of x
-0.1631852
```
