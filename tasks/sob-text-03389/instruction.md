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
Zulima Farber: Zulima Farber (born 1944) is the former Attorney General of New Jersey and the first Latina (Cuban) to serve as Acting Governor of New Jersey.  She was appointed Attorney General in 2006 by Governor Jon Corzine and resigned on August 31, 2006.  She was succeeded by First Assistant Attorney General Anne Milgram on an interim basis until Stuart Rabner took office on September 26, 2006.

Peter C. Harvey: Peter C. Harvey was the first African American to serve as New Jersey Attorney General.  Harvey was appointed by New Jersey Governor Jim McGreevey as Acting Attorney General on February 15, 2003, and was confirmed by the New Jersey Senate as Attorney General on June 16, 2003.  Harvey served until 2006, when he was succeeded by Zulima Farber.  Following his resignation as Attorney General, he became a Partner in the New York City law office of Patterson, Belknap, Webb, and Tyler.

Frank S. Katzenbach: Frank Snowden Katzenbach, Jr. (November 5, 1868 – March 13, 1929) was an American jurist and Democratic party politician from New Jersey.  He was an Associate Justice of the New Jersey Supreme Court and was the Democratic nominee for Governor of New Jersey in 1907.  He was the brother of New Jersey Attorney General Edward L. Katzenbach and uncle of Nicholas Katzenbach, the United States Attorney General.

David Samson (lawyer): David Samson (born August 14, 1939) is an American lawyer and convicted felon who served as New Jersey Attorney General under Democrat Governor Jim McGreevey from 2002 to 2003.  He served as the Chairman of the Port Authority of New York and New Jersey (PANYNJ) from 2011 until his resignation on March 28, 2014 in the aftermath of the Fort Lee lane closure scandal.  Samson is a partner and founding member of the law firm Wolff & Samson from which he resigned in April 2015, and had been an ally of Governor Chris Christie.

Golan Cipel: Golan Cipel (born 1968) is an Israeli consultant most known for his relationship with former New Jersey Governor Jim McGreevey.

New Jersey Attorney General: The attorney general of New Jersey is a member of the executive cabinet of the state and oversees the Department of Law and Public Safety.  The office is appointed by the Governor of New Jersey, confirmed by the New Jersey Senate, and term limited.  Under the provisions of the New Jersey State Constitution, the Attorney General serves a concurrent four-year term to the governor.

Jim McGreevey: James Edward McGreevey (born August 6, 1957) is an American politician and member of the Democratic Party, who served as the 52nd Governor of New Jersey from 2002 until his resignation in 2004.  He was also a seminarian.  He served in the New Jersey General Assembly from 1990 to 1992, as the Mayor of Woodbridge Township from 1991 to 2002 and in the New Jersey Senate from 1994 to 1998.  He was the Democratic nominee for Governor of New Jersey in 1997 but was narrowly defeated by Republican incumbent Christine Todd Whitman.  He ran again in 2001 and was elected by a large margin.

Cara Rodriguez: Cara Rodriguez (born June 24, 1976) is an American attorney and politician who was the acting Attorney General of Oklahoma for a period of several days in February 2017.  She took office after former attorney general Scott Pruitt resigned to take office as Administrator of the Environmental Protection Agency.  Prior to her tenure as acting attorney general, Rodriguez served as General Counsel to Attorney General Pruitt, assistant solicitor general, and first assistant attorney general.  She attended Tulane University for her bachelor's degree and University of Oklahoma Law School for her Juris Doctor.

Elections in New Jersey: Elections in New Jersey are authorized under Article II of the New Jersey State Constitution, which establishes elections for the governor, the lieutenant governor, and members of the New Jersey Legislature.  Elections are regulated under state law, Title 19.  The office of the New Jersey Secretary of State has a Division of Elections that oversees the execution of elections under state law (This used to be the New Jersey Attorney General).  In addition, the New Jersey Election Law Enforcement Commission (ELEC) is responsible for administering campaign financing and lobbying disclosure.

John Jay Hoffman: John Hoffman was Acting Attorney General of the State of New Jersey.  He served from 2013 to 2016, longer than any other Acting Attorney General in the State's history.

Question: Peter C. Harvey was the first African American to serve as New Jersey Attorney General, Harvey was appointed by  New Jersey Governor Jim McGreevey as Acting Attorney General, on what date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "attorney_general_name": {
      "type": "string",
      "description": "The name of the Attorney General."
    },
    "appointment_details": {
      "type": "object",
      "properties": {
        "role_type": {
          "type": "string",
          "description": "The specific role appointed, e.g., 'Acting Attorney General' or 'Attorney General'."
        },
        "appointing_governor": {
          "type": "string",
          "description": "The name of the Governor who made the appointment."
        },
        "appointment_date": {
          "type": "string",
          "description": "The date of the appointment."
        }
      },
      "required": [
        "role_type",
        "appointing_governor",
        "appointment_date"
      ],
      "additionalProperties": false
    },
    "historical_significance": {
      "type": "object",
      "properties": {
        "is_first_african_american": {
          "type": "boolean",
          "description": "Indicates if the person was the first African American to hold the office."
        },
        "office_held": {
          "type": "string",
          "description": "The specific office for which the historical significance applies."
        }
      },
      "required": [
        "is_first_african_american",
        "office_held"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "attorney_general_name",
    "appointment_details",
    "historical_significance"
  ],
  "additionalProperties": false
}
