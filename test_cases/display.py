import pandas as pd 

# COPY PATH OF APP VERSION TEST CASE RESULTS

by_intent = pd.read_csv('test_cases/v1.0_test\QTIP_Accuracy_By_Intent.csv')
full_display = pd.read_csv('test_cases/v1.0_test\QTIP_Detailed_Test_Results.csv')
overall = pd.read_csv('test_cases/v1.0_test\QTIP_Overall_Results.csv')

print(by_intent)
print()
print(full_display)
print()
print(overall)