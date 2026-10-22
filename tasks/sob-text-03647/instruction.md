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
Yusuf Nazzal: Yusuf Nazzal (1937 – 6 September 1972) alias 'Tony', was the second in command of eight Palestinian fedayeen that invaded 31 Connollystrasse in the Munich Olympic Village on 5 September 1972.  Nine members of the Israeli Olympic team were taken hostage after two members, weightlifter Yossef Romano and wrestling coach Moshe Weinberg, were killed in the initial takeover.  Television images broadcast to the billions of people watching around the world show Nazzal frequently throughout the crisis, seemingly always smoking, wearing sunglasses, open neck red shirt and a cowboy hat, which led him to be identified as the 'Cowboy'.  According to author Serge Groussard, Nazzal "liked to be called Guevara".

Eliezer Halfin: Eliezer Halfin (18 June 1948, Riga – 6 September 1972, Munich) was a Latvian-born wrestler with the Israeli Olympic team at the 1972 Summer Olympics in Munich, Germany.  Along with 10 other athletes and coaches he was taken hostage by Palestinian Black September terrorists on 5 September 1972.

Luttif Afif: Luttif Afif (1937 or 1945 – 6 September 1972), "alias" Issa (Jesus in Arabic), was the commander of the group of Palestinian fedayeen, who led the invasion into the Munich Olympic Village on 5 September 1972 and took as hostage nine members of Israel's Olympic team after killing two members who resisted.  He was the chief negotiator on behalf of the Palestinians, who were members of the Black September offshoot of Yassir Arafat's Palestine Liberation Organization.  The various pictures of Afif, wearing a white beach hat and a linen safari suit and his face covered with charcoal or shoe polish are some of the iconic images of the 1972 Munich Olympics.

Ian Livingstone (disambiguation): Ian Livingstone (born 1949) is an English fantasy author and video games entrepreneur.

The House on the Borderland and Other Novels: The House on the Borderland and Other Novels is a collection of short novels by author William Hope Hodgson.  It was published by Arkham House in 1946 in an edition of 3,014 copies.  The collection was reprinted by Gollancz in 2002, with a new introduction by China Miéville, as volume 33 of their Fantasy Masterworks series.

Ian Livingstone: Ian Livingstone CBE (born 29 December 1949 ) is an English fantasy author and entrepreneur.  Along with Steve Jackson, he is the co-founder of a series of role-playing gamebooks, "Fighting Fantasy", and the author of many books within that series.  He is also one of the co-founders of prominent games company Games Workshop.

China Miéville: China Tom Miéville {'1': ", '2': ", '3': ", '4': "} ( ; born 6 September 1972) is an English fantasy fiction author, comic writer, political activist and academic.  He often describes his work as weird fiction and allied to the loosely associated movement of writers sometimes called New Weird.

Stephen Deas: Stephen Deas, born in 1968 in Southeast England, is an English fantasy author.  He is most famous for his fantasy opus, the "Memory of Flames" sequence, set in a fantasy world inhabited by dragons.

Matt Thistlethwaite: Matthew James "Matt" Thistlethwaite (born 6 September 1972) is an Australian politician.  He has been an Australian Labor Party member of the Australian House of Representatives since 2013, representing the electorate of Kingsford Smith.  He was formerly a member of the Australian Senate from 2011 to 2013.  Thistlethwaite served as Parliamentary Secretary for Pacific Island Affairs and Parliamentary Secretary for Multicultural Affairs in the Gillard government from March to July 2013, and as Parliamentary Secretary for Infrastructure and Transport in the Rudd government from July to September 2013.  Before entering electoral politics, he was the general secretary of the New South Wales branch of the Australian Labor Party.

David Lee Stone: David Lee Stone (born 1978), is an English fantasy author best known for his series of books "The Illmoor Chronicles".  He has also written under the pseudonyms David L. Stone, David Grimstone and Rotterly Ghoulstone.

Question: What English fantasy author born 6 September 1972  wrote the new introduction to The House on the Borderland and Other Novels.

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "author_nationality": {
      "type": "string",
      "description": "The nationality of the author."
    },
    "author_profession": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Professions or roles of the author."
    },
    "author_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the author in YYYY-MM-DD format."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book to which the author contributed."
    },
    "contribution_type": {
      "type": "string",
      "description": "The type of contribution made by the author to the book."
    },
    "reprint_year": {
      "type": "integer",
      "description": "The year the book was reprinted with the new contribution."
    }
  },
  "required": [
    "author_name",
    "author_nationality",
    "author_profession",
    "author_birth_date",
    "book_title",
    "contribution_type",
    "reprint_year"
  ],
  "additionalProperties": false
}
