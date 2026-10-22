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
Silas House: Silas Dwane House (born August 7, 1971) is an American writer best known for his novels.  He is also a music journalist, environmental activist, and columnist.  House's fiction is noted for its attention to the natural world, working class characters, and the plight of the rural place and rural people.

Ken Saro-Wiwa: Kenule Beeson "Ken" Saro-Wiwa (10 October 1941 – 10 November 1995) was a Nigerian writer, television producer, environmental activist, and winner of the Right Livelihood Award and the Goldman Environmental Prize.  Saro-Wiwa was a member of the Ogoni people, an ethnic minority in Nigeria whose homeland, Ogoniland, in the Niger Delta has been targeted for crude oil extraction since the 1950s and which has suffered extreme environmental damage from decades of indiscriminate petroleum waste dumping.  Initially as spokesperson, and then as president, of the Movement for the Survival of the Ogoni People (MOSOP), Saro-Wiwa led a nonviolent campaign against environmental degradation of the land and waters of Ogoniland by the operations of the multinational petroleum industry, especially the Royal Dutch Shell company.  He was also an outspoken critic of the Nigerian government, which he viewed as reluctant to enforce environmental regulations on the foreign petroleum companies operating in the area.

Dennis Delaney: Dennis Delaney (born January 29, 1953) is an American writer and actor, and former environmental activist who (in 1980) became the first National Director of Greenpeace USA.  He is a graduate of the University of North Carolina School of the Arts, and the University of California, Santa Cruz.

Atticus Lish: Atticus Lish (born 1972, age 43) is an American novelist.  His debut, "Preparation for the Next Life" (New York: Tyrant, 2014), caught its independent publisher “off guard” by becoming a surprise success, winning a number of awards including the PEN/Faulkner Award for Fiction.  Lish lives in Sunset Park, Brooklyn with his wife.  He is the son of influential literary editor Gordon Lish.

Gordon Lish: Gordon Lish (born February 11, 1934 in Hewlett, New York) is an American writer.  As a literary editor, he championed many American authors, particularly Raymond Carver, Barry Hannah, Amy Hempel, Rick Bass, and Richard Ford.  He is the father of the novelist Atticus Lish.

Rick Bass: Rick Bass (born March 7, 1958) is an American writer and an environmental activist.

Janisse Ray: Janisse Ray (born 1962) is an American writer, naturalist and environmental activist.

Douglas Glover (writer): Douglas Glover BA, M.Litt., MFA (born 14 November 1948 in Simcoe, Ontario.  Canada) is a Canadian writer.  He was raised on his family's tobacco farm just outside Waterford, Ontario.  He has published five short story collections, four novels (including "Elle" which won the 2003 Governor-General's Award for Fiction), two books of essays, "Notes Home from a Prodigal Son" and "Attack of the Copula Spiders", and "The Enamoured Knight", a book-length meditation on "Don Quixote" and novel form.  His 1993 novel, "The Life and Times of Captain N.", was edited by Gordon Lish and released by Alfred A. Knopf.  His most recent book is a story collection, "Savage Love" (Goose Lane Editions, 2013).

Steven Guilbeault: Steven Guilbeault (born 1970 in La Tuque, Quebec) is a Canadian science reporter, environmental reporter, environmental journalist, writer, consultant, venture capitalist, professional speaker, NGO founder and environmental activist.  He is best known as the co-founder of Équiterre, a non-profit and non-governmental organization.

Greg Mulcahy: Greg Mulcahy is an American novelist and short story writer.  He was born in St. Paul, Minnesota in 1958.  His collection,"Out of Work," was published by Alfred A. Knopf in 1993.  His novel, "Constellation," was published by Avisson Press in 1996.  His short fiction appeared frequently in Gordon Lish's "The Quarterly".  His work has also appeared in Diane Williams's NOON Coop Renner's "elimae," Kathryn Rantala's publications,"The New York Tyrant", "Caliban", "The Gettysburg Review", "Juked", "Alice Blue Review", "Sidebrow", "five_trope", "Word Riot," and other journals.

Question: Name an American writer and environmental activist championed by Gordon Lish.

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_found": {
      "type": "object",
      "description": "The American writer and environmental activist identified.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the person."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the person."
        },
        "professions": {
          "type": "array",
          "description": "A list of professions held by the person.",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_date",
        "professions"
      ],
      "additionalProperties": false
    },
    "championed_by_editor": {
      "type": "object",
      "description": "Details about the literary editor who championed the person.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the literary editor."
        },
        "role": {
          "type": "string",
          "description": "The role of the editor."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "criteria_matched": {
      "type": "array",
      "description": "A list of criteria from the question that were matched by the identified person.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_found",
    "championed_by_editor",
    "criteria_matched"
  ],
  "additionalProperties": false
}
