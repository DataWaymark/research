library(quantmod)

getSymbols("^GSPC")
getSymbols("^GDAXI")

plot(GSPC$GSPC.Adjusted)
plot(ROC(GSPC$GSPC.Adjusted))
plot(GDAXI$GDAXI.Adjusted)
plot(ROC(GDAXI$GDAXI.Adjusted))
