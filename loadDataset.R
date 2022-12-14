#dsnames <- c("xalan-2.7", "jedit-4.3", "ckjm", "xalan-2.5", "forrest-0.6", "pbeans1")

dsnames <- c("ant-1.3", "ckjm")

#dfl <- listData[listData$corpus == "ck",]["system"]
#str(dfl)
#class(dfl)
#dim(dfl)
#attributes(dfl)
#row.names(dfl)
#levels(dfl$system)
#names(dfl)
#dfl$system[1]
#dsnames <- as.character(dfl$system)
#dsnames


loadDataset <- function(name)
{
  library(DefectData)
  return(loadData(name)$data)
}

