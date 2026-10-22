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
Resistance (2003 film): Resistance is a 2003 Dutch/American World War II film, directed by Todd Komarnicki and starring Bill Paxton, Julia Ormond, Philippe Volter, Sandrine Bonnaire, and Victor Reinier.  It was written by Komarnicki and Anita Shreve, based on Shreve's 1995 novel of the same name.  "Resistance", with a 16 million euro budget, was the most expensive Dutch production ever.  Its theatrical run lasted for just one week.

Sea Glass: Sea Glass is a 2002 romance novel by Anita Shreve.  It is chronologically the second novel in Shreve's informal trilogy to be set in a large beach house on the New Hampshire coast that used to be a convent.  It is preceded by "Fortune's Rocks" and followed by "The Pilot's Wife".

Slightly Foxed: Slightly Foxed is a British quarterly literary magazine.  Its primary focus is books and book culture.  2016 saw the publication of its fiftieth issue.  Notable authors to have written for the magazine include Penelope Lively, Richard Mabey, Diana Athill, Ronald Blythe and Robert Macfarlane.

Fortune's Rocks (novel): Fortune's Rocks is a 1999 romance novel by bestselling author Anita Shreve.  It is chronologically the first novel in Shreve's tetralogy to be set in a large beach house on the New Hampshire coast that used to be a convent.  It is followed by "Sea Glass", "The Pilot's Wife" and "Body Surfing".

Anita Shreve: Anita Shreve (born 1946) is an American writer.  The daughter of an airline pilot and a homemaker, she graduated from Dedham High School in Massachusetts, attended Tufts University and began writing while working as a high school teacher in Reading, Massachusetts.  One of her first published stories, "Past the Island, Drifting", (published in 1975) was awarded an O. Henry Prize in 1976.

A Flag on the Island: A Flag on the Island is a collection of short stories written by V.S. Naipaul, and first published by André Deutsch in 1967.  It includes the title novella, "A Flag on the Island," outtakes from previous novels such as "The Enemy", from "Miguel Street", and pieces published in periodicals in England or the United States.  The book is dedicated to Diana Athill.

Writers' &amp; Artists' Yearbook: The current edition is the 2018 edition and includes articles by William Boyd, J.K. Rowling, Diana Athill, Tom Holland, Anita Bean, Neil Gaiman, Katie Fforde amongst others.

The Pilot's Wife: The Pilot's Wife : A Novel is a 1998 novel by Anita Shreve.  It is chronologically the third novel in Shreve's informal trilogy to be set in a large beach house on the New Hampshire coast that used to be a convent.  It is preceded by "Fortune's Rocks" and "Sea Glass".

Diana Athill: Diana Athill {'1': ", '2': ", '3': 'OBE', '4': "} (born 21 December 1917) is a British literary editor, novelist and memoirist who worked with some of the greatest writers of the 20th century at the London-based publishing company Andre Deutsch Ltd.

Judith Hearne: Judith Hearne (later republished as The Lonely Passion of Judith Hearne), was regarded by Northern Irish-Canadian writer Brian Moore as his first novel.  The book was published in 1955, after Moore had left Ireland and was living in Canada.  It was rejected by ten American publishers before being accepted by a British publisher.  Diana Athill's memoir, "Stet" (2000), has information about the publishing of "Judith Hearne".

Question: Are Anita Shreve And Diana Athill from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "authors_compared": {
      "type": "array",
      "description": "Details about the authors whose nationalities are being compared.",
      "items": {
        "type": "object",
        "properties": {
          "author_name": {
            "type": "string",
            "description": "The name of the author."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the author."
          }
        },
        "required": [
          "author_name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "are_from_same_country": {
      "type": "boolean",
      "description": "True if both authors are from the same country, false otherwise."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the identified nationalities."
    }
  },
  "required": [
    "question_asked",
    "authors_compared",
    "are_from_same_country",
    "reasoning"
  ],
  "additionalProperties": false
}
