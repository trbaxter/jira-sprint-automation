# Description
This is a Python script that can be used to automate JIRA tasks in the sprint-planning process for scrum teams.

<br/>
<br/>

# Table of Contents

[Technologies Used](#technologies-used)  
[Design Diagram](#design-diagram)  
[FAQ](#faq)  
[License](#license)  
[Support](#support)  

<br/>
<br/>

# Technologies Used

<b>Python v3.7</b> - Core language used in the automation script.

<b>Python Libraries:</b>  

`requests` - Used for making HTTP requests to interact with the JIRA API.  
`base64` - Used for encoding JIRA credentials into a base64 string for authentication.  
`os` - Used to access environment variables securely, such as API tokens and email addresses.  
`datetime` & `timedelta` - Used to manage date and time calculations for sprint start and end periods.  
`logging` - Used to handle output and logging throughout the script.  
`certifi` - Used to handle SSL certificate verification and ensure HTTPS connections are secure.

<b>JIRA Agile REST API</b> - Contains the endpoints that the script interacts with.

<b>Mermaid</b> - Used in the README markdown file to document and visualize the logical workflow of the script.  

<br/>
<br/>

# Design Diagram

```mermaid

%%{init:
    {
        "flowchart": 
        {
            "rankSpacing": 30,
            "nodeSpacing": 20
        }
    }
}%%

flowchart TD

%% Start %%
start([&nbsp; Start &nbsp;]):::start

%% End %%
finish([&nbsp; Finish &nbsp;]):::finish

%% Actions %%
A1[&nbsp; Use next sprint &nbsp; <br/> in the backlog]:::action
A2[&nbsp; Generate &nbsp; <br/> new sprint]:::action
A3[Collect IDs of <br/> &nbsp; incomplete stories &nbsp;]:::action
A4[&nbsp; End current sprint &nbsp;]:::action
A5[&nbsp; Move incomplete stories &nbsp; <br/> to new sprint]:::action
A6[&nbsp; Start new sprint &nbsp;]:::action
A7[&nbsp; Output error log &nbsp;]:::action

%% Decisions %%
D1{Is there an <br/> upcoming sprint <br/> in the backlog?}:::decision
D2{Sprint created <br/> successfully?}:::decision
D3{Is there <br/> an active sprint?}:::decision

%% Yes/No Nodes %%
YES1([&nbsp; <b>Yes</b> &nbsp;]):::yes_or_no
YES2([&nbsp; <b>Yes</b> &nbsp;]):::yes_or_no
YES3([&nbsp; <b>Yes</b> &nbsp;]):::yes_or_no
NO1([&nbsp; <b>No</b> &nbsp;]):::yes_or_no
NO2([&nbsp; <b>No</b> &nbsp;]):::yes_or_no
NO3([&nbsp; <b>No</b> &nbsp;]):::yes_or_no

%% Links %%
start --> D1
D1 --- YES1 --> A1
D1 --- NO1 --> A2
A2 --> D2
D2 --- YES2 --> D3
D2 -.- NO2 -.- A7 -.-> finish
A1 --> D3
D3 --- YES3 --> A3
D3 --- NO3 --> A6
A3 ---> A4
A4 ---> A5
A5 ---> A6
A6 ---> finish

%% Class Colors %%
classDef start stroke: #0f0, stroke-width: 2.5px;
classDef finish stroke: #f00, stroke-width: 2.5px;
classDef decision stroke: #cc5500, stroke-width: 2.5px;
classDef action stroke: #196de3, stroke-width: 2.5px;
classDef yes_or_no stroke: #fff, stroke-width: 2.5px;
```

<br/>
<br/>

# FAQ

<details>
<summary>&nbsp; How is the new sprint named? &nbsp;</summary><br/>

> The new sprint will be generated using the definition of the `sprint_name` variable.

</details>

<br/>

<details>
<summary>&nbsp; How are unfinished issues tracked from one sprint to the next? &nbsp;</summary><br/>

> Because sprints are closed before a transfer occurs, any unfinished stories will display as 'Issues Not Completed' in the sprint
> status report. 

</details>

<br/>

<details>
<summary>&nbsp; How is the automation schedule being set for this script? &nbsp;</summary><br/>

> The script runs automatically based off the `cron` expression in the sprint_automation yaml file located in the .github folder.  
>   
> More information on cron expressions can be found [here](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).  
> 
> The current configuration runs on a bi-weekly schedule based on the initial run date, aligning with the typical 2-week sprint period.

</details>

<br/>
<br/>

# License

This project, including the Python script and accompanying documentation, is licensed under the MIT license. See the [LICENSE](LICENSE)
file for details.

<br/>
<br/>

# Support

For any questions or assistance, please reach out to the project creator. 
