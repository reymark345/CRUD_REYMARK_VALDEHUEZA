import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
import joblib

# Define the dataset
data = [
    {"client_status": "ACTIVE", "income": "LOW", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "NO", "eligible_to_claim": "YES"},
    {"client_status": "INACTIVE", "income": "HIGH", "member_status": "NEW", "duplicate_name_in_other_area": "YES", "verified_by_barangay": "NO", "physical_cash_card_presented": "YES", "eligible_to_claim": "NO"},
    {"client_status": "INACTIVE", "income": "MEDIUM", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "NO"},
    {"client_status": "ACTIVE", "income": "MEDIUM", "member_status": "NEW", "duplicate_name_in_other_area": "YES", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"},
    {"client_status": "ACTIVE", "income": "LOW", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"},
    {"client_status": "INACTIVE", "income": "HIGH", "member_status": "NEW", "duplicate_name_in_other_area": "YES", "verified_by_barangay": "NO", "physical_cash_card_presented": "YES", "eligible_to_claim": "NO"},
    {"client_status": "ACTIVE", "income": "MEDIUM", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "NO", "eligible_to_claim": "NO"},
    {"client_status": "ACTIVE", "income": "LOW", "member_status": "NEW", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "NO", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"},
    {"client_status": "INACTIVE", "income": "HIGH", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"},
    {"client_status": "INACTIVE", "income": "LOW", "member_status": "NEW", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"},
    {"client_status": "ACTIVE", "income": "HIGH", "member_status": "OLD", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "NO", "eligible_to_claim": "YES"},
    {"client_status": "ACTIVE", "income": "MEDIUM", "member_status": "NEW", "duplicate_name_in_other_area": "NO", "verified_by_barangay": "YES", "physical_cash_card_presented": "YES", "eligible_to_claim": "YES"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Separate features and target
X = df.drop(columns=['eligible_to_claim'])
y = df['eligible_to_claim']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = CategoricalNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the model and label encoders
joblib.dump(model, 'C:\\laragon\\www\\project\\naive_bayes_model.pkl')
joblib.dump(label_encoders, 'C:\\laragon\\www\\project\\label_encoders.pkl')
