def calculate_advanced_battery_health(rebalance_overdue, deep_discharge, temperature_extremes, operating_hours, battery_age):
    # Scoring parameters
    score_per_day_rebalance_overdue = 2
    score_per_deep_discharge = 5
    score_per_temperature_extreme_hour = 3
    score_per_operating_hour = 1
    age_decay_factor = 0.1  # Additional score per year of age

    # Calculate scores for each factor
    rebalance_score = rebalance_overdue * score_per_day_rebalance_overdue
    deep_discharge_score = deep_discharge * score_per_deep_discharge
    temperature_score = temperature_extremes * score_per_temperature_extreme_hour
    operating_hours_score = operating_hours * score_per_operating_hour

    # Adjust scores based on battery age
    age_adjustment = battery_age * age_decay_factor
    total_score = (rebalance_score + deep_discharge_score + temperature_score + operating_hours_score) * (1 + age_adjustment)

    # Determine health status based on total score
    if total_score >= 75:
        health_status = "Critical"
    elif total_score >= 50:
        health_status = "Urgent"
    elif total_score >= 25:
        health_status = "Warning"
    else:
        health_status = "OK"

    return total_score, health_status

# Example use of the function
example_rebalance_overdue = 3  # days
example_deep_discharge = 2      # events
example_temperature_extremes = 10  # hours
example_operating_hours = 1500   # hours
example_battery_age = 2          # years

score, status = calculate_advanced_battery_health(example_rebalance_overdue, example_deep_discharge, 
                                                  example_temperature_extremes, example_operating_hours, 
                                                  example_battery_age)
print(f"Battery Health Score: {score}, Health Status: {status}")

