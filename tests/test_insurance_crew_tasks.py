import unittest
from unittest.mock import patch

from crewai.task import Task

from insurance_crew.agents.crew import InsuranceClaimCrew
from insurance_crew.tasks import InsuranceTaskFactory


class InsuranceCrewTaskTests(unittest.TestCase):
    def test_build_vision_task_uses_official_crewai_task(self):
        factory = InsuranceTaskFactory()
        task = factory.build_vision_task()

        self.assertIsInstance(task, Task)
        self.assertEqual(task.description, "Inspect the claim image evidence and summarize the damage findings.")

    def test_kickoff_delegates_to_official_crewai_crew(self):
        with patch("insurance_crew.agents.crew.Crew") as crew_cls:
            crew_instance = crew_cls.return_value
            crew_instance.kickoff.return_value = "crew-result"

            crew = InsuranceClaimCrew()
            result = crew.kickoff("claim-123", db={"claim_id": "claim-123"})

            self.assertEqual(result, "crew-result")
            crew_instance.kickoff.assert_called_once()
            kwargs = crew_instance.kickoff.call_args.kwargs
            self.assertEqual(kwargs["inputs"]["claim_id"], "claim-123")
            self.assertEqual(kwargs["inputs"]["db"], {"claim_id": "claim-123"})


if __name__ == "__main__":
    unittest.main()
