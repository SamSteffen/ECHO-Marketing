# ECHO Idaho Marketing Campaigns (2018-2021)
The following is a visualization project analyzing various Mail Chimp email marketing campaigns for a continuing education platform serving Idaho's rural healthcare workforce, using Python's pandas and matplotlib libraries.

## Overview
### ECHO Idaho Program Structure
ECHO Idaho is a free, virtual continuing education platform available for Idaho healthcare professionals. Housed at the University of Idaho, WWAMI Medical Education Program, the program is Idaho's only available chapter of the Extensions for Community Healthcare Outcomes organization, a global initiative intended to improve patient healthcare outcomes in rural and underserved communities through the democratization of expertise. The program is grant funded.

ECHO Idaho was initiated in 2018 with a single series focusing on Opioid and Addiction Treatment. Since its inception, the program has proliferated to span 10 different series on a variety of healthcare topics, and now has registered more than 3,000 unduplicated Idaho healthcare professionals in its community. Series typically offer hour-long sessions twice a month over the lunch-hour, Monday through Thursday. Each series features an interdisciplinary panel of experts who facilitate the conversation during each session; each session features a 20-30 minute didactic presentation as well as a real de-identified case presentation presented by a volunteer.

### How ECHO Idaho Uses Emails
For a free, virtual continuing education platform that conducts its web-based services primarily over Zoom teleconferencing software, email marketing is one of the primary ways that the program is able to reach new and existing audiences. Because ECHO Idaho is housed at the University of Idaho, ECHO Idaho's email marketing campaigns are bound by the same rules governing those of the University, which stipulate that emails originating from the University of Idaho can only be sent to individuals who have "opted in" to receive them. This "opt in" decision on the user-end is usually made during the registration process, via the ECHO Idaho website's registration page: https://www.uidaho.edu/academics/wwami/echo/register 
Once an individual has completed the registration for one or several ECHO series, their information is added to ECHO's mothership database, iECHO. iECHO stores data for all of ECHO Idaho's participants as well as all of the other ECHO programs, globally.

Completing registration prior to or following an ECHO session is NOT required to attend and participate in ECHO Idaho sessions. 

Until September of 2022, the University of Idaho utilized MailChimp as its primary email communications instrument. 

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
1. **iECHO**    
An ECHO program-specific online database where personal info (name, email, credential, workplace, residence, etc.) as well as series and session attendance records are stored;
2. **MailChimp**    
The University of Idaho's main communications system, which stores and preserves metrics fo each campaign such as: how many people received each email, how many times it was opened, how many times it was forwarded, how many links were clicked, etc.;
3. **eeds**    
An online platform where healthcare professionals are able to create and track continuing education credits earned for participation in ECHO Idaho and other event-based CE;
4. **SoundCloud**    
The host site of ECHO Idaho's CE-eligible podcast, *Something for the Pain*.

### Why Emails?
The purpose of this analysis is to bring these disparate data sources together to create visualizations for attendance and email data for each ECHO series and activity years (2018-2021). It is also to determine the following:
- The efficacy of daily email campaigns on program attendance (the relationship between email open-rates and session attendance).
- The efficacy of weekly email campaigns on program attendance (the realtionship between email open-rates and session attendance).
- What can be learned from the ECHO sessions with the best attendance and the type of email campaign that was used to promote it? 
- What can be learned from the ECHO sessions with the worst attendance and the type of email campaigns used to promote it?
- Using cumulative email and attendance data, establish a metric that can be used to determine successfull versus unsuccessful email campaigns for future marketing purposes.

## Results
To illustrate the impact of email campaigns on ECHO Idaho's series by attendance, it's important to state the various education series ECHO Idaho has hosted by program year. The following represents a dataframe showing 10 series, broken down by series name, launch-date and end-date:

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>

* Note that the several of the above series have continued beyond the listed "end-dates"; the iECHO attendance data is presented cumulatively at the end of the year; hence this data ends at the end of Dec. 2021.

### ECHO Series Offered by Year
#### 2018    
- Opioid Addiction and Treatment series (eventually became "Opioids, Pain and Substance Use 
       Disorders" in Jan. 2021, hereafter abbreviated "OPSUD")
- Behavioral Health in Primary Care series (hereafter abbreviated "BH in PC") 
- MAT Waiver Training (eventually renamed "X-Waiver Training", hereafter abbreviated "XWT")

#### 2019    
- OPSUD
- BH in PC
- XWT

#### 2020    
- OPSUD
- BH in PC
- XWT
- COVID-19 series (hereafter abbreviated "COVID")
- Syphilis in Pregnancy series (hereafter abbreviated "Syphilis")
- Perinatal Substance Use Disorder series (hereafter abbreviated "PSUD")
- COVID-19 Nursing-Home Safety series (eventually re-name COVID-19 Safety for Post-Acute and Long-Term Care facilities, hereafter abbreviated "PALTC")

#### 2021    
- OPSUD
- BH in PC
- XWT
- COVID
- PALTC
- PSUD
- Pediatric Behavioral Health (hereafter abbreviated "PBH")
- Hepatitis C (eventually renamed "Viral Hepatitis and Liver Care", hereafter abbreviated "VHLC")
- Counseling Techniques for Substance Use Disorders (herafter abbreviated "CTSUDs")

### 2018 Analysis

The barchart below shows the quantity of emails sent across ECHO series in 2018:

<img src="Visualizations/2018/Session_attendance_totals_2018.png" alt="df - Session Attendance Totals 2018" width="400"/>

<img src="Visualizations/2018/Email_campaigns_by_series_2018.png" alt="Email Campaigns by series 2018" width="400"/><img src="Visualizations/2018/Session_attendance_2018.png" alt="Session attendance 2018" width="400"/>

<img src="Visualizations/2018/Email_v_attendance_OPSUD_2018.png" alt="OPSUD Email v attendance 2018" width="400"/><img src="Visualizations/2018/Email_v_attendance_BH_in_PC_2018.png" alt="BH in PC Email v attendance 2018" width="400"/>

### 2019 Analysis

The barchart below shows the quantity of emails sent across ECHO series in 2019:

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2019/Email_campaigns_by_series_2019.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2019/Session_attendance_2019.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2019/Email_v_attendance_OPSUD_2019.png) 

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2019/Email_v_attendance_BH_in_PC_2019.png)


### 2020 Analysis

The barchart below shows the quantity of emails sent across ECHO series in 2020:

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_campaigns_by_series_2020.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Session_attendance_2020.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Session_attendance_2020_sans_outliars.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_BH_in_PC_2020.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_OPSUD_2020.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_COVID_2020.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_PALTC_2020.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_PSUD_2020.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2020/Email_v_attendance_Syphilis_2020.png)


### 2021 Analysis

The barchart below shows the quantity of emails sent across ECHO series in 2021:

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_campaigns_by_series_2021.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Session_attendance_2021.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_BH_in_PC_2021.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_OPSUD_2021.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_COVID_2021.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_PALTC_2021.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_PSUD_2021.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_CTSUDs_2021.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_PBH_2021.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/2021/Email_v_attendance_VHLC_2021.png)


### Cumulative Analysis (2018-2021)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_campaigns_by_series_2018-2022.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_OPSUD_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_BH_in_PC_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_COVID_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_PALTC_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_CTSUDs_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_PSUD_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_PBH_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_Syphilis_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Email_v_attendance_VHLC_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Net_attendance_growth_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/Net_attendance_growth_by_series_cumulative.png)

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/New_attendees_per_session_cumulative.png)  

<img src="Visualizations/Cumulative/Series_data_sessions_dates_cumulative.png" alt="df1" width="400"/>
![](Visualizations/Cumulative/New_attendees_by_series_cumulative.png)


### Summary
- The efficacy of daily email campaigns on program attendance (the relationship between email open-rates and session attendance).
- The efficacy of weekly email campaigns on program attendance (the realtionship between email open-rates and session attendance).
- What can be learned from the ECHO sessions with the best attendance and the type of email campaign that was used to promote it? 
- What can be learned from the ECHO sessions with the worst attendance and the type of email campaigns used to promote it?
- Using cumulative email and attendance data, establish a metric that can be used to determine successfull versus unsuccessful email campaigns for future marketing purposes.


#### Questions for Further Analysis
- Do people forward our emails?
- How many people are estimated to "fall through the cracks" because we lack a stable/reliable CRM (customer relations manager)?

#### Projections
- What are the population sizes of Idaho healthcare professionals? At what point will ECHO Idaho have reached all the healthcare professionals it can?

