library(quantmod)

getSymbols("^GSPC")
getSymbols("^GDAXI")

sum(is.na(GSPC$GSPC.Adjusted))
sum(is.na(GDAXI$GDAXI.Adjusted))

summary(GSPC$GSPC.Adjusted)
summary(GDAXI$GDAXI.Adjusted)

rGSPC <- ROC(GSPC$GSPC.Adjusted)
rDAX <- ROC(GDAXI$GDAXI.Adjusted)

sum(is.na(rGSPC))
sum(is.na(rDAX))

summary(rGSPC)
summary(rDAX)

data <- merge(rGSPC, rDAX)
data <- na.approx(data)
data <- na.omit(data)
#data <- na.omit(data)

library(e1071)

print(sd(data$GSPC.Adjusted))
print(sd(data$GDAXI.Adjusted))

print(skewness(data$GSPC.Adjusted))
print(skewness(data$GDAXI.Adjusted))

print(kurtosis(data$GSPC.Adjusted))
print(kurtosis(data$GDAXI.Adjusted))

library(tseries)

jarque.bera.test(data$GSPC.Adjusted)
jarque.bera.test(data$GDAXI.Adjusted)

library(nortest)

ad.test(data$GSPC.Adjusted)
ad.test(data$GDAXI.Adjusted)

plot(data)
legend(1, 95, legend=c("S&P500", "DAX"),
       col=c("black", "red"), lty=1:2, cex=0.8)

summary(data)

input = data$GDAXI.Adjusted
h = hist(input, breaks=50) # or hist(x,plot=FALSE) to avoid the plot of the histogram
h$density = h$counts/sum(h$counts)*100
plot(h,freq=FALSE)
lines(density(na.omit(input)))

#симулация с 100 000 повторения - генериране 100 000 пъти различни "случаи"

fit_in = 0
len = dim(input)[1]
for(i in 1: (len-5)) {
  r = as.numeric(input[i]) + as.numeric(input[i+1]) + as.numeric(input[i+2]) + as.numeric(input[i + 3]) + as.numeric(input[i + 4])
  if (r < -0.04) {
    fit_in = fit_in + 1  
  }
}
print(fit_in/(len-5))


nIter = 1000000
fit_in = 0
ExpRet = mean(as.vector(input)[-1])
ExpVar = sqrt(var(as.vector(input)[-1]))

for(i in 1:nIter) {
  r = rnorm(5, mean=ExpRet, sd=ExpVar);
  if (sum(r) < -0.04) {
    fit_in = fit_in + 1  
  }
  
}
print(fit_in/nIter)
