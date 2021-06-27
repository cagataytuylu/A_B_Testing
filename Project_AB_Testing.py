import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Steps of AB Test
# 1. Establish Hypotheses
# 2. Assumption Check
# - 1. Normality Assumption
# - 2. Variance Homogeneity
# 3. Implementation of the Hypothesis
# - HO red if p-value < 0.05.
# - 1. Independent two-sample t-test if assumptions are met (parametric test)
# - 2. Mannwhitneyu test if assumptions are not met (non-parametric test)
# Note:
# - Number 2 directly if normality is not achieved. If variance homogeneity is not provided, an argument is entered for number 1.
# - It can be useful to perform outlier analysis and correction before normality analysis.

control_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Control Group")
test_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Test Group")

control_group.describe().T
control_group["Purchase"].mean()

test_group.describe().T
test_group["Purchase"].mean()

# from helpers.helpers import check_df
# check_df(control_group)
# check_df(test_group)
############################
# Task 1. Define the hypothesis of the A/B test.
############################


############################
# 1. Establishing the hypothesis
############################
# H0: M1 = M2 = (There is no significant difference in earnings between the maximum bidding bid type and the average bidding bid type?)
# H1: M1 != M2 = (there are ......?)


# Note: Our business is with the Purchase variable, because after 2 advertising alternatives, it will care about customer gain.


############################
# Task 2. Perform the hypothesis test. out whether the results are statistically significant. Comment if # is not.
############################

############################
#2. Assumption Check
############################

# Normality Assumption
# Variance Homogeneity

############################
# Normality Assumption
############################

# H0: Assumption of normal distribution is provided.
# H1:..not provided.

test_stat, pvalue = shapiro(control_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9773, p-value = 0.5891
# H0 CANNOT BE REJECTED since p > 0.05, normality assumption is provided


test_stat, pvalue = shapiro(test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9589, p-value = 0.1541
# H0 CANNOT BE REJECTED since p > 0.05, normality assumption is provided


############################
# Assumption of Variance Homogeneity
# ############################


# H0: Variances are Homogeneous
# H1: Variances Are Not Homogeneous


test_stat, pvalue = levene(control_group["Purchase"],
                           test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 2.6393, p-value = 0.1083
# H0 CANNOT BE REJECTED since p-value > 0.05, variances are homogeneous.



# when we look at the above outputs, normality assumption and variance homogeneity in both groups
# It is seen that the # assumption is met. In this case, since both assumptions are met,
# independent two-sample t-test (parametric test) should be applied.

############################
# Task 4. Based on your answer in Task 2, what is your advice to the customer?
############################
# H0: M1 = M2 = (There is no significant difference in earnings between the maximum bidding bid type and the average bidding bid type?)
# H1: M1 != M2 = (there are ......?)

############################
# Independent two-sample t-test (parametric test) as assumptions are provided
############################
test_stat, pvalue = ttest_ind(control_group["Purchase"],
                              test_group["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = -0.9416, p-value = 0.3493
# H0 CANNOT be REJECTED because p-value > 0.05.

