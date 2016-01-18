Feature: Guess a number home page
    Background:
        Given The user visits the web site home

    Scenario: The user can see the text 'Guess my number'
        Then the user can see 'guess my number'

    Scenario: The user can guess a number
        Then the user can input a number
        Then the user can see a guess button

    Scenario: The can see the answer if they want to
        Then the answer is present in the html but invisible
        Then the user can see a button to show the answer
        When the show answer button is clicked
        Then the answer is visible

    Scenario: The user is informed of a correct guess
        When the user enters a correct guess
        When the user clicks the guess button
        Then the user sees 'You guessed correctly'

    Scenario: The user is informed of an incorrect guess
        When the user enters an incorrect guess
        When the user clicks the guess button
        Then the user sees 'You guessed incorrectly'
