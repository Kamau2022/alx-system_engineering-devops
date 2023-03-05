# Summary
For one hour and 25 minutes between the hour of 1:35 AM  and 15:00PM PT, on 07/03/2023 request to our website resulted to  an internal server error. This incident affected 100%  of users and 123 number of support tickets were submitted. The root cause of this error was  due to wrong configurations of the .htaccess file.
Timeline (all times Pacific Time)
    • 1:25 pm – The last configurations done on the file 
    • 1:35 pm – Outage begins
    • 1:35 pm– Pager alerts teams
    • 1:38 pm - error logs and file/folder permissions were examined.
    • 1:47 pm - The permissions for newly created folders and files were checked.
    • 1:49 pm – Configurations were done on the .htaccess file
    • 1:56pm – Apache server was restarted
    • 1:57pm – Server request made was successful. 
# Root Cause and Resolution
At 1:25 pm a configuration directive was put in our .htaccess file and the effect of this configuration was never tested. This change in the file configuration introduced a bug, which made it impossible to access services on our website. The outage began at 1:35pm and whenever a request was made an internal error message was displayed on webpage. At 1:35 pm the monitoring systems alerted our engineer who investigated the error logs and the file/folder permissions. After failing to identify the cause of the error, the engineer escalated the issue. The team examined the httpd error log and found the directive used in our.htaccess file is not permitted. The directive causing the error was removed, our web servers were restarted and a request made at 1:57 pm was  successful.

# Corrective and preventative measures
Our team has conducted an in depth analysis of the outage. It was unanimously agreed that .htaccess files should only be used if  one has no access to httpd main server config file. We were able to come up with the other measures that will prevent the incident from happening in the future:
    • Any directive that you can include in a .htaccess file should be  set in a directory block, as it will have the same effect with better performance.
    • Ensure there is a backup file.
    • AllowOverride should be set such that configuration directives are being honored.
    • Allow only few individuals to access and configure the .htaccess file.
    • Develop better mechanism for quickly delivering status notifications during incidents.
    • Tests should be conducted whenever changes are made to the file.
