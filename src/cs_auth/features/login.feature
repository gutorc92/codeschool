Feature: login

Scenario: User not registered
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	And I fill in "Email or username:" with "pedro"
	And I fill in "Password" with "teste"
	Then I press "Next"
	Then I should see "Please enter a correct username or email and password. Note that both fields are case-sensitive"

Scenario: Login in
	Given System create user "pedro"
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	And I fill in "Email or username:" with "pedro"
	And I fill in "Password" with "teste"
	Then I press "Next"
	Then I should see "Profile: pedro" 

Scenario: Wrong password
	Given System create user "joao" with password "testando"
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	And I fill in "Email or username:" with "joao"
	And I fill in "Password" with "teste"
	Then I press "Next"
	Then I should see "Please enter a correct username or email and password. Note that both fields are case-sensitive"

Scenario: Blank fields
	When I visit site page "/accounts/login"
	Then I should see "Welcome to Codeschool!" 
	Then I press "Next"
	Then I should see "Either supply us with your email or username." 
	Then I should see "This field is required."