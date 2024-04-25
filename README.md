# Job-Posting-Alert
A redesign of a simple script I wrote at a previous job. The goal is to read a spreadsheet containing job posting information and let me know if there are any postings that need to be updated. If there are any updates needed, it sends an email. The redesign is a bit more stable and can read from any spreadsheet rather than being tied to a single sheet (the orginal script was an attachment to a google sheet).
The supplied Test_File.xlsx shows the spreadsheet layout.
    - Please ensure that dates are entered as plain text and in the YYYY-MM-DD format.
The config.ini file has the basic user data that can be changed by the user.
    - For the email list, please use comma seperators
    - The script defaults to sending the email to your email, so you do not need to add your own email to the list.