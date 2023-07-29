# Journal

## Week 13 (June 19th - June 23rd)

During this week, I worked on the following tasks:

1. Created wireframes for the design of our restaurant app.
2. Created all API endpoints designs
3. Presented wireframes and endpoints to instructors

## Week 14 (June 26th - June 30th)

1. Ed [started the docker-compose.yaml](https://gitlab.com/backofthehouse/gastronomical-gems/-/commit/1f143d9ee7367a6ed2573a3c663b243ea0fbe937), there were issues deploying the project so I [redid our docker-compose.yaml](https://gitlab.com/backofthehouse/gastronomical-gems/-/commit/620af9a726360d5f76d130d6711bcb0f9a5fced8) as well as including pgadmin.
2. In addition to fixing the docker-compose.yaml, I [created the our first migration, queries, and router files](https://gitlab.com/backofthehouse/gastronomical-gems/-/commit/696f487279f5975932fb62171f73cac3dfa8665f) for the team to follow and apply. Specifically, for accounts. "Get all accounts" and "Create Account" endpoints were created specifically.
3. Found out that some members of the team have not began cloning the project repo and were having issues with initial docker deployment.
4. The team was still having trouble with git commands so I went over the proper steps with Ben and Ed. We had everyone make "test journal entries" as the document to push and commit to the main branch. The team was also struggling to understand how to properly sync sub-branches and create a merge request to main and apporoving it.
5. I went over with with the team how to create migrations and endpoints. Ben and Ed were present and Alec left after going over git commands. Raymond was not present due to family obligations.
6. Ed [added sections of his Mod2 frontend code](https://gitlab.com/backofthehouse/gastronomical-gems/-/commit/d89c8a68a470c18d76b5d9e97f2300b6322ca84e) to begin the frontend templates. Some features are appearing visually but no backend functionality.
7. I reminded and asked the team again to create endpoints based off my example with "accounts" over the break.

## Week 15 (July 10th - July 14th)

1. Ed showed the team how to create migrations. No git commits avaiable to link.
2. I asked Ed to create endpoints for "/menu_items" and Ben to create endpoints for "/order" as they've claimed they're caught up on the the curriculum.
3. I focused on getting the backend authenticaion online. I installed jwtdown-fastapi into our fastapi directory/requirements.txt. Additionally, I generated the unique signing_key to our docker-compose.yaml file.
4. I also created our authenticator file by following the module on Learn regarding backend auth. I adjust the files from the tutorial so that it was appropriate for our project.
5. I was able to successfully implement backend authentication by successfully generating a token for a new user. This is [the merge request](https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/25/diffs) for the above feature.
6. After backend auth has been implemented, I create the queries and routers for reservations to handle the CRUD operations via [this merge request](https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/20/diffs)

## Week 16 (July 17th - July 20th)

1. I notified the team that I would be offline on Thursday, leaving 3 days to work on frontend authorization.
2. I created the initial frontend pages "SignupForm.js" and "LoginForm.js" while finalizing reservation endpoints to reference account_id as a foreign key via [this merge request](https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/36)
3. Although the frontend forms are able to submit data to the backend, the login does not work since it's not able to sucessfully fetch the token from the backend.
4. I eventually fixed the front end auth issue by updating my import to '@galvanize-inc/jwtdown-for-react' [Merge Request #41](https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/41/diffs). Our project can now allow users to create an account and sucessfully login with a token. I also updated our Nav.js to checkToken and display the proper Nav items depending on the login status of the user.

## Week 16 (July 17th - July 20th)
1. Monday, I encountered an issue trying to post new accounts into the backend via the signup form. It was resolved with Instructor Zach by fixing a typo in my routers/accounts.py
2. Tuesday, worked with a team to help un-stuck folks from their backend point issues. Fetch issues, CORS errors, etc. Some good progress was made.
3. Wedneday, started off the day with Signup/Login breaking again on local and our deployed project - it was resolved with Instructor Paul when we finally created a .env file (vs. .env.sample)
4. Thursday, finalized the accounts edit form and accounts detail page having accountData being carried across the app with the useContext hook. Began working on unit tests
5. Unit tests finalized, our team was scrambling in preparation for the presentation with Instructor Paul. Everyone did well and we all individuallly satisfied the MVP requirements as a team. After presentation, we put together the finalize touches to clean our code, update journals, git issues, and a few people wanted to quash bugs within their code. Overall, we came very far since week1 and we're proud of ourselves.
