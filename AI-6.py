def evaluate_performance(attendance, projects_completed, teamwork_score):
    if attendance >= 90 and projects_completed >= 5 and teamwork_score >= 8:
        return "Excellent"
    elif attendance >= 75 and projects_completed >= 3 and teamwork_score >= 6:
        return "Good"
    elif attendance >= 60 and projects_completed >= 2 and teamwork_score >= 5:
        return "Average"
    else:
        return "Needs Improvement"

def main():
    print("=== Employee Performance Evaluation System ===")
    try:
        attendance = float(input("Enter attendance percentage (0-100): "))
        projects_completed = int(input("Enter number of projects completed: "))
        teamwork_score = float(input("Enter teamwork score (1-10): "))

        result = evaluate_performance(attendance, projects_completed, teamwork_score)
        print(f"\nPerformance Rating: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
