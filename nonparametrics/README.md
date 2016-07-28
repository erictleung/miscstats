# Non-parametrics

Similar to the one-sample t test is the Wilcoxon signed-rank test. However, the
Wilcoxon test is a non-parametric test. The test checks if the distribution of
the data is symmetric around some median value.

Example:

```R
> wilcox.test(rnorm(10, mean = 0, sd = 1), mu = 5)

        Wilcoxon signed rank test

data:  rnorm(10, mean = 0, sd = 1)
V = 0, p-value = 0.001953
alternative hypothesis: true location is not equal to 5
```
