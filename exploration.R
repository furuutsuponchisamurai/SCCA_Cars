library(dplyr)
library(ggplot2)
# Read in data
df <- read.csv('~/Projects/SCCA_Cars/_data/NationalsDrivers2019.tsv', sep='\t')


# How many double drivers?
ddrivers <- df %>% group_by(IsDoubleDriving, RaceClass) %>% tally()

ddrivers <- df %>% filter(IsDoubleDriving == TRUE) %>% group_by(doub)

# Where are drivers coming from?
df <- df %>% mutate(State = toupper(State))
d_location <- df %>% group_by(State) %>% tally()
d_div <- df %>% group_by(Division) %>% tally()
d_Reg <-  df %>% group_by(Region) %>% tally()

# Car
df <- df %>% mutate(Car = toupper(Car))
df_car <- df %>% group_by(Car) %>% tally()
df_car_trophy <- df %>% filter(WonTrophy == 1) %>% group_by(CarYear, Manufacturer,Car,Tire) %>% tally()

df_tire <- df %>% group_by(Tire) %>% summarise(Total = n(),
                                               Trophies = sum(WonTrophy))
