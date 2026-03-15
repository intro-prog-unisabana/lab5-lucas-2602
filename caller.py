

# FREEZE CODE BEGIN
x = int(input())
y = float(input())
# FREEZE CODE END

from mystery_module import transform_data
res = transform_data(x, y, "quiz_test")
print(res)
