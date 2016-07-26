# Distributions

Common distribution types:

- Normal/Gaussian (`norm`)
- Binomial (`binom`)
- Poisson (`pois`)
- Uniform (`unif`)

Distribution functions:

- probability distribution functions (`p`)
- density functions (`d`)
- quantile functions (`q`)
- random number generator (`r`)

Example:

```R
> pnorm(q = 0)
[1] 0.5
> pnorm(q = 0.5)
[1] 0.6914625
> dnorm(0)
[1] 0.3969525
> qnorm(0.5)
[1] 0
> qnorm(0.95)
[1] 1.644854
> rnorm(2)
[1] -1.2137979 -0.8883634
```
