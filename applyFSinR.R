library(FSinR)

applyFSinR <- function(dsname, algorithm)
{
  #library(FSinR)
  #source("./loadDataset.R")
  
  data <- loadDataset(dsname)
  evaluator <- filterEvaluator('determinationCoefficient')
  searcher <- searchAlgorithm(algorithm)
  results <- featureSelection(data, "bug", searcher, evaluator)
  
  return(results$bestFeatures)
}


applyFSinR_FS <- function(dsname, searcher, evaluator)
{
  #library(FSinR)
  #source("./loadDataset.R")
  
  data <- loadDataset(dsname)
  evaluator <- filterEvaluator(evaluator)
  searcher <- searchAlgorithm(searcher)
  results <- featureSelection(data, "bug", searcher, evaluator)
  
  return(results$bestFeatures)
}