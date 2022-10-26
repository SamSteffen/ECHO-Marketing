# ECHO Idaho Marketing Campaigns (2018-2021)
The following is a visualization project analyzing various Mail Chimp email marketing campaigns for a continuing education platform serving Idaho's rural healthcare workforce, using Python's pandas and matplotlib libraries.

## Overview
### ECHO Idaho Program Structure
[ECHO Idaho](https://www.uidaho.edu/academics/wwami/echo) is a free, virtual continuing education platform available for Idaho healthcare professionals. Housed at the University of Idaho, WWAMI Medical Education Program, the program is Idaho's only available chapter of the Extensions for Community Healthcare Outcomes organization, a global initiative intended to improve patient healthcare outcomes in rural and underserved communities through the democratization of expertise. The program is grant funded.

ECHO Idaho was initiated in 2018 with a single series focusing on Opioid and Addiction Treatment. Since its inception, the program has proliferated to span 10 different series on a variety of healthcare topics, and now has registered more than 3,000 unduplicated Idaho healthcare professionals in its community. Series typically offer hour-long sessions twice a month over the lunch-hour, Monday through Thursday. Each series features an interdisciplinary panel of experts who facilitate the conversation during each session; each session features a 20-30 minute didactic presentation as well as a real de-identified case presentation presented by a volunteer.

### How ECHO Idaho Uses Emails
For a free, virtual continuing education platform that conducts its web-based services primarily over Zoom teleconferencing software, email marketing is one of the primary ways that the program is able to reach new and existing audiences. Because ECHO Idaho is housed at the University of Idaho, ECHO Idaho's email marketing campaigns are bound by the same rules governing those of the University, which stipulate that emails originating from the University of Idaho can only be sent to individuals who have "opted in" to receive them. This "opt in" decision on the user-end is usually made during the registration process, via the ECHO Idaho website's registration page: https://www.uidaho.edu/academics/wwami/echo/register 
Once an individual has completed the registration for one or several ECHO series, their information is added to ECHO's mothership database, iECHO. iECHO stores data for all of ECHO Idaho's participants as well as all of the other ECHO programs, globally.

Completing registration prior to or following an ECHO session is NOT required to attend and participate in ECHO Idaho sessions. 

Until November of 2022, the University of Idaho utilized MailChimp as its primary email communications instrument. 

### Types of Emails Sent by ECHO Idaho
From its inception ECHO Idaho has utilized several types of email campaigns to effectively recruit and maintain attendance across series:
1. **Series-specific day-of emails:**    
These are emails that individuals who are registered for a particular series receive the day of the event; their contents feature series name, topic, speaker, relevant zoom link, time, contact info, etc.
2. **Weekly Emails:**    
Because ECHO is of a size now where it has multiple sessions from different series each week, a weekly email is sent out every Monday morning, featuring all of the ECHO sessions occuring in a given week. These emails also feature announcements about upcoming events and participant reminders.
3. **Newsletters:**    
In August of 2020, ECHO Idaho sent its first newsletter. These were initially sent quarterly, then bi-montlhly. As of 2022, they have become semi-bi-monthly (meaning sometimes they're sent every month).
4. **Special Announcements:**    
Special announcement emails are utilized for special occasions, guest speakers, series launches/re-launches, special registrations, redactions and other infrequent or singular events and communications. 

### Data Sources
The data sources for this analysis include:
1. **[iECHO](https://iecho.unm.edu/)**    
An ECHO program-specific online database where personal info (name, email, credential, workplace, residence, etc.) as well as series and session attendance records are stored;
2. **MailChimp**    
The University of Idaho's main communications system, which stores and preserves metrics fo each campaign such as: how many people received each email, how many times it was opened, how many times it was forwarded, how many links were clicked, etc.;
3. **[eeds](https://www.eeds.com/cloud-based-tracker-for-cme/healthcare-professionals)**    
An online platform where healthcare professionals are able to create and track continuing education credits earned for participation in ECHO Idaho and other event-based CE;
4. **[SoundCloud](https://soundcloud.com/user-658492948)**    
The host site of ECHO Idaho's CE-eligible podcast, *[Something for the Pain](https://www.uidaho.edu/academics/wwami/echo/podcast)*.

### Why Emails?
The purpose of this analysis is to bring these disparate data sources together to create visualizations for attendance and email data for each ECHO series and activity years (2018-2021). It is also to determine the following:
- The efficacy of daily email campaigns on program attendance (the relationship between email open-rates and session attendance).
- The efficacy of weekly email campaigns on program attendance (the realtionship between email open-rates and session attendance).
- What can be learned from the ECHO sessions with the best attendance and the type of email campaign that was used to promote it? 
- What can be learned from the ECHO sessions with the worst attendance and the type of email campaigns used to promote it?
- Using cumulative email and attendance data, establish a metric that can be used to determine successfull versus unsuccessful email campaigns for future marketing purposes.

## Results
To illustrate the impact of email campaigns on ECHO Idaho's series by attendance, it's important to state the various education series ECHO Idaho has hosted by program year. The following represents a dataframe showing 10 series, broken down by series name, launch-date and end-date:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/series_session_count_df.jpg" alt="df1" width="400"/>

* Note that the several of the above series have continued beyond the listed "end-dates." The iECHO attendance data is presented cumulatively at the end of the year; hence this data "ends" at the end of Dec. 2021 but does not necessarily indicate the end of a series. This df and the data in this analysis omits attendance data that is currently being gathered for series that began in 2022, like Pediatric Autism and MOUD Consultation Hours.

### ECHO Series Offered by Year
#### 2018    
- [Opioid Addiction and Treatment series](https://www.uidaho.edu/academics/wwami/echo/current-series/opioid-program) (eventually became "Opioids, Pain and Substance Use 
       Disorders" in Jan. 2021, hereafter abbreviated "**OPSUD**")
- [Behavioral Health in Primary Care series](https://www.uidaho.edu/academics/wwami/echo/current-series/behavioral-health) (hereafter abbreviated "**BH in PC**") 
- [MAT Waiver Training](https://www.uidaho.edu/academics/wwami/echo/xwaiver) (eventually renamed "X-Waiver Training", hereafter abbreviated "**XWT**")

#### 2019    
- OPSUD
- BH in PC
- XWT

#### 2020    
- OPSUD
- BH in PC
- XWT
- [COVID-19 series](https://www.uidaho.edu/academics/wwami/echo/current-series/covid-19) (hereafter abbreviated "**COVID**")
- [Syphilis in Pregnancy series](https://www.uidaho.edu/academics/wwami/echo/past-series/syphilis) (hereafter abbreviated "**Syphilis**")
- [Perinatal Substance Use Disorder series](https://www.uidaho.edu/academics/wwami/echo/past-series/perinatal-substance-2021) (hereafter abbreviated "**PSUD**")
- [COVID-19 Nursing-Home Safety series](https://www.uidaho.edu/academics/wwami/echo/past-series/nursing-home) (eventually re-name COVID-19 Safety for Post-Acute and Long-Term Care facilities, hereafter abbreviated "**PALTC**")

#### 2021    
- OPSUD
- BH in PC
- XWT
- COVID
- PALTC
- PSUD
- [Pediatric Behavioral Health](https://www.uidaho.edu/academics/wwami/echo/past-series/pediatric-behavioral-health) (hereafter abbreviated "**PBH**")
- [Hepatitis C](https://www.uidaho.edu/academics/wwami/echo/current-series/hepatitis-c) (eventually renamed "Viral Hepatitis and Liver Care", hereafter abbreviated "**VHLC**")
- Counseling Techniques for Substance Use Disorders (herafter abbreviated "**CTSUDs**")   

---

### 2018 Analysis

The barchart below shows the quantity of emails sent for all available ECHO series in 2018:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2018/plotly/email_charts/emails_2018.png" width="800"/>

The line graph below illustrates session attendance for all ECHO series offered in 2018:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/attendance_charts/cumulative_2018_attendance_chart.jpg" alt="Session attendance 2018" width="800"/>

The bubble chart below depicts the attendance by region for each ECHO Idaho series offered in 2018:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2018/plotly/maps/2018_cumulative_map.png" width = "800"/>

The line graphs below illustrates the relationship between session attendance for ECHO Idaho's 2018 series against the number of individuals who received emails about the series.  

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2018/plotly/att_and_email_charts/att_v_email_bhpc_2018.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2018/plotly/att_and_email_charts/att_v_emails_2018_opsud.png" width="800"/>

> **FINDING:**
> The above charts illustrate that despite rapid increase in the number of people who receive ECHO Idaho day-of campaign emails for the Opioid series, attendance at the ECHO sessions remained relatively constant over time. For the BH in PC series, the quantity of email recipients remains constant while the session attendance gradually declines.   

---

### 2019 Analysis

The barchart below shows the quantity of emails sent for all available ECHO series in 2019:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2019/plotly/email_charts/emails_2019.png" width="800"/>

The line graph below illustrates session attendance for all ECHO series offered in 2019:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/attendance_charts/cumulative_2019_attendance_chart.jpg" alt="Session attendance 2019" width="800"/>

The bubble chart below depicts the attendance by region for each ECHO Idaho series offered in 2019:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2019/plotly/maps/2019_cumulative_map.png" width = "800"/>

The line graphs below illustrate the relationship between session attendance for ECHO Idaho's 2019 series against the number of individuals who received emails about the series. 

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2019/plotly/att_and_email_charts/att_v_emails_bhpc_2019.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2019/plotly/att_and_email_charts/att_v_emails_opsud_2019.png" width="800"/>


> **FINDING:**
> The above charts illustrate that despite continued increase in the number of people who receive ECHO Idaho day-of campaign emails, attendance at the ECHO sessions remains relatively constant over time.   

---

### 2020 Analysis

The barchart below shows the quantity of emails sent for all available ECHO series in 2020:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/email_charts/emails_2020.png" width="800"/>

The line graph below illustrates session attendance for all ECHO series offered in 2020:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/attendance_charts/cumulative_2020_attendance_chart.jpg" alt="session attendance 2020" width="800"/>

The bubble chart below depicts the attendance by region for each ECHO Idaho series offered in 2020:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/maps/2020_cumulative_map.png" width = "800"/>

Because the initial session of ECHO Idaho's COVID-19 series drew 600 attendees, the datapoint for that session, while accurate, represents a considerable outliar. Below is a graph representing the 2020 data with the outliars removed.

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/attendance_charts/cumulative_2020_attendance_chart%20-%20sans_outliars.jpg" width="800"/>

The line graphs below illustrate the relationship between session attendance for ECHO Idaho's 2020 series against the number of individuals who received emails about the series. 

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/att_and_email_charts/att_v_emails_bhpc_2020.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/att_and_email_charts/att_v_emails_opsud_2020.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/att_and_email_charts/att_v_emails_covid_2020.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/att_and_email_charts/att_v_emails_paltc_2020.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/att_and_email_charts/att_v_email_syphilis_cumulative.jpg" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2020/plotly/att_and_email_charts/att_v_emails_psud_2020.png" width="800"/>

>**FINDING:**
>The above charts illustrate that despite continued increase in the number of people who receive ECHO Idaho day-of campaign emails, attendance at the ECHO sessions remains relatively constant over time.   

---

### 2021 Analysis

The barchart below shows the quantity of emails sent for all available ECHO series in 2021:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/email_charts/emails_2021.png" width="800"/>

The line graph below illustrates session attendance for all ECHO series offered in 2021:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/attendance_charts/cumulative_2021_attendance_chart.jpg" width="800"/>

The bubble chart below depicts the attendance by region for each ECHO Idaho series offered in 2021:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/maps/2021_cumulative_map.png" width = "800"/>

The line graphs below illustrate the relationship between session attendance for ECHO Idaho's 2021 series against the number of individuals who received emails about the series. 

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/att_and_email_charts/att_v_emails_bhpc_2021.png" width="800"/> 

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/att_and_email_charts/att_v_emails_opsud_2021.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/att_and_email_charts/att_v_emails_covid_2021.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/att_and_email_charts/att_v_emails_paltc_2021.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/2021/plotly/att_and_email_charts/att_v_emails_psud_2021.png" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/att_and_email_charts/att_v_email_pbh_cumulative.jpg" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/att_and_email_charts/att_v_email_ctsuds_cumulative.jpg" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/att_and_email_charts/att_v_email_vhlc_cumulative.jpg" width="800"/>

> **FINDING:**
> The above charts illustrate that despite continued increase in the number of people who receive ECHO Idaho day-of campaign emails, attendance at the ECHO sessions remains relatively constant over time.   

---

### Cumulative Analysis (2018-2021)

The barchart below shows the quantity of emails sent for all available ECHO series from 2018-2021:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/Email_campaigns_2018-2022.jpg" width="800"/>

The line graphs below illustrate the relationship between session attendance for each of ECHO Idaho's  series against the number of individuals who received emails about the series, from the start of the series to the end of the series or the end of the 2021 calendar year. 

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_bhpc.jpg" alt="bhpc email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_opsud.jpg" alt="OPSUD email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_covid.jpg" alt="COVID email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_paltc.jpg" alt="PALTC email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_ctsuds.jpg" alt="CTSUDs email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_psud.jpg" alt="PSUD email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_pbh.jpg" alt="PBH email v attendance cumulative" width="800"/>  

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_syphilis.jpg" alt="Syphilis email v attendance cumulative" width="800"/>

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/plotly/email_charts/cumulative_emails_vhlc.jpg" alt="VHLC email v attendance cumulative" width="800"/>

The scatter plot below illustrates the growth of ECHO Idaho's programs by new attendees over time:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/matplotlib/New_attendees_per_session_cumulative.png" alt="New attendees per session cumulative" width="800"/>

Here is the same data color-coordinated to show which series brought in new participants, and when:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/matplotlib/New_attendees_by_series_cumulative.png" alt="New attendees by series" width="800"/>

The scatter plot below illustrates the net growth of ECHO's population by new attendees over time:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/matplotlib/Net_attendance_growth_cumulative.png" alt="Net attendance growth" width="800"/>

Here is the same data color-coordinated to show which series brought in new participants, and when:

<img src="https://github.com/SamSteffen/ECHO-Marketing/blob/main/Visualizations/Cumulative/matplotlib/Net_attendance_growth_by_series_cumulative.png" alt="Net attendance by series" width="800"/>

>**FINDING:**
>The above charts illustrate that despite continued increase in the number of people who receive ECHO Idaho day-of campaign emails, attendance at the ECHO sessions remains relatively constant over time.   

---

## Summary
- The efficacy of daily email campaigns on program attendance (the relationship between email open-rates and session attendance).
- The efficacy of weekly email campaigns on program attendance (the realtionship between email open-rates and session attendance).
- What can be learned from the ECHO sessions with the best attendance and the type of email campaign that was used to promote it? 
- What can be learned from the ECHO sessions with the worst attendance and the type of email campaigns used to promote it?
- Using cumulative email and attendance data, establish a metric that can be used to determine successfull versus unsuccessful email campaigns for future marketing purposes.


#### Questions for Further Analysis
- If attendance remains constant despite increased email recipients, does this indicate that the attendees at ECHO sessions are circulating or are the sessions being attended consistently by the same audience?
- Do people forward our emails?
- How many people are estimated to "fall through the cracks" because we lack a stable/reliable CRM (customer relations manager)?

#### Projections
- What are the population sizes of Idaho healthcare professionals? At what point will ECHO Idaho have reached all the healthcare professionals it can?

