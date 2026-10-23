{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nManning M. Kimmel: Manning Marius Kimmel (also known as Marius Manning Kimmel, October 25, 1832 – February 27, 1916) was a military officer who served on both sides of the American Civil War.  He entered the United States Military Academy at West Point in 1853 and graduated in 1857.  After initially fighting for the Union, he switched sides to the Confederacy, one of four West Point graduates to fight on both sides during the war.  In the Confederate Army, he served as adjutant general and assistant adjutant general on the staff of generals Benjamin McCulloch and Earl Van Dorn, and as inspector general on John Magruder's staff.  He was the father of Admiral Husband E. Kimmel, who commanded the United States Pacific Fleet during the Attack on Pearl Harbor.\n\nShot by Both Sides: \"Shot by Both Sides\" is a song written by Howard Devoto and Pete Shelley, and performed by the English post-punk band Magazine.  It was released in January 1978 as the band's first single (reaching No. 41 on the UK charts) and appeared a few months later on their debut album, \"Real Life\".\n\nBuddy Burton: W. E. (Buddy) Burton (1890–1976) was a multi-instrumentalist and band leader who appeared on many 1920s Chicago South Side jazz and Blues 78 rpm Phonograph records as vocalist and drummer, and also played washboard, piano, celeste, and kazoo.  He was born in Louisville, Kentucky and went to Chicago around 1922.  He first recorded with Jelly Roll Morton and sessions that were led by Jimmy Blythe.  Burton released five sides under his own name in 1928, six sides with Marcus Norman (as \"Alabama Jim And George\" which some experts have listed as being made with Bob Hudson, although Norman is credited with co-writing), two sides as a duo with Blythe and one with Irene Sanders.  He also backed blues singers Tillie Johnson and Mae Mathews, and played with the Dixie Four and The Harlem Trio.  Other than five numbers in 1929, duets with pianist Bob Hudson in 1932, and the duet with Sanders in 1936, little is known about Burton's life after the mid-thirties although he was probably somewhat active.  It is reported that he died of a self-inflicted gunshot wound.\n\nKite (geometry): In Euclidean geometry, a kite is a quadrilateral whose four sides can be grouped into two pairs of equal-length sides that are adjacent to each other.  In contrast, a parallelogram also has two pairs of equal-length sides, but they are opposite to each other rather than adjacent.  Kite quadrilaterals are named for the wind-blown, flying kites, which often have this shape and which are in turn named for a bird.  Kites are also known as deltoids, but the word \"deltoid\" may also refer to a deltoid curve, an unrelated geometric object.\n\nRegular haircut: A regular haircut is a men's and boys' hairstyle that has hair long enough to comb on top, a defined or deconstructed side part, and a short, semi-short, medium, long, or extra long back and sides.  The style is also known by other names including taper cut, regular taper cut, side-part and standard haircut; as well as short back and sides, business-man cut and professional cut, subject to varying national, regional, and local interpretations of the specific taper for the back and sides.\n\nPythagorean theorem: In mathematics, the Pythagorean theorem, also known as Pythagoras's theorem, is a fundamental relation in Euclidean geometry among the three sides of a right triangle.  It states that the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.  The theorem can be written as an equation relating the lengths of the sides \"a\", \"b\" and \"c\", often called the \"Pythagorean equation\":\n\nPhoenix Shot Tower: The Phoenix Shot Tower, also known as the Old Baltimore Shot Tower, is a red brick shot tower, 234.25 ft tall, located near the downtown, Jonestown (also known later as Old Town), and Little Italy communities of East Baltimore, in Maryland.  When it was completed in 1828 it was the tallest structure in the United States.  The tower was originally known as the \"Phoenix Shot Tower\", then the \"Merchants' Shot Tower\", and now is also sometimes called the \"Old Baltimore Shot Tower\".  It is the only surviving shot tower among three that existed in Baltimore, and was designated a National Historic Landmark on November 11, 1971.\n\nD-beat: D-beat (also known as \"discore\", \"kängpunk\" (Swedish for \"boot-punk\"), and \"discrust\") is a style of hardcore punk, developed in the early 1980s by imitators of Discharge, after whom the genre is named, as well as a drum beat characteristic of this subgenre.  D-beat is known for its \"grinding, distorted and brutally political\" sound.  Discharge may have themselves inherited the beat from Motörhead and the Buzzcocks.  D-beat is closely associated with crust punk, which is a heavier, more complex variation.  The style was particularly popular in Sweden, and developed there by groups such as Crude SS, Anti Cimex, Mob 47 and Driller Killer.  Other D-beat groups include Doom and the Varukers from the UK; Disclose from Japan; Crucifix and Final Conflict from the U.S.; Ratos de Porão, from Brazil; and MG15, from Spain.  While the style initially developed in the early 1980s, a number of new groups working within the subgenre emerged in the mid-1990s.  These include the Swedish groups Wolfbrigade, Totalitär, Avskum, Skitsystem and Disfear.\n\nPete Shelley: Pete Shelley (born Peter Campbell McNeish, 17 April 1955 in Leigh, Lancashire) is an English singer, songwriter and guitarist, best known as the leader of Buzzcocks.\n\nPoint-of-view shot: A point of view shot (also known as POV shot, First-person shot or a subjective camera) is a short film scene that shows what a character (the subject) is looking at (represented through the camera).  It is usually established by being positioned between a shot of a character looking at something, and a shot showing the character's reaction (see shot reverse shot).  The technique of POV is one of the foundations of film editing.\n\nQuestion: What \"Shot by Both Sides\" writter is also known as the leader of Buzzcocks?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"writers\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals who wrote the song.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the writer.\"\n          },\n          \"is_leader_of_buzzcocks\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if this writer is known as the leader of Buzzcocks.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_leader_of_buzzcocks\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the writer who is also the leader of Buzzcocks.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"writers\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "writers": {
        "type": "array",
        "description": "A list of individuals who wrote the song.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the writer."
            },
            "is_leader_of_buzzcocks": {
              "type": "boolean",
              "description": "Indicates if this writer is known as the leader of Buzzcocks."
            }
          },
          "required": [
            "name",
            "is_leader_of_buzzcocks"
          ],
          "additionalProperties": false
        }
      },
      "answer": {
        "type": "string",
        "description": "The name of the writer who is also the leader of Buzzcocks."
      }
    },
    "required": [
      "song_title",
      "writers",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
