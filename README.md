# Description
This is a Python script that can be used to automate JIRA tasks in the sprint-planning process for scrum teams.

These tasks include: 
- Sprint creation and sprint ending events
- Transferring incomplete JIRA issues from one sprint to the next

<br/>
<br/>

## Table of Contents

[Technologies Used](#technologies-used)  
[Design Diagram](#design-diagram)  
[How to Use](#how-to-use)
[FAQ](#faq)  
[License](#license)  
[Support](#support)  

<br/>
<br/>

## Technologies Used

<ins>Python v3.13.0</ins>

Core language used.

<br/>

<ins>Python Libraries</ins>  

`requests` - Makes HTTP requests to interact with the JIRA API.  
`base64` - Encodes JIRA credentials into a base64 string for authentication.  
`os` - Accesses environment variables securely.  
`datetime` & `timedelta` - Manages date and time calculations.  
`logging` - Handles output and logging.    
`certifi` - Handles SSL certificate verification.  
`time` - Creates wait times between batch submissions of issues to the JIRA API.  
`sys` - Raises exceptions that signal failure to the GitHub Actions workflow.   

<br/>

<b>JIRA Agile REST API</b>

Possesses the endpoints that the script interacts with.

<br/>

<b>Mermaid</b>

Used in the README markdown file to document and visualize the logical workflow of the script.  

<br/>
<br/>

## Design Diagram

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
classDef yes_or_no stroke: #fff, stroke-width: 1.5px;
```

<br/>
<br/>

## How to Use

(Section coming soon)

<br/>
<br/>

## FAQ

<details>
<summary>&nbsp; How is the new sprint named? &nbsp;</summary><br/>

> The new sprint name will be generated using the definition of the `sprint_name` variable.
> 
> Users may customize this variable to take advantage of dynamically-generated sprint names if successive sprints use a particular 
> naming convention.

</details>

<br/>

<details>
<summary>&nbsp; How are unfinished issues tracked from one sprint to the next? &nbsp;</summary><br/>

> Because sprints are closed before a transfer occurs, any unfinished stories will display as 'Issues Not Completed' in the sprint
> status report. 
> 
> This approach avoids the appearance of users manually removing their stories from a sprint.

</details>

<br/>

<details>
<summary>&nbsp; How is the automation schedule being set for this script? &nbsp;</summary><br/>

> The script runs automatically based off the `cron` expression in the sprint_automation yaml file located in the .github folder.  
>   
> More information on cron expressions can be found [here](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).  


</details>

<br/>
<br/>

## License

This project, including the Python script and accompanying documentation, is licensed under the MIT license. See the [LICENSE](LICENSE)
file for details.

<br/>
<br/>

## Support

For any questions or assistance, please reach out to the project creator. 
