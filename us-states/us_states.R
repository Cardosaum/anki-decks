library(tidyverse)
library(magrittr)
library(stringi)
library(glue)

us_names <- c("name", "location", "abbreviation", "largest_city", "capital", "bordering", "flag", "state_nickname", "blankmap", "nickname_reverse", "nothing")
us <- read_tsv("us.txt", col_names = us_names)
us %<>% select(-nothing)

svgf <- read_lines("us_states_al.svg")

us_svgs <- vector()
for (f in seq_along(us$abbreviation)) {
    i <- us$abbreviation[f]
    state_color <- paste(c("#", i, " {fill:#bd93f9}"), collapse = "")
    svgf[12] <- state_color
    us_svgs[f] <- paste0("us_state_", i, ".svg", collapse = "")
    file_name <- us_svgs[f]
    write_lines(svgf, file_name)
}

us %<>%
    mutate(state_svg = us_svgs) %>%
    glimpse()

us %>%
    select(-blankmap) %>%
    rename(blankmap = state_svg)

us$location
