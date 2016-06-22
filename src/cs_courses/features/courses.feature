Feature: Courses creation

Background:
  Given System create admin user
  And System create discipline "Discipline"
	When I visit site page "/django-admin"
	And I fill in "Username:" with "admin"
	And I fill in "Password:" with "admin"
	And I press "Log in"

Scenario: Course is created with all required data 
	Given I visit site page "/django-admin/cs_courses/course/add/"
  When I select "Discipline (discipline)" from "id_discipline"
  And I select "admin" from "id_teacher"
	And I press "Save"
  Then I should see "was added successfully."

Scenario: Course is not created without discipline 
	Given I visit site page "/django-admin/cs_courses/course/add/"
  When I select "admin" from "id_teacher"
	And I press "Save"
  Then I should see "This field is required."

Scenario: Course is not created without teacher 
	Given I visit site page "/django-admin/cs_courses/course/add/"
  When I select "Discipline (discipline)" from "id_discipline"
	And I press "Save"
  Then I should see "This field is required."

Scenario: Course is removed
  Given System create course "Course"
	And I visit site page "/django-admin/cs_courses/course"
	When I click in "Course"
	When I click in "Delete"
	When I press "Yes, I'm sure"
  Then I should see "was deleted successfully."
