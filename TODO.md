
###Models
- User (use abstract model)
- Course
- Lesson
- Task
- Submission
- Badge
- UserBadge

###Issues
- Difficulty adding multiple text input fields in one and the same task
- Difficulty generalizing layout with this db structure.
- Considering scrapping/thinning out the db design, and rather use markdown for at least the tasks.
- Another solution which keeps the database as is can consider each task as code snippets, and each lesson would be instructions to the tasks for said lesson. That way I can loop over every task associated with a lesson, and render an input field for each task. Remember to use | safe when necessary.