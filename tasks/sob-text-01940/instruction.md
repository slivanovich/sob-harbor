{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSalvageData: SALVAGEDATA Recovery is a GSA, certified data recovery services and software tools firm to undergo yearly ISO 9001:2008 quality control reviews.  The company helps individual, business and government customers recover from computer and electronic data loss situations.\n\nEVault: EVault is a part of Carbonite, and a distinguished brand name for some of Carbonite's product offerings.  EVault and its partner network develop and support on-premises, cloud-based, and hybrid backup and recovery services for midmarket customers in need of data backup, data recovery, disaster recovery, regulatory compliance, and cloud storage or online backup services.  The company primarily services customers in heavily regulated industries—financial services, legal, health care—as well as in government, education, telecommunications, and charity/nonprofit.  Headquartered in Boston, Massachusetts, United States, the company has sales, service, and data center operations in North America and EMEA (Europe, the Middle East and Africa).\n\nGeorge Soulis: George Soulis (born February 19, 1976) is a Greek Canadian, data recovery specialist, baseball player and entrepreneur.  He is the founder and CEO of DataRecall International Data Recovery Services. DataRecall International is based in Athens Greece, and holds offices in Munich, Germany and Montreal, Quebec.\n\nDun &amp; Bradstreet: Dun & Bradstreet, Inc. () is a company that provides commercial data, analytics and insights for business, headquartered in Short Hills, a community in Millburn, New Jersey, US.  It offers a wide range of products, and services for risk and finance, operations and supply, and sales and marketing professionals, as well as research and insights on global business issues, serving customers in government and industries such as communications, technology, strategic financial services, and retail/telecommunications/manufacturing markets.  Often referred to as D&B, the company’s database contains more than 265 million business records worldwide.\n\nAxcient: Axcient, Inc is a Mountain View, California company which provides Recovery-as-a-Service (RaaS) for businesses to protect their data and applications.  Axcient's platform manages data backup, data recovery, disaster recovery, regulatory compliance, cloud storage, online backup and granular data recovery from a single web based service to eliminate data loss for small to large businesses.\n\nSándor Kürti: Dr. Sándor Kürti (born 1947) graduated in 1971 from the University of Veszprem (Hungary) on the faculty of Chemistry Process Automation.  In 1975 he obtained diploma in system manager engineering, and received doctor’s degree from mathematical statistical analysis.  After his graduation he worked for the Danubian Oil Refinery.  His fields were: implementation of computer control system at gasoline mixing unit, design of the process control system of a catalic crack plant.  Later on he joined the International Research Institute MNIIPU (Moscow, SU) where he dealt with mathematical simulation of blending systems.  Working for Honeywell, (Bracknell, UK) he simulated process control system of a catalytic crack plant.  In 1989 he founded .  KÜRT developed a hard disk repair technology, a world-renowned data recovery technology, as well as IT security technology and methodology.  He was awarded Kalmar Laszlo Award for the data recovery technology in 1995, Information Technology Manager of the Year in 1997, 1998, Gabor Denes Award for Innovation in 1998.  He is vice president of IVSZ (Hungarian Association of IT Companies).  In 2004 he was decorated with the Széchenyi Prize for his exceptionally high standard, exemplary, internationally acknowledged accomplishments.  He has been elected as a member of the Stakeholder Group of the European Union's data security organization (ENISA).  In 2005 he was given Ernst & Young “Entrepreneur Of The Year 2004” international business award for his creativity, for his personal contribution to the accomplishment of innovative ideas, and his success in creating a model organizational culture at KÜRT Co.  The KÜRT Co. received the ‘Family Friendly Workplace Prize 2005’ in the medium-sized enterprises category.  In 2006 Dr. Sándor Kürti was the first representative of the Hungarian business community to participate in selecting the world’s best entrepreneur at The “World Entrepreneur Of The Year” contest organised by Ernst&Young.  In 2007 he was given the Pro Information Technology Award by the Hungarian Association of IT Companies.\n\nDriveSavers: In 1985 former Jasmine Technologies executives Jay Hagan and Scott Gaidano founded DriveSavers, operating from Gaidano’s condo with $1,400.  DriveSavers originally offered both hard drive repair and data recovery services, but the company dropped its drive repair services within its first eight months.  In 1992, DriveSavers signed an agreement with SuperMac Technology to assume technical support and warranty obligations for SuperMac Mass Storage Products.\n\nWandera: Wandera is a privately held company backed by Bessemer Venture Partners and 83North Venture Capital.  The SaaS service provides customers with a Secure Mobile Gateway (SMG) which compresses mobile data, enforces acceptable usage policies, provides multi-level mobile threat detection by scanning on device and in the cloud, and provides data usage reporting to business organizations to help protect business data.\n\nOnavo: Onavo, a mobile analytics company based in Israel, is the developer of Onavo Insights and Onavo Mobility apps.  The app provides information for users on <ref name=\"Onavo Extend for iPhone/iPad\"> </ref> data usage and compression of data, as well as mobile data protection.  Onavo Insights provides data to companies about app usage and consumer trends in online gaming, social networking, finance, and entertainment.\n\nSecureDataRecovery: Secure Data Recovery Services is a privately held company with corporate headquarters in California, which provides data recovery services.  Secure Data Recovery Services was the first data recovery company to achieve certification.  The SSAE 16 Type II Certification is an updated version of the , which the company had also previously held.  SSAE 16 reports (also known as \"SOC 1\" reports) retain the original purpose of SAS 70 by providing a means of reporting on the system of internal control particularly as it relates to internal control over financial reporting (ICFR).  It is also the only company in the data recovery industry to have a certified Class 10 ISO 4 Cleanroom.  They are also certified to perform data recovery by Hitachi, Seagate, IBM, Toshiba, Maxtor, Fujitsu, Lacie, and other hard drive manufacturers.  They are a Dun & Bradstreet D-U-N-S listed company.\n\nQuestion: Secure Data Recovery Services is a privately held company with corporate headquarters in California, which provides data recovery services, and are a listed company on which company that provides commercial data, analytics and insights for business, headquartered in Short Hills, a community in Millburn, New Jersey, US?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"listed_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company Secure Data Recovery Services is listed on.\"\n    },\n    \"listed_company_headquarters\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"state\": {\n          \"type\": \"string\"\n        },\n        \"country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"listed_company_services_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the services provided by the listed company.\"\n    },\n    \"secure_data_recovery_is_privately_held\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if Secure Data Recovery Services is a privately held company.\"\n    }\n  },\n  \"required\": [\n    \"listed_company_name\",\n    \"listed_company_headquarters\",\n    \"listed_company_services_description\",\n    \"secure_data_recovery_is_privately_held\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "listed_company_name": {
        "type": "string",
        "description": "The name of the company Secure Data Recovery Services is listed on."
      },
      "listed_company_headquarters": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "listed_company_services_description": {
        "type": "string",
        "description": "A description of the services provided by the listed company."
      },
      "secure_data_recovery_is_privately_held": {
        "type": "boolean",
        "description": "Indicates if Secure Data Recovery Services is a privately held company."
      }
    },
    "required": [
      "listed_company_name",
      "listed_company_headquarters",
      "listed_company_services_description",
      "secure_data_recovery_is_privately_held"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
