library(tidyverse)
library(gridExtra)

data = read.csv(file.choose())

data
p1 = data %>%
  ggplot(aes(x=tick,y=population)) +
  geom_line() +
  theme_minimal()


p2 =data %>%
  ggplot(aes(x=tick,y=average_speed)) +
  geom_line() +
  theme_minimal()


grid.arrange(p1, p2, ncol = 1)
