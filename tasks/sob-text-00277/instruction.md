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
Downing Street Declaration: The Downing Street Declaration (DSD) was a joint declaration issued on 15 December 1993 by the Prime Minister of the United Kingdom, John Major, and the Taoiseach of the Republic of Ireland, Albert Reynolds at the British Prime Minister's office in 10 Downing Street.

Prime Minister's Official Spokesperson: The Prime Minister's Official Spokesperson or alternatively Prime Minister's Official Spokesman/Spokeswoman is a position in the United Kingdom's Civil Service, located in the Prime Minister's Office in 10 Downing Street and used by the British Prime Minister to convey information to the public.  The Prime Minister's Official Spokesperson usually addresses a small group of press and media correspondents, known as lobby correspondents, each morning to deliver statements on current events on behalf of the Prime Minister.

Chief Mouser to the Cabinet Office: The Chief Mouser to the Cabinet Office is the title of the official resident cat of the Prime Minister of the United Kingdom at 10 Downing Street.  Only four cats, Humphrey, Sybil, Larry and Freya have been given the title officially; other cats were given this title affectionately, usually by the British press.  There has been a resident Treasury or Downing Street cat employed as a mouser and pet since the reign of Henry VIII, when Cardinal Wolsey placed his cat by his side while acting in his judicial capacity as Lord Chancellor, an office he assumed in 1515.

10 Downing Street Guard Chairs: The 10 Downing Street Guard Chairs are two antique chairs.  In the early 19th century, 10 Downing Street was guarded by two men who sat outside the building in leather chairs made by Thomas Chippendale.  There was a drawer underneath the chair which was filled with hot coals to keep the guards warm whilst on duty.  The chairs were made with a circular back and hood, both to shield the guards from bad weather and to improve the surrounding acoustics, thereby allowing the guard to hear better from a wider angle.

Marienborg: Marienborg has been the official residence of Denmark's prime minister since 1962.  It is frequently used for governmental conferences, summits and other official purposes, including the prime minister's new year speech.  Unlike the residences of other heads of government and state (e.g. the White House, 10 Downing Street, La Moncloa and Élysée Palace), Marienborg does not serve as the government headquarters or contain the office of the prime minister, instead Christiansborg Palace is the location of the government departments.

Downing Street mortar attack: The Downing Street mortar attack was carried out by the Provisional Irish Republican Army (IRA) on 7 February 1991.  The IRA launched homemade mortar shells at 10 Downing Street, London, the official residence of the Prime Minister of the United Kingdom.  It was an attempt to assassinate Prime Minister John Major and his War Cabinet, who were meeting to discuss the Gulf War.  One of the heavy mortar shells exploded in the back garden of number 10, only yards from the cabinet office.  Due to the bomb-proof windows, none of the cabinet were hurt, though four other people received minor injuries, including two police officers.  The other two shells overshot Downing Street and landed on a green nearby.

Larry (cat): Larry is the 10 Downing Street cat and is Chief Mouser to the Cabinet Office.  Larry is a brown and white tabby, believed to have been born in January 2007.  By July 2016, when Theresa May became Prime Minister, Larry had developed a reputation of being "violent" in his interactions with other local mousers, namely the Foreign Office's much younger cat Palmerston.

List of residents of 10 Downing Street: Number 10 Downing Street is the residence and office of the First Lord of the Treasury as Prime Minister of the United Kingdom.  The headquarters of Her Majesty's Government, it is situated on Downing Street in the City of Westminster in London, England.

Downing Street memo: The "Downing Street memo" (or the "Downing Street Minutes"), sometimes described by critics of the Iraq War as the "smoking gun memo", is the note of a 23 July 2002 secret meeting of senior British government, defence and intelligence figures discussing the build-up to the war, which included direct reference to classified United States policy of the time.  The name refers to 10 Downing Street, the residence of the British prime minister.

Humphrey (cat): Humphrey (c. 1988 – March 2006) was a cat employed as the Chief Mouser to the Cabinet Office at 10 Downing Street, the official residence of the Prime Minister of the United Kingdom, from October 1989 to 13 November 1997.

Question: Larry is the 10 Downing Street, official resident cat of the Prime Minister of the UK, also called? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cat_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the cat."
        },
        "breed": {
          "type": "string",
          "description": "The breed or description of the cat."
        },
        "birth_year": {
          "type": "integer",
          "description": "The believed year of the cat's birth."
        }
      },
      "required": [
        "name",
        "breed",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "official_title": {
      "type": "string",
      "description": "The official title held by the cat."
    },
    "residence_address": {
      "type": "string",
      "description": "The official residence of the cat."
    },
    "associated_with_office": {
      "type": "string",
      "description": "The office or position the cat is officially associated with."
    }
  },
  "required": [
    "cat_details",
    "official_title",
    "residence_address",
    "associated_with_office"
  ],
  "additionalProperties": false
}
