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
Season of Migration to the North: Season of Migration to the North (Arabic: موسم الهجرة إلى الشمال‎ ‎ Mawsim al-Hiǧra ilā ash-Shamāl ) is a classic post-colonial Sudanese novel by the novelist Tayeb Salih.  Originally published in Arabic in 1966, it has since been translated into more than twenty languages.  Salih was fluent in both English and Arabic, but chose to pen this novel in Arabic.  The English translation was published in 1969 as part of the influential Heinemann African Writers Series.  The novel is a counter narrative to "Heart of Darkness".  It was described by Edward Said as one of the six great novels in Arabic literature.  In 2001 it was selected by a panel of Arab writers and critics as the most important Arab novel of the twentieth century.

Scott Meredith: Scott Meredith, born Arthur Scott Feldman (1923, New York City, NY – 1993, Manhasset, NY) was a prominent American literary agent, and founder of the Scott Meredith Literary Agency.  His clients included famous and successful writers such as Richard S. Prather, Morris West, Norman Mailer, J.G. Ballard, Arthur C. Clarke, P.G. Wodehouse and Philip K. Dick.

Native Writers' Circle of the Americas: The Native Writers' Circle of the Americas (NWCA) is an organization of Native American writers, most notable for its literary awards, presented annually to Native American writers in three categories: First Book of Poetry, First Book of Prose, and Lifetime Achievement.  The awards are voted upon by Native American writers, making it one of the few literary awards presented to Native Americans by Native Americans.

The Devil's Advocate (West novel): The Devil's Advocate is a 1959 novel by Australian author Morris West. <ref name="National Library of Australia - Trove - The devil's advocate / Morris West"> </ref> It forms part of West's "Vatican" sequence of novels, along with "The Shoes of the Fisherman" (1963), "The Clowns of God" (1981), and "Lazarus" (1990).

Denys Johnson-Davies: Denys Johnson-Davies (Arabic: دنيس جونسون ديڤيز) (also known as Abdul Wadud) was an eminent Arabic-to-English literary translator who translated, "inter alia," several works by Nobel Prize-winning Egyptian author Naguib Mahfouz, Sudanese author Tayeb Salih, Palestinian poet Mahmud Darwish and Syrian author Zakaria Tamer.

The Salamander (1981 film): The Salamander (also known as Morris West's The Salamander) is a 1981 thriller film directed by Peter Zinner, at his directorial debut.  The film is based on a novel with the same name by Morris West.

The Ambassador (West novel): The Ambassador is a novel by Australian author Morris West. <ref name="NLA - Trove - The Ambassador / Morris West"> </ref> It was first published in 1965.  The novel is fictionalisation of the period leading up to and shortly after the Coup d'état against and assassination of South Vietnamese President Ngo Dinh Diem.

The Wedding of Zein: The Wedding of Zein (Arabic: عرس الزين) is a contemporary Arabic novel by the late Sudanese author Tayeb Salih.  It was published in Arabic in 1962 and translated into English in 1968.  Within the realm of Arab literature, the book is considered a classic and was republished as part of the influential Heinemann African Writers Series.

Tayeb Salih: Tayeb Salih (Arabic: الطيب صالح‎ ‎ ; 12 July 1929 – 18 February 2009) was a Sudanese writer.

Morris West: Morris Langlo West AO (26 April 19169 October 1999) was an Australian novelist and playwright, best known for his novels "The Devil's Advocate" (1959), "The Shoes of the Fisherman" (1963) and "The Clowns of God" (1981).  His books were published in 27 languages and sold more than 60 million copies worldwide.  Each new book he wrote after he became an established writer sold more than one million copies.

Question: Were Morris West and Tayeb Salih American writers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_topic": {
      "type": "string",
      "description": "The main topic of the question asked."
    },
    "authors": {
      "type": "array",
      "description": "List of authors whose nationalities were checked.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin/nationality of the author as stated in the context."
          },
          "is_american": {
            "type": "boolean",
            "description": "True if the author is American, false otherwise."
          }
        },
        "required": [
          "name",
          "origin_country",
          "is_american"
        ],
        "additionalProperties": false
      }
    },
    "answer": {
      "type": "boolean",
      "description": "The final boolean answer to the question 'Were Morris West and Tayeb Salih American writers?'"
    }
  },
  "required": [
    "question_topic",
    "authors",
    "answer"
  ],
  "additionalProperties": false
}
