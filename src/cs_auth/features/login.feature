Feature: login

Scenario: User not registered
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	And I fill in "Email or username:" with "pedro"
	And I fill in "Password" with "teste"
	Then I press "Next"
	Then I should see "Please enter a correct username or email and password. Note that both fields are case-sensitive"
	 
