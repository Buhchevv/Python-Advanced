def students_credits(*args):
    total_credits = 0
    credits_info = dict()
    final_strings = []

    for info in args:
        course_name, course_credits, max_test_points, points = info.split("-")
        current_percentage = int(points) / int(max_test_points)
        current_credits = current_percentage * int(course_credits)
        total_credits += current_credits
        credits_info[course_name] = current_credits

    if total_credits >= 240:
        final_strings.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        final_strings.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")
    sorted_dian_points_info = sorted(credits_info.items(), key=lambda a: -a[1])

    for course, points in sorted_dian_points_info:
        final_strings.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_strings)


print(

    students_credits(

            "Discrete Maths-40-500-450",
            "AI Development-20-400-400",
            "Algorithms Advanced-50-700-630",
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Game Engine Development-70-100-70",
            "Mobile Development-25-250-225",
            "QA-20-300-300",

    )

)