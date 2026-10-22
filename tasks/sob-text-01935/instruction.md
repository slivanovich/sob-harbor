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
Gardnerville Branch Jail: The Gardnerville Branch Jail is a historic jail located at 1440 Courthouse St. in Gardnerville, Nevada.  The jail was built in 1910 and served as Douglas County's only jail from 1910 to 1915.  Prior to 1910, the only county jail was in Genoa, the county seat; however, since Gardnerville was several miles from Genoa, it resorted to housing prisoners in the local judge's granary.  As the granary was considered unfit for holding prisoners, the community petitioned the county to construct a new jail.  However, local leaders in Minden, who wanted to move the county seat to their town, protested the move, as they suspected that Gardnerville was attempting to claim the county seat itself.  Nonetheless, the county approved the construction of the new jail.  The jail housed its first prisoners before construction even finished, as the Genoa jail burned down; one prisoner was briefly chained to a post until the new jail could accommodate him.  Once completed, the jail served the county until 1915, when Minden became the county seat and opened its own county jail.

Frank Pawlowski: Frank E. Pawlowski was the State Police Commissioner for the Pennsylvania State Police.

Jeffrey B. Miller: Jeffrey B. Miller, AA, BS, MPA, was the former commissioner of the Pennsylvania State Police.  Miller, a native of Harrisburg, Pennsylvania, served in that position from March 24, 2003, after being confirmed by the Pennsylvania State Senate, until August 8, 2008.

Illinois State Police: The Illinois State Police (ISP) is the state police force of Illinois.  Officially established in 1922, the Illinois State Police have over 3,000 personnel and 21 districts.  The main facilities of the Illinois State Police Academy, which were constructed in 1968, are located in Springfield.  Prior to 1968, training was conducted at the Illinois State Fairgrounds.  ISP also maintains the Illinois sex offender registry, administers the state's AMBER Alert program, and issues Illinois Firearm Owner Identification Cards (FOID) and Concealed Carry Licenses.  The Illinois State Police is also responsible for driving and physically protecting the Governor of Illinois.  In 2005, officers and duties of the Illinois Department of Central Management Services Police were merged into the Illinois State Police.

John Charles Groome (Pennsylvania): John Charles Groome (March 20, 1862 – August 31, 1930), was the first commissioner of the Pennsylvania State Police from 1905 to 1917.  He was the former warden of the Eastern State Penitentiary and a Colonel in World War I.

Pennsylvania State Police: The Pennsylvania State Police (PSP) is the state police force of Pennsylvania, responsible for statewide law enforcement.  It was founded in 1905 by order of Governor Samuel Pennypacker, by signing senate bill 278 on May 2.  The bill was signed in response to the Great Anthracite Strike of 1902, private police forces used by mine and mill owners to stop worker strikes (the Coal and Iron Police) and the inability or refusal of local police or sheriffs offices to enforce the law.  The strike lasted from May 15, 1902 to October 23, 1902 and ended with the help of Theodore Roosevelt the sitting president of the time.  The department became the first uniformed police organization of its kind in the United States and a model for other state police agencies throughout the nation.  PSP enlisted members are referred to as "troopers".  Up until 1963 married men were not allowed to apply to state police, and active trooper had to seek permission from their superior officer to get married.  In 1971 the first female applicant to the state police academy was accepted as a cadet and graduated in 1972.  As of October 2016, the state police have 4,233 state troopers, 5% of them being women, and more than 1,850 civilian support staff.  The state police academy is located in Hershey, Pennsylvania.

State Police of Crawford and Erie Counties: The State Police of Crawford and Erie Counties was a volunteer organization providing police service in northwest Pennsylvania.  It was separate and distinct from the Pennsylvania State Police and was disbanded in 2005.

Eastern State Penitentiary: The Eastern State Penitentiary, also known as ESP, is a former American prison in Philadelphia, Pennsylvania.  It is located at 2027 Fairmount Avenue between Corinthian Avenue and North 22nd Street in the Fairmount section of the city, and was operational from 1829 until 1971.  The penitentiary refined the revolutionary system of separate incarceration first pioneered at the Walnut Street Jail which emphasized principles of reform rather than punishment.

Baltimore County Jail: Baltimore County Jail is a historic jail located at Towson in Baltimore County, Maryland, United States.  It was built in 1855 and is a two-story Italianate style stone building, measuring 52 feet wide and 62 feet deep.  It consists of a five-bay-wide warden’s house with a central three story entry tower.  In the rear is a cell block with three levels of jail cells and covered by a gable roof.  The warden’s house and tower features a low pyramidal hipped roof and 30 in walls.  Attached to the warden’s house is a stone garage built in 1940.  It was used as a correctional facility until 2006.

Frank Noonan: Frank Noonan was formerly State Police Commissioner for the Pennsylvania State Police.  Noonan began his career in 1971 as an agent for the Federal Bureau of Investigation.  Following his retirement from the FBI in 1998, Noonan was appointed as Northeast Regional Director for the Attorney General's Bureau of Narcotics Investigation.  After 11 years as Regional Director, Noonan was promoted to Chief of Criminal Investigations for the Office of Attorney General in July 2009.

Question: In which city was the jail located which the first commissioner of the Pennsylvania State Police was a warden of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "commissioner": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the commissioner."
        },
        "role": {
          "type": "string",
          "description": "The role of the commissioner, e.g., 'first commissioner'."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "former_institution": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the institution the commissioner was formerly a warden of."
        },
        "type": {
          "type": "string",
          "description": "The type of institution, e.g., 'prison' or 'penitentiary'."
        },
        "location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the institution is located."
            },
            "state": {
              "type": "string",
              "description": "The state where the institution is located."
            }
          },
          "required": [
            "city",
            "state"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "type",
        "location"
      ],
      "additionalProperties": false
    },
    "answer_city": {
      "type": "string",
      "description": "The city where the jail is located, which is the final answer to the question."
    }
  },
  "required": [
    "commissioner",
    "former_institution",
    "answer_city"
  ],
  "additionalProperties": false
}
