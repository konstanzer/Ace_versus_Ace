from numpy import sqrt
import scipy.stats as stats


def z_test(ctr_old, ctr_new, nobs_old, nobs_new,
           effect_size=0, alpha=.05):
    """Perform z-test to compare that two proportions differ by at least a
    given effect size:
        H0: ctr_old + effect_size < ctr_new
        HA: ctr_old + effect_size >= ctr_new
    Parameters
    ----------
    ctr_old: float
      The click through rate in the pre-treatment sample.
    ctr_new: float
      The click through rate in the post-treatment sample.
    nobs_old: int
      The number of observations in the pre-treatment sample.
    nobs_new: int
      The number of observations in the post-treatment sample.
    effect_size: float
      The size of the difference between pre-treatment CTR and post-treatment
      CTR to test for.
    alpha: float (between zero and one)
      The p-value threshold to use for rejection of the null hypothesis.
    Returns
    -------
    z_score: float
      The computed z-score for the test of proportions.
    p_value: float
      The computed p-value for the test of proportions,
    reject: bool
      Is the null hypothesis rejected at the given threshold.
    """
    conversion = (
        (ctr_old * nobs_old + ctr_new * nobs_new) /
        (nobs_old + nobs_new))
    se = sqrt(conversion * (1 - conversion) * (1 / nobs_old + 1 / nobs_new))
    z_score = (ctr_new - ctr_old - effect_size) / se
    p_val = 1 - stats.norm.cdf(z_score)
    reject_null = p_val < alpha
    return z_score, p_val, reject_null

if __name__ == '__main__':
    # Testing the z-test on a known example
    old_p = 100.0 / 1000
    new_p = 150.0 / 1000
    old_row = 1000.0
    new_row = 1000.0
    # p-value should be << 1
    print(z_test(old_p, new_p, old_row, new_row))
    # p-value should be 1 because z-score < 0
    print(z_test(new_p, old_p, old_row, new_row))
    # p-value should be 0.5 because the null is exactly true.
    print(z_test(old_p, new_p, old_row, new_row, effect_size=0.05))
