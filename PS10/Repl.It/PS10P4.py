from FunctionPS10P4 import total_and_averageP4

# Get student's last name and exam scores from user
last_name = input("Enter student's last name → ")
s1 = float(input("    ◦ Enter exam score 1 → "))
s2 = float(input("    ◦ Enter exam score 2 → "))
s3 = float(input("    ◦ Enter exam score 3 → "))

# total points and average score
total_points, average_score = total_and_averageP4(s1, s2, s3)

# Display last name, total points, and average exam score
print("\n")
print("       \x1B[1;4m   ", last_name, "   \x1B[0m")
print("\n◦ Total points → ", int(total_points))
print("◦ Average exam score → {:.2f}".format(average_score))

