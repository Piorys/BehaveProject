@profile
Feature: Twitter profile
	As a regular twitter user
	I want to be able to see and modify my profile details
	So my profile details can be up-to-date

	@T.2.1
	Scenario: T.2.1 Edit Profile Page
		Given I am logged in on main page 
		When I navigate to edit profile section
		Then I can see edit profile section

	@T.2.2
	Scenario: T.2.2 Adding Bio
		Given I am logged in on main page
		When I navigate to edit profile section
		And I will update my bio
		Then I will see my bio updated

	@T.2.3
	Scenario: T.2.3 Adding Location
		Given I am logged in on main page
		When I navigate to edit profile section
		And I will update my location
		Then I will see my location updated

