from insurance_crew.crew import InsuranceClaimCrew


def main():
    crew = InsuranceClaimCrew()

    print("=" * 60)
    print("Insurance Crew Initialized Successfully")
    print("=" * 60)
    print("Crew Wrapper :", type(crew))
    print("Crew Object  :", type(crew.crew))
    print("Total Tasks  :", len(crew.tasks))


if __name__ == "__main__":
    main()