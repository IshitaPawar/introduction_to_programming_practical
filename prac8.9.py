students = {
    "S101": {
        "name": "Asha",
        "marks": {
            "Python": 92,
            "Math": 88
        }
    },
    "S102": {
        "name": "Ravi",
        "marks": {
            "Python": 85,
            "Math": 90
        }
    }
}

print("Asha's Python marks:", students["S101"]["marks"]["Python"])

students["S101"]["marks"]["Python"] = 96

print("Updated student details:", students["S101"])
