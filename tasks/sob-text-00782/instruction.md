{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWinslow Township High School: Winslow Township High School (WTHS) is a four-year comprehensive public high school in Winslow Township, in Camden County, New Jersey, United States, that serves students in ninth through twelfth grades as the lone secondary school of the Winslow Township School District.  Until 2000, the facility that is now Winslow Township High School was part of the Lower Camden County Regional School District and was known as Edgewood Regional High School, which was the sister school of Overbook Regional Senior High School in Pine Hill (now known as Overbrook High School).\n\nPresbyterian Boys' Senior High School: Presbyterian Boys' Secondary School (or PRESEC) is a secondary school for boys, founded in 1938, under the auspices of the Presbyterian Church of the Gold Coast.  The progenitor of the school was the Basel missionary, The Reverend Nicholas Timothy Clerk.  The school has ties with its sister school, Aburi Girls' Senior High School.\n\nReverend Juuso Shikongo Senior Secondary School: Reverend Juuso Shikongo Senior Secondary School is a Namibian public school in the Omuntele Constituency in the Oshikoto Region about 60 kilometres southeast of Ondangwa, which was in 2013 inaugurated by then Education Minister Dr David Namwandi.  The school is named after the founder of the Evangelical Lutheran Church in Namibia 's Omuntele congregation, Reverend Juuso Shikongo, the school started operating from a sister school, Uukule Senior Secondary School situated at Onyaanya Constituency some 30 kilometres away, in 2011 before moving to Omuntele at the beginning of the year 2013.  In his official inauguration address, the education minister David Namwandi pointed out that Government has spent N$120 million (Namibian Dollars) on the construction of classrooms, offices and hostels for the school.\n\nCarle Place, New York: Carle Place is a hamlet and census-designated place (CDP) in the Town of North Hempstead in Nassau County, New York, United States.  The CDP's population was 4,981 at the 2010 census.\n\nIshibu Higher Secondary School: Ishibu Higher Secondary School (Nepali: ईसिवू उचच माधयमिक विधालय ) is a community school under government of Nepal located at the point of ishibu vdc ward no.4 in Terathum district of Nepal. It is established in 1960 A.D in the fundamental of primary school and it has been upgraded adding high school & later in 5–7 years ago it has risen as higher secondary school.Since it is situated on the lap of the Himalayas, it has automatically a panoramic environment of nature where the atmosphere is cool and favorable for students.  In the past time its educating system was in old system where there was everything lack needed for studies and teachers were used to regard as god like and it was quite rigorous management of school therefore, students were forced to study with hard labour memorising by heart.Teaching was lecture based method so that there was rare practical education.  But now education system has also been change along with changes of time.It has a modern fashioned library and it is equipped with sufficient halls for seating of students.  Head of school is thought to be Principal or headmaster and the former principal was Mr.Mahesh Niraula whereas the current Principal is Mr. Ram Prasad Timsina.Since it is a government school it has not any sister school however few name of schools may come with the same name but they are distinguished by location.\n\nJ. Sterling Morton High School East: J. Sterling Morton High School East (often called \"Morton East\") is a public secondary school located in Cicero, Illinois.  Morton East is one of three schools in J. Sterling Morton High School District 201.  Morton East is a sophomore through senior building, with future students attending the \"J. Sterling Morton Freshman Center\" for one year.  Morton East's sister school, J. Sterling Morton High School West is a four-year secondary school.\n\nBaldwin Senior High School (New York): Baldwin High School is a public secondary school located in Baldwin, Nassau County, New York.  The school serves students in grades 9 to 12 in the Baldwin Union Free School District.  It is the eighth largest in Nassau County.\n\nLegae Academy: Legae Academy is an English medium, independent, co-educational, secondary school located in Gaborone, Botswana.  The academy is a sister school to Legae English Medium Primary School which was established in 1983.  The academy follows the Cambridge International Examinations syllabus, allowing students to sit for the International General Certificate of Secondary Education (IGCSE) after four years of secondary education, and the A-Level examination after a further two years.Legae academy is the best school for Cambridge in not only Botswana but Southern africa itself\n\nEast Rockaway High School: East Rockaway Junior-Senior High School (often abbreviated ERHS) is a co-educational six-year secondary school in East Rockaway, New York, and the sole high school in Nassau County, New York, School District 41 (East Rockaway School District), the smallest school district in Nassau County.  It is currently undergoing renovations to expand the school into a middle school and high school, becoming a seven-year secondary school.  East Rockaway High School serves graduates from local Centre Ave. and Rhame Ave. Elementary Schools, as well as the private St. Raymond Elementary School.\n\nSingwango Secondary School: Singwango Secondary School is located in Filabusi, Matabeleland South Province, Zimbabwe.  It had a sister school in Carle Place, New York, United States, although Carle Place High School still donates sports equipment and clothes.\n\nQuestion: Which Nassau County hamlet is home to the sister school of Singwango Secondary School?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"hamlet_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the hamlet where the sister school is located.\"\n    },\n    \"county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the hamlet is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the hamlet is located.\"\n    },\n    \"country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the hamlet is located.\"\n    },\n    \"sister_school_relationship_status\": {\n      \"type\": \"string\",\n      \"description\": \"Details about the current status of the sister school relationship.\"\n    }\n  },\n  \"required\": [\n    \"hamlet_name\",\n    \"county\",\n    \"state\",\n    \"country\",\n    \"sister_school_relationship_status\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "hamlet_name": {
        "type": "string",
        "description": "The name of the hamlet where the sister school is located."
      },
      "county": {
        "type": "string",
        "description": "The county where the hamlet is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the hamlet is located."
      },
      "country": {
        "type": "string",
        "description": "The country where the hamlet is located."
      },
      "sister_school_relationship_status": {
        "type": "string",
        "description": "Details about the current status of the sister school relationship."
      }
    },
    "required": [
      "hamlet_name",
      "county",
      "state",
      "country",
      "sister_school_relationship_status"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
