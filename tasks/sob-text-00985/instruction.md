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
Mount Holyoke College: Mount Holyoke College is a liberal arts college for women in South Hadley, Massachusetts, United States.  It was the first member of the Seven Sisters colleges, and it served as a model for some of the others.  Mount Holyoke is part of the region's Five College Consortium, along with Amherst College, Smith College, Hampshire College, and the University of Massachusetts Amherst.

Mary Eleanor Wilkins Freeman: Mary Eleanor Wilkins Freeman (October 31, 1852 – March 13, 1930) was a prominent 19th-century American author.

Wide Awake (magazine): Wide Awake was a monthly American children's magazine, founded in 1875 by Daniel Lothrop.  It published stories written by Margaret Sidney, Edward Everett Hale, Sarah Orne Jewett, Elizabeth Stuart Phelps Ward, and Mary Eleanor Wilkins Freeman.  "Wide Awake" was illustrated by many well known artists including Howard Pyle, William Thomas Smedley, and Sol Eytinge Jr.

Pembroke (book): Pembroke (1894) is a novel written by Mary E. Wilkins Freeman.  It is set in the small town of Pembroke, Massachusetts in the 1830s and 40s.  The novel tells the story of a romance gone awry and the dramatic events that follow, which entertain the residents of the small town for years after.  As one of Freeman's first novels, "Pembroke" experienced great success in its time and, although it has only recently experienced a comeback in the academic sphere, it is known for being an exemplary piece of New England local color fiction.

Peter Swirski: Peter Swirski (born 1966) is a Canadian scholar and literary critic featured in "Canadian Who's Who" and Amazon's #1 Bestseller in American Literary History and Criticism and in Canadian Literary History and Criticism.  Specialist in American literature and American Studies, he is the author of seventeen books, including the prize-winning "Ars Americana, Ars Politica" (2010) and the staple of American popular culture studies "From Lowbrow to Nobrow" (2005).  His other well-known studies include "American Utopia and Social Engineering" (2011), "American Political Fictions" (2015), and the digital-futurological bestseller "From Literature to Biterature" (2013).  He is also the leading scholar on the late writer and philosopher Stanisław Lem.

A New England Nun: "A New England Nun" is a short story by Mary Eleanor Wilkins Freeman published in 1891.

Collected Ghost Stories: Collected Ghost Stories is a posthumous collection of stories by author Mary E. Wilkins Freeman (1852–1930).  It was released in 1974 by Arkham House in an edition of 4,155 copies.  The book is the first collection of all of Freeman's supernatural stories.

Leah Blatt Glasser: Leah Blatt Glasser is an American literary critic and Mary Eleanor Wilkins Freeman scholar at Mount Holyoke College.  She is currently "Dean of First-Year Studies & Lecturer in English" at Mount Holyoke College.  Her former student (the Pulitzer Prize-winning playwright, Suzan-Lori Parks) would later credit Glasser with her success.

Young Lucretia and Other Stories: Young Lucretia and Other Stories is a collection of thirteen short stories by Mary Eleanor Wilkins Freeman.  The individual stories in book were originally published in leading literary magazines such as "Harper's Young People" and "St. Nicholas Magazine" between 1887 and 1892.  They were later collected and reprinted by Harper & Brothers in 1892.  These stories primarily feature children who learn moral lessons after misbehaving.

The Pot of Gold and Other Stories: The Pot of Gold and Other Stories is a collection of children's short stories written by American author Mary Eleanor Wilkins Freeman.  First published in 1892 by D. Lothrop Company in Boston, the stories are set in the villages of New England.  Hiding beneath the child-friendly narration of these sixteen stories, Wilkins comments on New England village life and the post-Civil war woman.

Question: In which state is the college that Leah Blatt Glasser is an American literary critic and Mary Eleanor Wilkins Freeman scholar?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "scholar_name": {
      "type": "string",
      "description": "The name of the scholar."
    },
    "college_name": {
      "type": "string",
      "description": "The name of the college where the scholar works."
    },
    "college_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the college is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the college is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the college is located."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "answer_state": {
      "type": "string",
      "description": "The state where the college is located, which is the answer to the question."
    }
  },
  "required": [
    "scholar_name",
    "college_name",
    "college_location",
    "answer_state"
  ],
  "additionalProperties": false
}
