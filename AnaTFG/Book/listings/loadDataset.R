dsnames <- c("xalan-2.7", "xalan-2.5", "jedit-4.3", "pbeans1", "ckjm", "forrest-0.6")

loadDataset <- function(name)
{
  library(DefectData)
  return(loadData(name)$data)
}