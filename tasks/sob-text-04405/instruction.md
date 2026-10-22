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
The Tin Drum: The Tin Drum (German: "Die Blechtrommel" ) is a 1959 novel by Günter Grass.  The novel is the first book of Grass's "Danziger Trilogie " (Danzig Trilogy) and winner of the Nobel Prize in literature.  It was adapted into a 1979 film, which won both the Palme d'Or, in the same year, and the Academy Award for Best Foreign Language Film the following year.

Günter Grass: Günter Wilhelm Grass (] ; 16 October 1927 – 13 April 2015) was a German novelist, poet, playwright, illustrator, graphic artist, sculptor, and recipient of the 1999 Nobel Prize in Literature.

Hugh Ambrose: Hugh Alexander Ambrose (August 12, 1966 – May 23, 2015) was an American historian and the author of a best-selling popular history of the Pacific Theater in World War II.  Ambrose rose to prominence as a researcher for and collaborator with his father, historian Stephen E. Ambrose.

Dog Years (novel): Dog Years (Hundejahre) is a novel by Günter Grass.  It was first published in Germany in 1963.  Its English translation, by Ralph Manheim, was first published in 1965.  It is the third and last volume of his "Danzig Trilogy", the other two being "The Tin Drum" and "Cat and Mouse".  The novel consists of three different chronological parts, from the 1920s to the 1950s.  The main characters are Walter Matern and Eduard Amsel.

The Meeting at Telgte: The Meeting at Telgte (German: Das Treffen in Telgte ) is a 1979 novel by the West German writer Günter Grass.  The narrative revolves around a fictional meeting for intellectuals hosted by Simon Dach after the Thirty Years' War.  The story is an analogy for the post-World War II society in Germany, and of Group 47 in West Germany, of which Grass was a member.

Crabwalk: Crabwalk, published in Germany in 2002 as Im Krebsgang, is a novel by Danzig-born German author Günter Grass.  As in earlier works, Grass concerns himself with the effects of the past on the present; he interweaves various strands and combines fact and fiction.  While the murder of Wilhelm Gustloff by David Frankfurter and the sinking of the ship the "Wilhelm Gustloff" are real events, the fictional members of the Pokriefke family bring these events into our own time.

China Marine (memoir): China Marine: An Infantryman's Life after World War II is the second memoir written by United States Marine Corporal Eugene B. Sledge, published posthumously with foreword by Stephen E. Ambrose, without subtitle, on May 10, 2002 by University of Alabama Press It was republished in paperback with the full title by Oxford University Press in July 2003.  This book is the sequel to his first, better known, memoir, "With the Old Breed: At Peleliu and Okinawa" and Ambrose identifies it as the only account of the Marines stationed in postwar China.  It has recently achieved wider public recognition as credited source material for the 2010 HBO miniseries "The Pacific".

Halleck: Lincoln's Chief of Staff: Halleck: Lincoln's Chief of Staff is the biography of Union Army General-in-Chief Henry Halleck written by Stephen E. Ambrose and published in 1962.  In this book, Ambrose provides an interpretation contrary to previous assessments of this "controversial figure" from the American Civil War.

Stephen E. Ambrose: Stephen Edward Ambrose (January 10, 1936 – October 13, 2002) was an American historian and biographer of U.S. Presidents Dwight D. Eisenhower and Richard Nixon.  He was a longtime professor of history at the University of New Orleans and the author of many bestselling volumes of American popular history.

The Box (Grass book): The Box (German: Die Box ) is a 2008 fictionalised autobiography by the German writer Günter Grass.  It has the subtitle "Tales from the Darkroom" ("Dunkelkammergeschichten").  In the narrative, the 80-year-old Grass' eight children, at their father's request, record conversations where they say what they think of him.  "The Box" follows the writer's previous memoir book, "Peeling the Onion" from 2006, which ended in 1959 with the literary success of "The Tin Drum".  It was followed by "Grimm's Words" in 2010.

Question: Who was born first Stephen E. Ambrose or Günter Grass?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "born_first": {
      "type": "string",
      "description": "The name of the person who was born first."
    },
    "comparison_result": {
      "type": "string",
      "description": "Indicates which person was born first based on their birth years."
    }
  },
  "required": [
    "person_a",
    "person_b",
    "born_first",
    "comparison_result"
  ],
  "additionalProperties": false
}
