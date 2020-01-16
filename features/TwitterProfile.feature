Feature: Twitter profile
	As a regular twitter user
	I want to be able to see and modify my profile details
	So my profile details can be up-to-date

	Scenario: T.2.1 Edit Profile Page
		Given I am logged in on main page 
		When I navigate to edit profile section
		Then I can see edit profile section

	Scenario: T.2.2 Adding Bio
		Given I am logged in on main page
		When I navigate to edit profile section
		And I will update my bio
		Then I will see my bio updated
	
	Scenario: T.2.3 Bio character limit
		Given I am logged in on main page
		When I navigate to edit profile section
		And I will try to insert bio longer than 160 characters
		Then I will see that my bio is limited to 160 characters

