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
Herald Corporation: Herald Corporation (formally Herald Media) is a South Korean media, education, and lifestyle company that provides a variety of contents and ecofriendly initiatives through its publications and subsidiaries.  This is located in Seoul, South Korea and founded in 1953.  It publishes the "Korea Herald", "Herald Business", "Junior Herald", and "Campus Herald".  Over the past 60 plus years, Herald, through its publication such as «a href="The%20Korea%20Herald">The Korea Herald</a», <Herald Business>, and <Junior Herald>, has evolved into a unique media and lifestyle platform that places a strong emphasis on education, design, and sustainability.

Kennebec Journal: The Kennebec Journal is a seven-day morning daily newspaper published in Augusta, Maine.  It is owned by MaineToday Media, which also publishes the state's largest newspaper, the "Portland Press Herald".

MaineToday Media: MaineToday Media is a privately owned publisher of daily and weekly newspapers in the U.S. state of Maine, based in the state's largest city, Portland.  It includes the "Portland Press Herald" and "Maine Sunday Telegram", the state's largest newspaper.

Jerry Crasnick: Jerry Crasnick is a sportswriter currently covering baseball for the sports website ESPN.com.  He began his career working for the Biddeford Journal Tribune in Maine, as well as the Portland Press Herald.  In 1988 he served as the beat writer for "The Cincinnati Post" where he covered the Cincinnati Reds.  During his time as beat writer, Crasnick covered Pete Rose and his suspension from Major League Baseball.  Crasnick also covered the Reds' 1990 World Series championship, and five years of Marge Schott's tenure as owner of the Reds.  He has worked for "The Denver Post" and Bloomberg News, while also writing for The Sporting News and Baseball America.

Andrés Oppenheimer: Andrés Oppenheimer (born in 1951 in Buenos Aires, Argentina) is the editor and syndicated foreign affairs columnist with "The Miami Herald," anchor of "Oppenheimer Presenta" on CNN En Español, and author of seven books, several of which have been published in English, Spanish, Portuguese and Japanese"."  His column, "The Oppenheimer Report," appears twice a week in "The Miami Herald" and more than 60 U.S. and international newspapers, including the Miami Herald, El Mundo of Spain, "La Nación" of Argentina, Reforma of Mexico, El Mercurio of Chile and El Comercio of Peru.  He is the author of “Saving the Americas” (Random House, 2007) and six other best-selling books, and is a regular political analyst with CNN en Español.  His previous jobs at The Miami Herald included Mexico City bureau chief, foreign correspondent, and business writer.  He previously worked for five years with The Associated Press in New York, and has contributed on a free-lance basis to "The New York Times", "The Washington Post", "The New Republic", the BBC, CBS’ “60 Minutes”, and El Pais of Spain.

Ethan Strimling: Ethan King Strimling (born October 19, 1967) is the mayor of Portland, Maine, who served as a Democratic state senator from 2002 to 2009.  He was replaced by Justin Alfond.  He is Executive Director of LearningWorks, a West End non-profit organization, and has served as a political columnist and commentator for the Portland Press Herald.

Cell Biology International: Cell Biology International is a peer-reviewed scientific journal published by Portland Press for the International Federation for Cell Biology.  The journal was established in 1977 as "Cell Biology International Reports" (ISSN 0309-1651  ) and published by Elsevier, obtaining its current name in 1993.  The journal was transferred to Portland Press in 2010.  It covers all aspects of cell biology.

Portland Press Herald: The Portland Press Herald (and Maine Sunday Telegram; collectively known as The Portland Newspapers) publish daily newspapers in the city of Portland, Maine, in the United States.  Serving the state's largest and principal commercial city, as well as much of southern Maine, the "Press Herald" and "Maine Sunday Telegram" form the largest-circulation newsroom in the state.

Herald House: Herald House or Herald Publishing House is the publishing division of the Community of Christ in Independence, Missouri.  It publishes books, periodicals and other materials at the direction of the First Presidency.  Its history dates to the publication of a church periodical called the "True Latter Day Saints' Herald" in Cincinnati, Ohio in 1860.  The first church-owned press was located in Plano, Illinois and a much larger facility was opened in Lamoni, Iowa in 1881.  The publishing plant in Lamoni was destroyed by fire in 1907.  A replacement facility was built shortly thereafter.  When the church headquarters moved to Independence, Missouri in 1921, the Herald House was relocated to a facility that had previously been used by an artillery battalion of the Missouri National Guard.  In 1965, a modern publishing facility was built for Herald House on Noland Road in Independence.  That facility was closed in 1999 and printing has been outsourced since that date.  The publishing offices were moved to The Temple and The Auditorium in Independence, Missouri.

Barbara Walsh (journalist): Barbara Ann Walsh (born August 13, 1958) is an American journalist and writer of children's books.  She has worked for "The Eagle-Tribune" (Lawrence, MA), "Portland Press Herald", and "South Florida Sun-Sentinel", and has taught journalism at Florida International University, University of Southern Maine, and University of Maine at Augusta.  She won a Pulitzer Prize in 1988 for a series she wrote for the "Eagle-Tribune" about the Massachusetts prison system.  Barbara has also worked as an international speaker for the U.S. Department of State.

Question: Which city is the company that owns the "Portland Press Herald" located in? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "owner_company_name": {
      "type": "string",
      "description": "The name of the company that owns the specified publication."
    },
    "owner_company_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the owner company is based."
        },
        "state": {
          "type": "string",
          "description": "The state where the owner company is based."
        },
        "country": {
          "type": "string",
          "description": "The country where the owner company is based."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "publication_name": {
      "type": "string",
      "description": "The name of the publication in question."
    }
  },
  "required": [
    "owner_company_name",
    "owner_company_location",
    "publication_name"
  ],
  "additionalProperties": false
}
