![](https://i.imgur.com/XyOI6vj.gif)

[![github action](https://github.com/israteneda/acme/workflows/tests/badge.svg)](https://github.com/israteneda/acme/actions)

Console app to calculate the total that the company has to pay an employee.

You can also check the docs at: https://acme-exercise.readthedocs.io/en/latest/

<details><summary>Problem Description</summary>
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Monday - Friday      | Saturday and Sunday  |
|----------------------|----------------------|
| 00:01 - 09:00 25 USD | 00:01 - 09:00 30 USD |
| 09:01 - 18:00 15 USD | 09:01 - 18:00 20 USD |
| 18:01 - 00:00 20 USD | 18:01 - 00:00 25 USD |

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

| Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|--------|---------|-----------|----------|--------|----------|--------|
| MO     | TU      | WE        | TH       | FR     | SA       | SU     |

**Input:** the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

**Output:** indicate how much the employee has to be paid

For example:

| Case       | Case 1                                                                     | Case 2                                           |
|------------|----------------------------------------------------------------------------|--------------------------------------------------|
| **Input**  | RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 | ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 |
| **Output** | The amount to pay RENE is: 215 USD                                         | The amount to pay ASTRID is: 85 USD              |
</details>

<details><summary>Architecture</summary>
</details>

<details><summary>Approach & Methodology</summary>
For the app development I used <a href="https://en.wikipedia.org/wiki/Kanban_(development)" target="_blank">Kanban Method</a> and <a href="https://en.wikipedia.org/wiki/Pomodoro_Technique" target="_blank">Pomodoro Technique</a>. 
</details>

<details><summary>Install & Run</summary>
</details>
