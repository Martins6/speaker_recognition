# Title: Cleaning noise from signal
# Author: Adriel Martins
# Date: 26/10/2020

library(tidyverse)

df_signal <-
  read.table(file = 'signal.dat') %>% 
  as_tibble() %>% 
  pivot_longer(cols = starts_with('V')) %>% 
  mutate(name = 1:n()) %>% 
  rename(index = name)

df_signal %>% 
  ggplot(aes(index, value)) +
  geom_path()

df_ecg <-
  read.table(file = 'ecg.dat') %>% 
  as_tibble() %>% 
  pivot_longer(cols = starts_with('V')) %>% 
  mutate(name = 1:n()) %>% 
  rename(index = name)

df_ecg %>% 
  ggplot(aes(index, value)) +
  geom_path()

###################### (ii) #######################
fs = 100
Ts = 1/fs
###################### (iii) #######################
omega_rad = fs * 2 * pi
###################### (iv) #######################
omega_N = omega_rad/2
omega_N
###################### (v) ... (ix) #######################
# DFT
df_signal %>% 
  mutate(W = Mod(fft(value))) %>% 
  ggplot(aes(index, W)) +
  geom_path() +
  labs(y = '| W |')

df_signal %>% 
  mutate(W = Mod(fft(value))) %>%
  mutate(W = if_else(W > 300 | W < 50, 0, W),
         value_hat = as.double(fft(W, inverse = T)/n())) %>% 
  ggplot(aes(index, W)) +
  geom_path()

df_signal %>% 
  mutate(W = Mod(fft(value))) %>%
  mutate(W = if_else(W > 300 | W < 50, 0, W),
         value_hat = as.double(fft(W, inverse = T)/n())) %>% 
  ggplot(aes(index, value_hat)) +
  geom_path()

df_signal %>% 
  mutate(W = Mod(fft(value))) %>%
  mutate(W = if_else(W > 300 | W < 50, 0, W),
         value_hat = as.double(fft(W, inverse = T)/n())) %>% 
  summarise(
    MSE = (value_hat - df_ecg$value)^2 %>% mean()
  )
