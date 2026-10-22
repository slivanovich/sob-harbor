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
Death of Aiyana Jones: Aiyana Mo'Nay Stanley-Jones (July 20, 2002 – May 16, 2010), was a seven-year-old African-American girl from the east side of Detroit, Michigan who was shot and killed during a raid conducted by the Detroit Police Department's Special Response Team on May 16, 2010.  Her death drew national media attention and led U.S. Representative John Conyers to ask U.S. Attorney General Eric Holder for a federal investigation into the incident.

Sibley County ICTV System: The Sibley County Interactive Cable TV (ICTV) System was a groundbreaking form of distance education using interactive television that drew national media attention.

Jon Hippe: Jon Mathias Hippe (26 September 1959) is a Norwegian researcher, politician and presenter.  He received national media attention when he was made General Manager of the Fafo foundation.  He continues to hold that position, however, in 2010 he was elected leader of A-pressen.  He is the younger brother of Ivar Hippe, a political consultant and former editor-in-chief of "Økonomisk Rapport".

Lutz Heilmann: Lutz Heilmann (born September 7, 1966 in Zittau, GDR) is a German politician of the left-wing party Die Linke.  He was elected to the Bundestag in the 2005 federal election as a member of the party list in Schleswig-Holstein.  Shortly thereafter it was revealed that he had worked for the Stasi (the East German secret police) from 1985 to 1990.  Heilmann drew national and international media attention when he caused the website codice_1 (not the German Wikipedia, but a search portal for it run by Wikimedia Deutschland) to be blocked by a preliminary injunction on November 13, 2008.  His Bundestag term ended in 2009, and he failed to be nominated for a second term.

John Conyers: John James Conyers Jr. (born May 16, 1929) is an American Democratic politician and the U.S. Representative for  's 13th congressional district .  The district includes the western half of Detroit, as well as River Rouge, Ecorse, Redford Township, Dearborn Heights, Highland Park, Westland, Garden City, Inkster, Wayne, and Romulus.  As the longest-serving active Representative, he is the Dean of the House of Representatives.

El Camino High School (Oceanside, California): The school drew national media attention in June 2008 for staging a controversial fake car accident, telling students their classmates had died as part of an anti-drunk driving program called "Every 15 Minutes--Extreme".  "Many seniors from all walks of life were included in the program to show the wide reach and seriousness of drunk driving" said Greg Vargas one of the dead seniors.

Alex Alben: Alex Alben (born New York City, 1958), American politician, author and technology executive, was named the first Chief Privacy Officer of Washington State in April 2015.  Previously, he was a candidate for the United States House of Representatives in 2004, a campaign which drew national attention because of the high tech district and the media personalities involved in the race, as noted by media coverage in The New York Times, "In a House Campaign With Personality, One Candidate Has the Microphone," June 12, 2004.  He ran as a Democrat in the Eighth Congressional District of Washington.  The seat has been held by Dave Reichert (R.) since 2004.  Alben is the author of "Analog Days—How Technology Rewrote Our Future," and consults to universities, high tech and energy companies.  Focusing on digital culture and privacy issues, Alben is a popular public speaker with Humanities Washington.http://www.humanities.org/programs/speakers/2015-16-speakers/AlexAlben

Criser High School: Criser High School was an African American school accommodating grades 1-12 constructed in 1959 in the Northern Virginia town of Front Royal, Virginia.  Its opening occurred the same year 22 African American students integrated the all-white Warren County High School which drew national media attention.

UAE National Media Council: The"UAE National Media Council (NMC)" is a federal institution established by virtue of Federal Law No. 1 of 2006.  It promotes and supports all media-related initiatives and activities in the UAE and abroad; it works to guarantee the implementation of the best international standards as far as media organization is concerned, as provided for in Cabinet decisions and law No. 15 of 1980 on Press and Publication.  Besides, the federal government counts on the National Media Council (NMC) to shape and insure the implementation of national media policy all in keeping a close collaboration with the other concerned institutions.  The council tries to go beyond its formal mission and to be active in the Emirati society and sign cooperation conventions with its counterpart institutions.

Simon Berman: Simon Berman (April 24, 1861 – October 19, 1934) was the mayor of Kwadijk, Middelie, Warder, Schagen, Bedum, and Alblasserdam in the Netherlands.  He was the first mayor of Kwadijk, Middelie, and Warder to actually live in one of those villages.  As a popular mayor of Schagen, he handled a double murder case that drew national media attention and advanced a professional school and regional light rail and canals.  In Alblasserdam, he addressed the local impacts of World War I.  Berman is also known for his association with Christian anarchism.

Question: What distinction does the representative who drew national media attention to the death of Aiyana Jones hold?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "representative_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the U.S. Representative."
        },
        "role": {
          "type": "string",
          "description": "The political role of the individual."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "event_of_attention": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the event that drew national media attention."
        },
        "action_taken": {
          "type": "string",
          "description": "The action taken by the representative regarding the event."
        }
      },
      "required": [
        "name",
        "action_taken"
      ],
      "additionalProperties": false
    },
    "distinction_held": {
      "type": "string",
      "description": "The specific distinction or title held by the representative."
    }
  },
  "required": [
    "representative_details",
    "event_of_attention",
    "distinction_held"
  ],
  "additionalProperties": false
}
