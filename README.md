# AutoEvent: DroidRun-Based Event Promotion Agent 🚀

AutoEvent is an intelligent mobile automation agent built on the **DroidRun** framework. It automates the tedious process of event outreach by bridging Google Sheets and WhatsApp using LLM-powered navigation.

## 📱 Project Overview
This agent performs an end-to-end automation loop:
1.  **Data Extraction:** Opens Google Sheets and navigates to the designated event spreadsheet.
2.  **Contact Parsing:** Reads lead names sequentially.
3.  **Personalized Outreach:** Switches to WhatsApp, searches for the contact, and sends a customized promotion message then waits for 3 seconds to prevent the spam detection.
4.  **Looping:** Automatically returns to the sheet to process the next entry until the list is complete.

## 🛠️ Tech Stack
* **Framework:** [DroidRun]
* **AI Engine:** Gemini 2.5 Flash(via Google Generative AI)
* **Language:** Python 3.12.10
* **Communication:** ADB (Android Debug Bridge)
* **Target Apps:** Google Sheets, WhatsApp

## ⚙️ Setup & Installation

### 1. Prerequisites
* Android device with **Developer Options** and **USB Debugging** enabled.
* The **DroidRun Portal** accessibility service active on the device.
* Google Sheets app logged in with access to your promotion list.

 ## Problem solved
* It automats the work of event promotion which is boring to do for multiple contacts.
* It waits 3 seconds for each message to prevent the risk of spam detection.
