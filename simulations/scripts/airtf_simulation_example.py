import pandas as pd
from pathlib import Path

# -------------------------------
# Responsibility Tax Formula
# -------------------------------
def calculate_rt(row):
    P = row["Profit(P)"]
    U = row["UnemploymentImpact(U)"]
    E = row["EnergyConsumption(E)"]

    alpha = row["Alpha"]
    beta = row["Beta"]
    gamma = row["Gamma"]

    RT = alpha * P + beta * U + gamma * E
    return RT


# -------------------------------
# Load Scenarios
# -------------------------------
def load_scenario(file_name):
    path = Path(__file__).parent / "../country-scenarios" / file_name
    return pd.read_csv(path)


# -------------------------------
# Run Simulation
# -------------------------------
def run_simulation(df):
    df["ResponsibilityTax(RT)"] = df.apply(calculate_rt, axis=1)

    # Redistribute
    df["WorkforceFund_40"] = df["ResponsibilityTax(RT)"] * 0.40
    df["UBI_30"] = df["ResponsibilityTax(RT)"] * 0.30
    df["GreenInfra_30"] = df["ResponsibilityTax(RT)"] * 0.30

    return df


# -------------------------------
# Main Entry
# -------------------------------
if __name__ == "__main__":
    scenario_files = [
        "US_Scenario_A_highAI.csv",
        "EU_Scenario_B_green_focus.csv",
        "Asia_Scenario_C_mixed.csv"
    ]

    for file in scenario_files:
        print(f"\n=== Running Simulation for {file} ===")
        df = load_scenario(file)
        result = run_simulation(df)
        print(result[[
            "Country", "Scenario",
            "ResponsibilityTax(RT)",
            "WorkforceFund_40", "UBI_30", "GreenInfra_30"
        ]])
