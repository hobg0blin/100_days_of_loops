print("digraph {")
print('  turtle_0[label="turtle"]')
for i in range(1, 100):
      print(f'  turtle_{i}[label="turtle"]')
      print(f"  turtle_{i-1}->turtle_{i}")
print("}")
