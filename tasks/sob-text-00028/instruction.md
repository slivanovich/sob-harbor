Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
William P. Brooks House: The William P. Brooks House, also known as Brooks Hall, is a dormitory in Amherst, Massachusetts that is built in the georgian revival style with art deco accents.  It is named after former professor and president of Massachusetts Agricultural College William P. Brooks.  It is part of the Central Residential Area at the University of Massachusetts Amherst.  It was designed by Louis Ross, who designed many of the dormitories on campus as well as the Student Union.

Sen. William P. Jackson House: Sen. William P. Jackson House was a historic home located at Salisbury, Wicomico County, Maryland.  It was a 3 ⁄ -story Queen Anne frame house completed in 1893.  It was torn down in November 1976, after a ten-year battle to save it.  It was built by United States Senator William P. Jackson.

William P. Baker: William Pond Baker (born June 14, 1940, in Oakland, California) is a former United States Congressman from California.  He attended San Jose State University, from which he earned a business degree.  Baker served as a member of the United States Coast Guard reserve from 1957 to 1965.

Sen. William P. Frye House: The Senator William P. Frye House is a historic house on 453-461 Main Street in Lewiston, Maine.  Built in 1874, it is a fine example of Second Empire architecture in the city, designed by local architects Fassett & Stevens for William P. Frye, a mayor of Lewiston and a United States Senator.  The house was listed on the National Register of Historic Places in 1976.

Bart Baker: Baker went to film school at University of Miami.  After realizing the potential of YouTube, he started filming music videos in his backyard on a green screen.  Lonely Island was described as a 'big inspiration' to Baker when he first started.

William P. Hepburn House: The William P. Hepburn House is a historic house and National Historic Landmark at 321 West Lincoln Street in Clarinda, Iowa.  It was home to United States Congressman William P. Hepburn (1833-1916) from about 1867 until his death.  Hepburn most significantly introduced the Hepburn Act of 1906, which gave the Federal government the power to set railroad rates, and was an important precedent in Federal regulation of private industry.  The house was declared a National Historic Landmark in 1976.  It is a private residence, not generally open to the public.

Alfred Marmaduke Hobby: Alfred Marmaduke Hobby (1836 - February 5, 1881) was a famous Texas merchant, politician, Confederate officer, and poet.  He was born in Macon, Georgia, in 1836, the son of Martin and Anna Elizabeth (Slade) Hobby.  Hobby's nephew is William P. Hobby, governor of Texas from 1917 to 1921.  His grandnephew William P. Hobby, Jr., was lieutenant governor of Texas 1973-91.

William P. Connery Sr.: William P. Connery Sr. (September 1855 – November 1928) was a Massachusetts politician who served as the 34th Mayor of Lynn, Massachusetts.  He was the father of U.S. Congressional Representatives Lawrence J. Connery and William P. Connery, Jr.

San Jose State University: San José State University (commonly referred to as San Jose State or SJSU) is a comprehensive public university located in San Jose, California, United States.  It is the founding school of the 23-campus California State University (CSU) system, and holds the distinction of being the oldest public institution of higher education on the West Coast of the United States.

William P. Hobby Unit: The William P. Hobby Unit (HB) is a prison for women in unincorporated Falls County, Texas.  Named after William P. Hobby, Lieutenant Governor of Texas, it is a part of the Texas Department of Criminal Justice (TDCJ).  It is located on Texas Farm to Market Road 712, off Texas Business Highway 6 and 6 mi southwest of Marlin.

Question: The university that William P. Baker went to is the founding school of what system?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "university_attended": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university the person attended."
        },
        "location": {
          "type": "string",
          "description": "The city and state where the university is located."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "founding_system": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university system the university is the founding school of."
        },
        "campus_count": {
          "type": "integer",
          "description": "The number of campuses in the university system."
        }
      },
      "required": [
        "name",
        "campus_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "university_attended",
    "founding_system"
  ],
  "additionalProperties": false
}
