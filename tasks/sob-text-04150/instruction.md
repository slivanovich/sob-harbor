{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Departed (band): The Departed (also known as Cody Canada and the Departed) is an American Alternative rock/alternative country band.  The band was formed by Cross Canadian Ragweed frontman Cody Canada after Ragweed broke up in 2010.  Canada’s longtime bassist Jeremy Plato followed and joined guitarist/vocalist Seth James, keyboard player Steve Littleton, and Drummer Dave Bowen.  Chris Doege would eventually replace Bowen on drums.  In December 2014, Littleton and Doege left the band.  Drummer Eric Hansen and keyboardist / rhythm guitarist Ross Smith was with the group from 2015-2017.\n\nCody High School (Wyoming): Cody High School is a school in Cody, Wyoming, United States.  It is part of Park County School District #6.  Cody has a population of about 9,000 people, and the school has approximately 570 students.  The school mascots are the broncs and fillies, and the colors are blue and gold.  The school is the long-time rival of Powell High School.\n\nRichard Hodges (surgeon): Richard Manning Hodges (November 6, 1827 – February 9, 1896) was an American surgeon.  He is known for publishing a work on surgical joint excisions, an account of the first use of ether for surgical anesthesia, and for naming the pilonidal sinus.  Hodges graduated from Harvard College in 1847, and from Harvard Medical School in 1850.  He first served as a demonstrator in anatomy at the medical school and then as a visiting surgeon and adjunct professor of surgery at Massachusetts General Hospital.  He was a friend and student of Henry Jacob Bigelow and was a member of the Harvard Board of Overseers, and of the Boston Society for Medical Improvement.\n\nCody Fajardo: Cody Michael Fajardo (born March 29, 1992) is a Canadian football quarterback for the Toronto Argonauts of the Canadian Football League (CFL).  He played college football at the University of Nevada, Reno and was the Wolf Pack's starting quarterback from 2011 to 2014.  He won the Glenn Davis Award in 2009 as the best high school football player in California.  Cody is of Spanish American descent.  Cody accounted for 13,000+ yards and 101 touchdowns in his career at Nevada.  He ran his first professional touchdown on 7/13/16 and threw his first professional touchdown on 7/25/16 both for the Toronto Argonauts of the CFL.\n\nCody Votolato: Cody Votolato (born May 20, 1982) is a musician from Redmond, Washington, best known for being the guitarist in the post-hardcore band The Blood Brothers.  He grew up in the eastside suburbs of Seattle.  Cody attended Redmond High School with his bandmates in the late 1990s when the band originally formed, graduating Spring of 2000.  His accomplished thrashy and discordant style, exhibited in early Blood Brothers albums and in Head Wound City, has evolved into a more melodic and experimental sound in recent years .  Votolato's older brother Rocky Votolato is a folk musician and solo artist who played in the band Waxwing with his brother, as well as with Rudy Gajadhar, the older brother of The Blood Brothers' drummer Mark Gajadhar.  Votolato also contributed artwork to The Blood Brothers' album \"...Burn, Piano Island, Burn\".  On September 4, 2012, it was announced that Cody has joined Cold Cave as touring guitarist.\n\nCody Hodges: Cody Hodges (born November 20, 1982) is a philanthropist, motivational speaker, and former professional American football player, playing in the National Football League, Arena Football League, and the Arena League 2.  Hodges is best known for his one season as the starting quarterback for the Texas Tech Red Raiders during the 2005 season.  As a fifth year Senior, he led the nation in passing and total offense and an appearance in the 2006 Cotton Bowl Classic and a 9–3 overall record.  He was the 3rd straight fifth year senior to start for Mike Leach and Texas Tech and was also the second of 4 West Texas natives to take the quarterback reins in the Leach era, along with predecessor Sonny Cumbie and successors Taylor Potts and Seth Doege.\n\nSeth Cohen: Seth Ezekiel Cohen is a fictional character on the FOX television series \"The O.C.\", portrayed by Adam Brody.  Seth is one of the \"core four\" characters on \"The O.C.\" alongside Ryan Atwood, Marissa Cooper, and Summer Roberts.  Seth's friendship with Ryan, who eventually became his adoptive brother, formed a focal point of the series along with their romances.  Seth married Summer in the series finale.  His other relationships were with Anna Stern and Alex Kelly.  Seth's goal was to attend Brown University, but he ends up going to Rhode Island School of Design (RISD) and continuing work on his comic book \"Atomic County\".  The role saw Brody win four Teen Choice Awards from five nominations, from 2004 to 2006.\n\nSeth Doege: Seth Colton Doege (born December 18, 1988) is an American football coach and formerly professional Canadian football quarterback.  After playing college football for Texas Tech University, he was signed by the Atlanta Falcons as an undrafted free agent in 2013.  On February 27, 2014, he was signed to the Saskatchewan Roughriders of the Canadian Football League.  Doege was Texas Tech's starting quarterback for the 2011 and 2012 seasons.  He is currently the wide receivers coach for Bowling Green.\n\nHodges Business College: Hodges Business College, also known as Hodges School, is a historic school building located near Mocksville, Davie County, North Carolina.  It was built in 1894, and is a two-story, rectangular, Gothic Revival style brick building.  It features multiple Gothic-arched window openings and front entrance.  The building housed a school into the 1910s, then was converted to tenant house, and after 1936 used for storage.  The building was converted to a residence in the 1990s.\n\nCody Canada: Cody Jay Canada (born May 25, 1976 in Pampa, Texas) is an American southern rock/alt-country artist.  From 1994-2010, Canada was the lead singer of Cross Canadian Ragweed.  In 2011, Canada founded the group The Departed with Jeremy Plato, Seth James, Steve Littleton and Chris Doege.\n\nQuestion: What school did Cody Hodges and Seth Doege have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the individuals mentioned in the question.\"\n    },\n    \"common_school\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the school that both individuals attended.\"\n    },\n    \"school_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of educational institution (e.g., University, High School).\"\n    },\n    \"roles_at_school\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"person_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the person.\"\n          },\n          \"role\": {\n            \"type\": \"string\",\n            \"description\": \"The role the person had at the school (e.g., starting quarterback, student).\"\n          },\n          \"years_active\": {\n            \"type\": \"string\",\n            \"description\": \"The years the person was active in that role at the school.\"\n          }\n        },\n        \"required\": [\n          \"person_name\",\n          \"role\",\n          \"years_active\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details about each person's role and tenure at the common school.\"\n    }\n  },\n  \"required\": [\n    \"person_names\",\n    \"common_school\",\n    \"school_type\",\n    \"roles_at_school\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the individuals mentioned in the question."
      },
      "common_school": {
        "type": "string",
        "description": "The name of the school that both individuals attended."
      },
      "school_type": {
        "type": "string",
        "description": "The type of educational institution (e.g., University, High School)."
      },
      "roles_at_school": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "person_name": {
              "type": "string",
              "description": "The name of the person."
            },
            "role": {
              "type": "string",
              "description": "The role the person had at the school (e.g., starting quarterback, student)."
            },
            "years_active": {
              "type": "string",
              "description": "The years the person was active in that role at the school."
            }
          },
          "required": [
            "person_name",
            "role",
            "years_active"
          ],
          "additionalProperties": false
        },
        "description": "Details about each person's role and tenure at the common school."
      }
    },
    "required": [
      "person_names",
      "common_school",
      "school_type",
      "roles_at_school"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
