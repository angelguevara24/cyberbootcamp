# Users and Groups

## Instructions

### Research

- Use `whoami` to print your username.

- Use `id` to print your UID, group id, and other permissions info.

- Use `id <username>` to print out information about other users on the system.
  - In case you forgot, where can you find out what these usernames are?
  - Record the output from this series of commands to answer the questions below.

- Use `groups <username>` to print the groups you and the other users belong to.
  - Record the output from this series of commands to answer the questions below.

### Adding Users and Groups
- Add a user using the command demonstrated by the instructor.

- Add your new user to the secondary group after you create a new group.

- Check that this group assignment worked.

## Questions
- What's the advantage of allowing multiple users to have accounts on a single machine?

- What is the main purpose of groups?

- Which command do you use to add a user? There are two possible answers.

- Which command do you use to change a user's password?

- Which command do you use to:
  - Change a user's primary group?
  - Change a user's secondary group?

- Your user, `loki`, is in the primary group `nors`. Your new user is in `norse` as a secondary group.
  - If your new user creates a file, can `loki` read it?
  - If `loki` creates a file, can your new user read it?
  - If `loki` creates a file, what is that file's default group owner?
  - If your new user creates a file, what is that file's default group owner?
