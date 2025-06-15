from team_lead_class import TeamLead


class TestTeamLead:
    def setup_method(self):
        self.lead = TeamLead(
            name="Test",
            salary=100000,
            department="DevOps",
            programming_language="Go",
            team_size=3
        )

    def test_has_name(self):
        assert hasattr(self.lead, "name")
        assert self.lead.name == "Test"

    def test_has_salary(self):
        assert hasattr(self.lead, "salary")
        assert self.lead.salary == 100000

    def test_has_department(self):
        assert hasattr(self.lead, "department")
        assert self.lead.department == "DevOps"

    def test_has_programming_language(self):
        assert hasattr(self.lead, "programming_language")
        assert self.lead.programming_language == "Go"

    def test_has_team_size(self):
        assert hasattr(self.lead, "team_size")
        assert self.lead.team_size == 3
