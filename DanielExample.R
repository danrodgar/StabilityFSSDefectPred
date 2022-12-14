
# EXAMPLES to add to the DASE project
# m1 <- matrix(C<-(1:10),nrow=5, ncol=6)
# m1

# df1 <- data.frame(v1 = c(1,3,5), v2 = c(4,6,7), c = c(TRUE,FALSE,TRUE))
# df2 <- data.frame(v1 = c(8,9,5), v2 = c(2,2,2), c = c(TRUE,FALSE,TRUE))
# df3 <- data.frame(v1 = c(1,1,9), v2 = c(1,6,8), c = c(TRUE,FALSE,FALSE))

# Add the elements of the dataframe to the list (not what I want)
# NOTE: It is NOT a list of dataframes 
# dfl <- list()  
# dfl <- append(df1, dfl)
# dfl <- append(df2, dfl)

# To have a list with 3 dataframes
# dfl <- list()
# dfl <- list("df1" = df1, "df2" = df2)
# dfltmp <- list("df3" = df3)
# dfl <- append(dfl, dfltmp)

###############################################################################
###############################################################################

library(DefectData)
listData
attributes(listData)
names(listData)

loadData("ckjm")
# dsl <- loadData("equinox")
# df <- dsl$data

#df[df$g == 'b',]
#Or the tidyverse answer
#library(dplyr)
#df %>%
#  filter(g == 'b') %>%
#  select(b)
#DSsNames <- listData %>%
#  filter(corpus == 'ck') %>%
#  select(system)
#typeof(DSsNames)


dfl <- listData[listData$corpus == "ambros",]["system"]
listData[listData$corpus == "ck",][3]
`#str(dfl)
#class(dfl)
#dim(dfl)
#attributes(dfl)
#row.names(dfl)
#levels(dfl$system)
#names(dfl)
#dfl$system[1]
ds_names <- as.character(dfl$system)
ds_names
# typeof(ds_names)



i=1
dfl <- list()  
for(i in 1:length(ds_names)) { 
  # print(ds_names[i])
  df_tmp <- loadData(ds_names[i])
  dfl_tmp <- list(df_tmp)
  names(dfl_tmp) <- ds_names[i] # Add the DS name 
  dfl <- append(dfl, dfl_tmp)
}

# It is possible to name all elements at once
# names(dfl) <- ds_names


library(FSinR)

##########################################################

evaluator <- wrapperEvaluator("knn")
searcher <- searchAlgorithm('sequentialForwardSelection')
d <-dfl[[1]]$data
d$bugs <- as.factor(d$bugs)
results <- featureSelection(d, 'bugs', searcher, evaluator)
#results <- featureSelection(iris, 'Species', searcher, evaluator)
results$bestFeatures
results$bestValue

##########################################################

evaluator <- filterEvaluator('MDLC')
searcher <- searchAlgorithm('sequentialForwardSelection')
results <- featureSelection(dfl[[1]]$data, dfl[[1]]$dep, searcher, evaluator)
results$bestFeatures
results$bestValue    

############################################################


evaluator <- filterEvaluator('Chi-squared')
#searcher <- searchAlgorithm('sequentialForwardSelection')
#evaluator <- filterEvaluator('ReliefFeatureSetMeasure')
#evaluator <- filterEvaluator('determinationCoefficient')
searcher <- searchAlgorithm('hillClimbing')

#z <- dfl[[1]]$data    #$equinox
#resultsList <- list()
#results <- featureSelection(data$data, data$dep, searcher, evaluator)
results <- featureSelection(dfl[[1]]$data, dfl[[1]]$dep, searcher, evaluator)
bestF <- results$bestFeatures
bestF
# bestFeatures is a vector that can be stored with additional attributes
str(bestF)
class(bestF)
typeof(bestF)
attributes(bestF)
names(bestF)
dimnames(bestF)
dimnames(bestF)[2]
str(dimnames(bestF)[2])
bestF[[8]]

##############################################################################
hybridSearcher <- hybridSearchAlgorithm('LCC')
evaluator <- filterEvaluator('determinationCoefficient')
results <- hybridFeatureSelection(dfl[[1]]$data, dfl[[1]]$dep, hybridSearcher, evaluator, evaluator)
bestF <- results$bestFeatures
bestF

#################################################################

library(caret)
resamplingParams <- list(method = "cv", number = 3)
fittingParams <- list(preProc = c("center", "scale"), metric="Accuracy", tuneGrid = expand.grid(k = c(1:3)))

searcher <- searchAlgorithm('hillClimbing')
#wrapper <- wrapperEvaluator()
wrapperEvaluator <- wrapperEvaluator("mlp", resamplingParams, fittingParams)
results <- featureSelection(dfl[[1]]$data, dfl[[1]]$dep, searcher, wrapperEvaluator)
result$bestFeatures

#result.search.fs <- (dfl[[1]]$data, dfl[[1]]$dep, wrapperSearcher)


#############################################################

library(FSinR)

## Examples of a wrapper evaluator generation

wrapper_evaluator_1 <- wrapperEvaluator('knn')
wrapper_evaluator_2 <- wrapperEvaluator('mlp')
wrapper_evaluator_3 <- wrapperEvaluator('randomForest')


## Examples of a wrapper evaluator generation (with parameters)

# Values for the caret trainControl function (resampling parameters)
resamplingParams <- list(method = "repeatedcv", repeats = 3)
# Values for the caret train function (fitting parameters)
fittingParams <- list(preProc = c("center", "scale"), metric="Accuracy",
                      tuneGrid = expand.grid(k = c(1:3)))

wrapper_evaluator <- wrapperEvaluator('knn', resamplingParams, fittingParams)


## The direct application of this function is an advanced use that consists of using this 
# function directly to evaluate a set of features
## Classification problem

# Generates the wrapper evaluation function
# wrapper_evaluator <- wrapperEvaluator('knn')
# Evaluates features directly (parameters: dataset, target variable and features)
results <- wrapper_evaluator(iris,'Species',c('Sepal.Length','Sepal.Width','Petal.Length','Petal.Width'))
# devuelve distintos valores
results


#####################################################33

measures <- list(IEConsistency(), mutualInformation(), giniIndex())
for (measure in measures) {
  # result <- sequentialForwardSelection()(iris, 'Species', measure)
  result <- sequentialForwardSelection()(dfl[[1]]$data, dfl[[1]]$dep, measure)
  print(attr(measure,'name'))
  print(result$bestFeatures)
}

chiSquared_evaluator <- chiSquared()
chiSquared_evaluator(iris,'Species',c('Sepal.Length'))

chiSquared_evaluator <- chiSquared()
chiSquared_evaluator(dfl[[1]]$data,'bugs',c('linesAddedUntil.'))
chiSquared_evaluator(dfl[[1]]$data,'bugs',c('numberOfFixesUntil.'))


########################################################

measures <- list(IEConsistency(), mutualInformation())
algorithms <- list(sequentialForwardSelection(), LasVegas())
for (algorithm in algorithms) {
  for (measure in measures) {
    #result <- algorithm(iris, 'Species', measure)
    result <- algorithm(dfl[[1]]$data, 'bugs', measure)
    print(paste("Algorithm: ",attr(algorithm,'name')))
    print(paste("Evaluation measure: ", attr(measure,'name')))
    print(result$bestFeatures)
  }
}

########################################################

# NOT WORKING
resamplingParams <- list(method = "cv", number = 5)
fittingParams <- list(preProc = c("center", "scale"), metric = "Accuracy", tuneGrid = expand.grid(k = c(1:3)))

wra <- wrapperEvaluator("knn", resamplingParams, fittingParams)

measures <- list(IEConsistency(), mutualInformation(), wra)
measures


##########################################################

evaluator <- wrapperEvaluator("knn")
searcher <- searchAlgorithm('sequentialForwardSelection')
results <- featureSelection(iris, 'Species', searcher, evaluator)
results$bestFeatures
results$bestValue


