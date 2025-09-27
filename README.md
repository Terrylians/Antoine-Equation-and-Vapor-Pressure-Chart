**Antoine-VaporPlotter**


A small Python project to calculate and plot vapor pressure vs. temperature using the Antoine equation, built with pandas and matplotlib. Ideal for quick visualizations, teaching demonstrations, and simple process checks.

**What it does**

Computes vapor pressure across a temperature range using the Antoine equation.
Produces publication-quality plots (vapor pressure vs temperature) with matplotlib.
Accepts different Antoine coefficients for multiple substances and compares them.
Exports results to CSV for further analysis.
Antoine equation

**The (common) Antoine form used here:**

log10(P) = A - B / (C + T)
P = vapor pressure (units depend on which Antoine constants you use — often mmHg or bar)
T = temperature (°C)
A, B, C = Antoine constants for the chosen substance

Important: Make sure you use Antoine constants that match your desired pressure unit and temperature range. The equation form and units can vary between data sources.

**Features**

Single-substance or multi-substance plotting
Linear or log pressure axis
Save numeric results to CSV
Easy to extend to different units or equations

<img width="807" alt="Screenshot 2025-02-04 at 10 46 02" src="https://github.com/user-attachments/assets/1d4528b5-21e5-41ba-ab21-729d2adf02ae" />

Example of vapor pressure curve based on Methane (CH4)
