Feature: Disciplines creation

Background:
  Given System create admin user
	When I visit site page "/django-admin"
	And I fill in "Username:" with "admin"
	And I fill in "Password:" with "admin"
	And I press "Log in"

Scenario: Discipline is created with all required data 
	Given I visit site page "/django-admin/cs_courses/discipline/add/"
	When I fill in "Name:" with "Discipline"
	And I fill in "Short description:" with "A discipline"
	And I fill in "Long description:" with "A long descirption"
	And I press "Save"
  Then I should see "was added successfully."

Scenario: Discipline is not created without name
	Given I visit site page "/django-admin/cs_courses/discipline/add/"
	When I fill in "Short description:" with "A discipline"
	And I fill in "Long description:" with "A long descirption"
	And I press "Save"
  Then I should see "This field is required."

Scenario: Discipline is removed
  Given System create discipline "Discipline"
	And I visit site page "/django-admin/cs_courses/discipline"
	When I click in "Discipline (discipline)"
	When I click in "Delete"
	When I press "Yes, I'm sure"
  Then I should see "was deleted successfully."

Scenario: Discipline is removed with courses
  Given System create discipline "Discipline" with courses
	And I visit site page "/django-admin/cs_courses/discipline"
	When I click in "Discipline (discipline)"
	When I click in "Delete"
	When I press "Yes, I'm sure"
	Then I visit site page "/django-admin/cs_courses/course"
  Then I should see "0 courses"
