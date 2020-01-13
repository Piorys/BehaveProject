Feature: Twetting
	As a regular Twitter User
	I want to be able to create/read/delete my tweets
	So I can manage my tweets easily

	Scenario: T.1.1 - Create Post
		Given I am logged in on main page
		When I create a new tweet
		Then I can see new tweet should be visible on my personal feed
	
	Scenario: T.1.2 - Create Post Widget
		Given I am logged in on main page
		Then I can see widget for tweet creation
	
	Scenario: T.1.3 - Delete Tweet
		Given I am logged in on main page
		When I delete one of my previously created tweets 
		Then I can no longer see it on my personal feed
	
	Scenario: T.1.4 - Post character limit
		Given I am logged in on main page
		When I try to create tweet longer than 280 characters
		Then I will see warning that my limit has been exceeded
