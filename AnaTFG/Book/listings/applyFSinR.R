applyFSinR <- function(dsname, algorithm)
{
  library(FSinR)
  source("./loadDataset.R")
  
  data <- loadDataset(dsname)
  evaluator <- filterEvaluator('determinationCoefficient')
  searcher <- searchAlgorithm(algorithm)
  results <- featureSelection(data, "bug", searcher, evaluator)
  
  return(results$bestFeatures)
}