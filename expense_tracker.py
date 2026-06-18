import pandas as pd;

data = {
    'Date' : ['01-jun', '02-jun', '03-jun', '04-jun', '05-jun'],
    'Category' : ['Food', 'travel', 'shopping', 'Travel', 'Food'],
    'Description' : ['Lunch', 'Bus ticket', 'cloths', 'train ticket', 'Dinner'],
    'amount' : [150,200, 400, 300, 120]
}

df = pd.DataFrame(data);

print("========== expense tracker ============= ");
print(f"Total Expense : {len(df)}");
print(f"Total Amount : ₹{df['amount'].sum()}");
print(f"Average Spend : ₹{df['amount'].mean()}");
print(f"Highest Average : ₹{df['amount'].max()}");

print("\n Spending by categary");
df['Category'] = df['Category'].str.strip().str.title()
print(df.groupby('Category')['amount'].sum());

print("\n Biggest Expense");
print(df[df['amount'] == df['amount'].max()][['Description', 'amount']]);