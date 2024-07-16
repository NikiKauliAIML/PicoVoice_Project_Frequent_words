# Calculate rain probability in given calender Day

"""
Problem Statement:
        The probability of rain on a given calendar day in Vancouver is p[i], where i is the day's index. 
        For example, p[0] is the probability of rain on January 1st, and p[10] is the probability of precipitation on January 11th.
        Assume the year has 365 days (i.e., p has 365 elements). What is the chance it rains more than n (e.g., 100) days in Vancouver?
        Write a function that accepts p (probabilities of rain on a given calendar day) and n as input arguments and returns the
        possibility of raining at least n days.

Overview:

        - p[i] : Probability of rain on given calender day in vancouver
        - P : P is list or sequence of shape and 365 parameter in it,  
        - n : number of days or thresould
        
        Calcualte rain probabilities more than n days in Vancouver.
        Design a function which argument probabilities of rain P and n, function return possibility of raining at least n days.       

Args: 
        -   P : List or sequence of shape (P[]) containing the pobabilities of rain on given calender day

        -   n : Int of shape containing possibilitity of raining at least n days 
        
"""


import streamlit as st
import numpy as np
from typing import Sequence
from scipy.stats import binom

def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:
  
  # Calculate total rain probability in given days
  total_rainprob = sum(p)/len(p)  

  # Calculate the probability of rain on n or fewer days
  less_than_n_days = binom.cdf(n, len(p), total_rainprob)

  # Calculate the probability of rain on more than n days
  morethan_n = 1 - less_than_n_days
  return morethan_n

def main():
  st.title("Rain Probability Calculator")

  # Input for daily rain probabilities
  p_input = st.text_input("Enter daily rain probabilities (comma-separated):")
  if p_input:
    try:
      p = np.array([float(prob) for prob in p_input.split(',')])
    except ValueError:
      st.error("Invalid input. Please enter numbers separated by commas.")
      p = None

  # Input for minimum number of rainy days
  n = st.number_input("Minimum number of rainy days:", min_value=0, max_value=365, value=0)

  if st.button("Run"):
    result = prob_rain_more_than_n(p, n)
    st.success(f"The probability of rain on more than {n} days is: {result:.4f}")

if __name__ == "__main__":
  main()
