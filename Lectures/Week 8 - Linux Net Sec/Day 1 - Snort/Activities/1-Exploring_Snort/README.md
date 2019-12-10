# Exploring Snort
In this exercise, you'll explore a Snort installation to:
- Familiarize yourself with Snort's directory structure
- Inspect the Snort configuration file
- Examine Snort community rules

While today's exercises focus on Snort, the concepts you learn here are applicable to all Intrusion Detection Systems.

**Good luck!**

---

## Instructions
### The Snort Configuration File
Begin by moving into `/etc/snort`. Then, answer the questions below.

- Run: `grep -in step snort.conf`.
  - How many steps are there to configuring Snort?

- Open `snort.conf` in nano. Scroll down to Step 1.
  - What kind of information do you configure in Step 1?
  - How would you configure Snort to protect the home network `192.168.1.0/24`? **Note**: Don't actually change the config file—just write down how you'd do this.
  - **Note**: You can open the file at one of the line numbers from the grep output with `nano +<Line Number> snort.conf`.

- Scroll down to Step 7.
  - How do you add rules to Snort?
  - Which rules are included by default?
  - Edit the file to include `local.rules`.

### Inspecting Rules
- Navigate to `/etc/snort/rules`.
  - How many lines are in the files `local.rules`, `community.rules`, and `sql.rules`?
  - **Hint**: `wc -l`

- Run the following command to print the last rule in each file:
  - `tail -n 1 {local,sql,community}.rules`

- For each rule you see, identify the following:
  - What **action** does snort take when it matches this rule's pattern?
  - Which **protocol** does each rule watch for?
  - What are the source/destination addresses the rule monitors?
  - What kind of activity does each rule monitor for (e.g., command and control messages in the packet? embedded viruses? etc.)

  - Note the `content` keyword in all three words. Refer to the documentation at: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node32.html#SECTION00451000000000000000>
    - What does the `content` keyword allow you to do?
    - What does the `content` keyword in the last rule in `local.rules` do?
