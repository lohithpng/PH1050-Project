import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv("ElementData.csv")
noble = df[df['Symbol'].isin(["He", "Ne", "Ar", "Kr", "Xe"])]
noble=noble.set_index('Symbol')
ratio=noble['MeltingPoint']/noble['BoilingPoint']
#Helium does not have a melting point at 1 atm, so it is NaN.
print(ratio,np.mean(ratio),np.std(ratio,ddof=1)) #we can see the ratios
ratio=ratio.dropna() #drop helium
n=len(ratio)
mean = np.mean(ratio)
sd = np.std(ratio, ddof=1)
t = stats.t.ppf(0.975, 3) #t value for 95% confidence interval with n-1=3 degrees of freedom
half1 = t * sd / np.sqrt(n) #half-width of the confidence interval
ci = (mean - half1, mean + half1) #confidence interval for the mean
ratio2= ratio.drop("Ne")
mean2 = np.mean(ratio2)
sd2 = np.std(ratio2, ddof=1)
t2 = stats.t.ppf(0.975, 2) #t value for 95% prediction interval with n-1=2 degrees of freedom
half2 = t2 * s2 * np.sqrt(1 + 1/len(ratio2)) #Prediction interval formula. It accounts for the uncertainty in the mean AND the variability of individual observations.
pi = (mean2 - half2, mean2 + half2)
ne = ratio["Ne"]
if ne < low or ne > high:
        print("Ne =", round(ne, 4), "-> OUTSIDE the interval, so Ne is an outlier")
else:
        print("Ne =", round(ne, 4), "-> INSIDE the interval, so no evidence Ne is an outlier")

        plt.figure(figsize=(5, 4))
plt.axhspan(mean - sd, mean + sd, color="grey", alpha=0.2, label="mean ± 1 SD")
plt.axhline(mean, color="grey", linestyle="--")
plt.scatter(ratios.index, ratios.values, color="blue", zorder=3)
plt.ylabel("T_melt / T_boil")
plt.xlabel("Noble gas")
plt.title("Noble-gas melting/boiling ratio")
plt.legend()
plt.tight_layout()
plt.savefig("noble_gas_ratio.png", dpi=200)
print("95% CI for mean:", ci) 
 print("Prediction interval from Ar, Kr, Xe:", pi)
