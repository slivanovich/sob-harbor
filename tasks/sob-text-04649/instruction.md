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
Birthplace of Ronald Reagan: The Birthplace of Ronald Reagan, also known as the Graham Building, is located in an apartment on the second floor of a late 19th-century commercial building in Tampico, Illinois, United States.  The building was built in 1896 and housed a tavern from that time until 1915.  On February 6, 1911 the future 40th President of the United States, Ronald Reagan, was born in the apartment there, the family moving into a house in Tampico a few months later.

List of things named after Ronald Reagan: This is a list of things named after former President of the United States Ronald Reagan.  The "Ronald Reagan Legacy Project" is an organization founded by Americans for Tax Reform president Grover Norquist that seeks to name at least one notable public landmark in each U.S. state and all 3067 counties after the 40th president.

Ronald Reagan Presidential Library: The Ronald Reagan Presidential Library and Center for Public Affairs is the presidential library and final resting place of Ronald Wilson Reagan, the 40th President of the United States (1981–1989), and his wife Nancy Reagan.  Designed by Hugh Stubbins and Associates, the library is in Simi Valley, California, about 40 mi northwest of Downtown Los Angeles and 15 mi west of Chatsworth.

Edith Luckett Davis: Edith Prescott Luckett Davis (July 16, 1888 – October 26, 1987) was a film and Broadway stage actress in the 1910s and 1920s.  She was the mother of Nancy Reagan, First Lady of the United States from 1981 to 1989, and mother-in-law of US president Ronald Reagan.

Bibliography of Ronald Reagan: This bibliography of Ronald Reagan includes major books and articles about 40th President of the United States Ronald Reagan and his policies.

Dutch: A Memoir of Ronald Reagan: Dutch: A Memoir of Ronald Reagan is a 1999 biography with fictional elements by Edmund Morris about Ronald Reagan, the 40th President of the United States.  There is much controversy about the book, cited by the Amazon.com editorial staff as "one of the most unusual and critically scrutinized biographies ever written,because of the fictional characters in display."  Debate exists as to whether "Dutch" should even be referred to as a biography at all.  It was published by Random House and edited by executive editor Robert Loomis.

Nancy Reagan: Nancy Davis Reagan (born Anne Frances Robbins; July 6, 1921 – March 6, 2016) was an American film actress and the wife of Ronald Reagan, the 40th President of the United States.  She served as the First Lady of the United States from 1981 to 1989.

Death and state funeral of Ronald Reagan: On June 5, 2004, Ronald Reagan, the 40th President of the United States, died after having suffered from Alzheimer's disease for nearly a decade.  His seven-day state funeral followed.  After Reagan's death, his body was taken from his Bel Air, Los Angeles home to the Gates, Kingsley and Gates Funeral Home in Santa Monica, California to prepare the body for burial.  On June 7, Reagan's casket was transported by hearse and displayed at the Ronald Reagan Presidential Library in Simi Valley, California, then flown to Washington, D.C. on June 9 for a service, public viewing and tributes at the U.S. Capitol.  His death occurred on the 60th anniversary of the WWII Allied D-Day invasion of Normandy, France, and the 20th anniversary of his own well-remembered speech commemorating that occasion at Pointe du Hoc.  It was also the 36th anniversary of the assassination of Robert F. Kennedy.

First inauguration of Ronald Reagan: The first inauguration of Ronald Reagan as the 40th President of the United States was held on Tuesday, January 20, 1981, on the West Front of the United States Capitol in Washington, D.C..  This was the first inauguration to be held on the building's west side.  The inauguration marked the commencement of the first four-year term of Ronald Reagan as President and of George H. W. Bush as Vice President.  Chief Justice Warren E. Burger administered the presidential oath of office to Reagan, who placed his hand upon a family Bible given to him by his mother, open to .  Associate Justice Potter Stewart administered the vice presidential oath to Bush.

Presidency of Ronald Reagan: The presidency of Ronald Reagan began on January 20, 1981, when Ronald Reagan was inaugurated as President of the United States, and ended on January 20, 1989.  Reagan, a Republican, took office as the 40th United States president following a landslide win over Democratic incumbent President Jimmy Carter in the 1980 presidential election.  Reagan was succeeded by his vice president, George H. W. Bush, who won the 1988 presidential election with Reagan's support.

Question: Edith Prescott Luckett Davis, was a film and Broadway stage actress in the 1910s and 1920s, she was the mother of which woman who was American film actress and the wife of Ronald Reagan, the 40th President of the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the woman who is the daughter of Edith Prescott Luckett Davis and wife of Ronald Reagan."
    },
    "mother_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of her mother."
        },
        "relationship_to_person": {
          "type": "string",
          "description": "The relationship of the mother to the person."
        }
      },
      "required": [
        "name",
        "relationship_to_person"
      ],
      "additionalProperties": false
    },
    "husband_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of her husband."
        },
        "relationship_to_person": {
          "type": "string",
          "description": "The relationship of the husband to the person."
        },
        "presidency_number": {
          "type": "integer",
          "description": "The number of her husband's presidency."
        }
      },
      "required": [
        "name",
        "relationship_to_person",
        "presidency_number"
      ],
      "additionalProperties": false
    },
    "person_occupation": {
      "type": "string",
      "description": "The occupation of the woman."
    },
    "person_role": {
      "type": "string",
      "description": "The political role held by the woman."
    }
  },
  "required": [
    "person_name",
    "mother_details",
    "husband_details",
    "person_occupation",
    "person_role"
  ],
  "additionalProperties": false
}
