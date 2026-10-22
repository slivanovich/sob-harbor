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
Murder of Jaidyn Leskie: Jaidyn Raymond Leskie (30 April 1996 – 15 June 1997) was the Australian child of Bilynda Williams and Brett Leskie, kidnapped and murdered in 1997.  Despite leads, and the arrest and trial of a prime suspect, Leskie's murder remains unsolved.  Although the decision was made in 2002 not to hold an inquest into the toddler's death, the case remained in the news for several more years and an inquest was held in 2006 implicating the mother's boyfriend, Greg Domaszewicz, who at the time of the kidnapping was babysitting the boy at his house at Newborough.

Murder of Barbara Barnes: Barbara Ann Barnes was an American schoolgirl who was murdered in December 1995 at the age of thirteen.  The case remains unsolved to this day.  Many have speculated that her grandfather may have been responsible for her death, but others believe that the crime was committed by someone local to the area.  Journalist James Renner has published his theory that the case may be connected to the murders of Tina Harmon, Krista Harrison, Deborah Smith and Amy Mihaljevic.

Murder of Krista Harrison: The murder of Krista Lea Harrison occurred on July 17, 1982, in Marshallville, Ohio.  The case remained unsolved for two years, until Robert Anthony Buell was convicted of her murder in 1984.  Harrison's case appeared on the fifth season of the American television show "Forensic Files" in an episode titled "Material Evidence."

Matthew &quot;Mack&quot; Harrison Marsden: Matthew "Mack" Harrison Marsden (1849–1883) was a livestock trader who lived in rural Jefferson County, Missouri.  Marsden was suspected of many crimes from 1881 to 1883, including arson, murder, and robbery.  Though he was often accused, questioned, and arrested, he was only brought to trial one time, and was acquitted.  Marsden’s family background gave no hint of criminal activity.  On the contrary, he came from an established family of farmers, engineers, and stockmen, and his wife’s family members were known as leaders in the local church.  His story came to an end when he was murdered, and though four different men were arrested, and three of them tried for the killing, no one was ever convicted.  Mack’s suspected killers left the county, the murder remained unsolved, and Marsden’s death corresponded with the end of a years-long crime spree.  Newspapers suggested that his killing was a service to the community, and for decades, people continued to believe he was behind a gang that committed a long series of unsolved crimes.

John J. McCabe: John Joseph McCabe (1955 - September 26, 1969) was a youth from Tewksbury, Massachusetts who was abducted and murdered after attending a Knights of Columbus dance in Lowell, Massachusetts.  His bound and strangled body was found in an empty lot on Maple Street in Lowell the next day.  His murder remained unsolved for 41 years until April 2011 when three men were arrested for his murder.  The case was covered in a "48 Hours" episode titled "The Pact".  On February 20, 2014, Walter Shelly of Tewksbury was sentenced in Lowell Superior Court to life in prison for the murder of John J. McCabe.

Murder of Jacqueline Thomas: Jacqueline Mary Thomas (1945 or 1946 – 18 August 1961) was a 15-year-old biscuit factory worker from Alum Rock, Birmingham, England who was sexually assaulted and strangled after disappearing on 18 August 1961.  Her body was discovered a week later close to her home, and the murder sparked a manhunt involving several hundred police officers.  A suspect was identified at the time, but there was insufficient evidence to charge him, and the crime remained unsolved for over four decades until a cold case review in the 2000s.  In 2007, 70-year-old Anthony Hall – already serving a life sentence for the murder of another teenager – was charged with Thomas's murder.  However, a judge subsequently ruled the charge should be stayed owing to the length of time that had passed since the incident.  Hall subsequently died in prison.

Robison family murders: The Robison family murders, also referred to as the Good Hart murders, were the mass murders of Richard Robison, his wife Shirley Robison (née Fulton), and their four children; Ritchie, Gary, Randy, and Susan on June 25, 1968.  The upper-middle-class family from the metropolitan Detroit area of Lathrup Village, Michigan, were shot and killed while vacationing in their Lake Michigan cottage just north of Good Hart, Michigan, near the Straits of Mackinac.  This case remained unsolved after a 15-month investigation by the Michigan State Police and the Emmet County Sheriff's Office.  However, when the investigation was completed in December 1969, evidence pointed to one person: Joseph Raymond Scolaro III, an embezzling employee of Richard Robison.

Murder of Eva Blanco: Eva Blanco Puig (February 17, 1981 – April 20, 1997) was a Spanish high school student who was murdered on Algete, Community of Madrid.  The case remained unsolved until 2015, when new advancements in genealogical DNA research led to the arrest of Ahmed Chelh Gerj, a Moroccan-Spanish citizen who moved to France in 1999.  While it was unsolved, the case was popularly known in Spain as the Eva Blanco Case ("Caso Eva Blanco"), the Crime of Algete ("Crimen de Algete") and the Operation Gang ("Operación Pandilla"), the code name given to the investigation by the Spanish Civil Guard.

Murder of Celia Douty: Celia Natasha "Tasha" Douty (11 February 1943 – 1 September 1983) was a British resort worker who was murdered on Brampton Island in Queensland, Australia.  The crime remained unsolved until 2001, when Sydney motor industry finance Business Manager, Wayne Butler, was found guilty.  It was the first murder in Australia to be solved using DNA profiling.  The prosecution relied heavily on DNA evidence and it became a case study for the use of the technique in court.

Robert Anthony Buell: Robert Anthony Buell (September 10, 1940 – September 24, 2002) was a former Akron, Ohio Planning Department worker, convicted of the murder of 11-year-old Krista Lea Harrison on July 17, 1982.

Question: The murder of Krista Lea Harrison occurred on July 17, 1982, in Marshallville, Ohio, the case remained unsolved for two years, until which former Akron, Ohio Planning Department worker, convicted of the murder of 11-year-old Krista Lea Harrison on July 17, 1982?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "victim_name": {
      "type": "string",
      "description": "The full name of the murder victim."
    },
    "convicted_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person convicted of the murder."
        },
        "occupation": {
          "type": "string",
          "description": "The occupation of the convicted person."
        },
        "city_of_residence": {
          "type": "string",
          "description": "The city where the convicted person worked or resided."
        }
      },
      "required": [
        "name",
        "occupation",
        "city_of_residence"
      ],
      "additionalProperties": false
    },
    "conviction_year": {
      "type": "integer",
      "description": "The year the person was convicted."
    },
    "unsolved_duration_years": {
      "type": "integer",
      "description": "The number of years the case remained unsolved before conviction."
    },
    "crime_location": {
      "type": "string",
      "description": "The location where the murder occurred."
    }
  },
  "required": [
    "victim_name",
    "convicted_person",
    "conviction_year",
    "unsolved_duration_years",
    "crime_location"
  ],
  "additionalProperties": false
}
