{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nColby Community College: Colby Community College (CCC) is a two-year community college located in Colby, Kansas, United States.  Established in 1964, the 80 acre main campus is located in the heart of Colby with an additional 64 acre agricultural center east of the city.\n\nSafe House (2012 film): Safe House is a 2012 American spy action-thriller film directed by Daniel Espinosa, starring Denzel Washington and Ryan Reynolds.  The film follows Matt Weston (Reynolds), a CIA agent on his first low-level posting in Cape Town who is in charge of a safe house where the CIA is interrogating Tobin Frost (Washington), a veteran operative who has allegedly betrayed the agency.  When the safe house is attacked by mercenaries who kill almost all the agents, Weston flees with Frost in his charge, and they end up on the run.  As the team of killers, who seem to be one step ahead of the pair, track them throughout Cape Town, Weston begins to wonder whom to trust.\n\nIrma Carrillo Ramirez: Ramirez was born in 1964.  She received a Bachelor of Arts degree in 1986 from the West Texas A&M University.  She received a Juris Doctor in 1991 from the Southern Methodist University Dedman School of Law.  Judge Ramirez began her legal career working as an associate for the law firm Locke Purnell Rain Harrell, PC (now Locke Lord LLP) from 1991 to 1995.  She served as an Assistant United States Attorney for the United States Attorney’s Office for the Northern District of Texas, working in the Civil Division from 1995 to 1999 and the Criminal Division from 1999 to 2002.\n\nSumie Inagaki: Sumie Inagaki (稲垣寿美恵 , Inagaki Sumie , born 6 April 1966) is a Japanese ultramarathon runner from Hokkaido.  Inagaki holds current women's world record in 24-hour run Indoor (240.631 km , Espoo FIN, Jan 2011), and in 48-hour run Track (397.103 km , Surgeres FRA, May 2010).  She is a two time female winner of IAU 24-Hour Run World Championship.  She was the female winner of 2006 and 2009 Spartathlon, and the female winner of 2011 and 2012 Badwater Ultramarathon.\n\nSPNRC High School: SPNRC High School (Sri Posani Narasimha Rao Choudari High School, Telugu:శ్రీ పోసాని నరసింహారావు చౌదరి ఉన్నత పాఠశాల) is a co-educational aided secondary school.  It was established on 12 August 1964 in Gollapudi beside the National Highway 9, India.  It is one of the oldest schools in Vijayawada.  The school was established on 12 August 1964 for VI and VII classes with 140 pupils and 3 teachers.  In 1965-66 the school was upgraded to VIII class.  In 1966-67 the school was further upgraded to open IV form.  In 1967-68, permission was granted to open old V form and new IX class.  In 1968-69, permission was accorded for opening of New X class and old SSLC.\n\nPolly Plumer: Polly Anne Plumer was the National High School record holder in the Mile run at 4:35.24, set in open competition at UCLA May 16, 1982 while a student at University High School (Irvine, California).  That distance is no longer run in high school competition since the NFHS converted to metric distances in 1980, but it is still an international record event.  Her record lasted over 30 years until it was surpassed on January 26, 2013 by Mary Cain, indoors, running 4:32.78 at the New Balance Games.  Cain later improved her own mark to 4:28.25, also indoors at the Millrose Games.  Because Cain's marks were set on an indoor track, which is generally considered to be more difficult, they were not recognized by \"Track and Field News\" the ratifier of high school records in non-NFHS sanctioned events (high school athletes in open competition), so Plumer retains the record as published.  Christine Babcock, born 8 years and 3 days after Plummer's record, running for Woodbridge High School, also in Irvine, took the record in the more commonly run but shorter 1600 meters to an equitable 4:33.82 in 2008.  Babcock's record was improved to 4:33.29 in 2014 by Alexa Efraimson.\n\nBirch Run High School: Birch Run High School is a public high school located at 12450 Church Street in Birch Run, Michigan and part of the Birch Run Area Schools district.  Birch Run's mascot is the panther, and its colors are blue and gold.  The school's athletic program competes in the Tri-Valley Conference-East as a Class B school.  Its team sports include baseball, basketball, bowling, cheerleading, cross country running, football, golf, powerlifting, soccer, softball, track and field, volleyball, wrestling.\n\nFike Recreation Center: Fike Recreation Center, originally known as Clemson Field House, is an on-campus recreation facility at Clemson University in Clemson, South Carolina.  It houses several gymnasiums, a pool, a fitness atrium, racquetball courts, an indoor walk/jog/run track, and a climbing wall.  The basketball team played there from 1930 to 1968, when Littlejohn Coliseum opened.\n\nMichael Norman (sprinter): Michael Norman, Jr. (born December 3, 1997) is an American track and field athlete who competes in the 100 meters, 200 meters, and 400 meters.  He graduated from Vista Murrieta High School in Murrieta, California in 2016.  He currently attends University of Southern California.  He broke the NFHS record in the 400 meters with a time of 45.19 seconds at the 2015 CIF California State Meet held at Buchanan High School in Clovis, California on June 6, 2015.  His time is the fastest 400 meters run by a U.S. high school athlete against other high school-aged athletes, along with Aldrich Bailey who also ran 45.19 seconds in Lubbock, Texas on April 28, 2012.  The time, however, is not the fastest 400 meters ever run by a U.S. high school-aged athlete according to the List of United States High School National Records in Track and Field.  The time of 44.69 seconds set by Darrell Robinson is the fastest.  However, it was set at a non-NFHS sanctioned meet, therefore only being acknowledged as a National Record by Track & Field News.  Norman's NFHS record is currently awaiting NFHS ratification.  On June 30, 2015, Norman was named the Gatorade Player of the Year for his achievements in Track and Field.  He is only the 2nd non-senior to win the Gatorade Player of the Year award in the 30-year history of the program and the first male sprinter to win the honors as a non-senior.\n\nDenzel Ramirez: Denzel Ramirez (born 22 December 1983) is a long-distance runner.  He represented Trinidad and Tobago at the 2005 Central American and Caribbean Championships and the 2006 Central American and Caribbean Games.  He ran track with Colby Community College and Troy University.\n\nQuestion: What school did Denzel Ramirez run track for that was established in 1964?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person in question.\"\n    },\n    \"activity\": {\n      \"type\": \"string\",\n      \"description\": \"The activity the person participated in.\"\n    },\n    \"school_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"school_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the school.\"\n        },\n        \"establishment_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the school was established.\"\n        }\n      },\n      \"required\": [\n        \"school_name\",\n        \"establishment_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the school that meets the criteria.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"activity\",\n    \"school_details\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person in question."
      },
      "activity": {
        "type": "string",
        "description": "The activity the person participated in."
      },
      "school_details": {
        "type": "object",
        "properties": {
          "school_name": {
            "type": "string",
            "description": "The name of the school."
          },
          "establishment_year": {
            "type": "integer",
            "description": "The year the school was established."
          }
        },
        "required": [
          "school_name",
          "establishment_year"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The name of the school that meets the criteria."
      }
    },
    "required": [
      "person_name",
      "activity",
      "school_details",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
