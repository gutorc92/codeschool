Feature: Register

Background: 
	Given System check permissions

Scenario: Invalid email
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	Then I click "SIGN UP"
	And I fill in "id_first_name" with "Teste"
	And I fill in "id_last_name" with "Junior"
	And I fill in "id_username" with "teste"
	And I fill in "id_email" with "fjalkdjflaksdjal"
	And I fill in "id_password1" with "testando"
	And I fill in "id_password2" with "testando"
	Then I press "Next"
	Then I should see "Enter a valid email address."

Scenario: Duplicate username
	Given System create user "jteste2" with password "teste" and email "test@testando.com"
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	Then I click "SIGN UP"
	And I fill in "id_first_name" with "Teste"
	And I fill in "id_last_name" with "Junior"
	And I fill in "id_username" with "jteste2"
	And I fill in "id_email" with "test@testando.com"
	And I fill in "id_password1" with "testando"
	And I fill in "id_password2" with "testando"
	Then I press "Next"
	Then I should see "This username is already taken."

Scenario: Valide fields
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	Then I click "SIGN UP"
	And I fill in "id_first_name" with "Teste"
	And I fill in "id_last_name" with "Junior"
	And I fill in "id_username" with "teste"
	And I fill in "id_email" with "teste@testando.com"
	And I fill in "id_password1" with "testando"
	And I fill in "id_password2" with "testando"
	And I fill in "id_date_of_birth" with "10/07/1992"
	And I select "male" from "Gender" 
	And I fill in "id_about_me" with "I am a test user for checking if the register form is working well"
	Then I press "Next"
	Then The browser's URL should contain "teste"


