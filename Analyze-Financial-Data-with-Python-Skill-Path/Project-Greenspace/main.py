import codecademylib3_seaborn
import matplotlib.pyplot as plt

project_a = [-2000000, 0, 0, 50000, 250000, 500000, 500000, 750000, 750000, 500000, 500000, 500000, 500000, 500000, 1000000]

discount_rate = [0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]

def calculate_npv(rate, cash_flow):
    npv = 0
    for t in range(len(cash_flow)):
        npv += cash_flow[t]/(1+rate)**t
    return npv

npvs_a = list()
for rate in discount_rate:
  npv_a = calculate_npv(rate,project_a)
  npvs_a.append(npv_a)
  
plt.plot(discount_rate,npvs_a, linewidth = 3.0, color = "green", label = "Project Greenspace")
plt.axhline(y=0, linewidth = 0.5, color = "black")
plt.title('NPV Profile: Project Greenspace ')
plt.xlabel('Discount Rate')
plt.ylabel('Net Present Value')
plt.legend()
plt.show()

"""
1. The initial investment requires $2,000,000, or a cash flow for Year 1  of -2000000. Construction will take place in Years 2 and 3 (no cash flows will be generated by the project).
The project will generate revenue in Year 4 and will continue to generate cash flows until the project is sold in Year 10 for $1,000,000, or a cash flow for Year 10 of 1000000.
Based on these projections, what is the discount rate where the NPV of Project Greenspace equals 0?

2. The discount rate where the NPV is equal to 0, is at 0.11 (11%)
After some discussions, it looks like construction may take longer and the expected revenue in Year 4 is only $50,000, instead of $250,000. Change the cash flow for Year 4 (the 4th value in project_a) to 50000 and run the code.
What happens to the NPV profile curve? At what discount rate does NPV = 0? Open the hint to see the answer.
The NPV profile curve shifts to the left when the cash flow for Year 4 decreases from $250,000 to $50,000. The discount rate where the NPV of Project Greenspace equals 0 is now just under 10%.

3. Based on another update from the project team, the project is estimated to provide cash flows for 15 years rather than 10. The project will generate $500,000 years 10-14, and the final cash flow of $1,000,000 from selling the project will be realized in Year 15 when the project is sold.
Begin by updating the year 10 cash flow (the last number in project_a) to 500000.

4. Since years 11, 12, 13 and 14 will realize cash flows of $500,000, add four more entries to the end of project_a with the value 500000. Each entry should be separated by a comma.

5. In year 15 the project is sold for $1,000,000. Add as final entry to project_a the value 1000000 and then run the code by clicking “Save”.
What happens to the NPV profile curve? In this scenario, at what discount rate does Project Greenspace become unattractive?
With these cash flows, this project becomes unattractive at 0.14 (14%) discount.

"""


