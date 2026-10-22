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
Chen Kenichi: Chen Kenichi (陳建一 , Chin Ken'ichi , , born January 5, 1956 in Tokyo, Japan) , whose name is often romanized Chin Kenichi in Japanese sources, is a chef best known for his role as the Iron Chef Chinese on the television series "Iron Chef".  Nicknamed ""The Szechuan Sage"", he wears a yellow outfit and rises into Kitchen Stadium holding a cleaver in his hand.  He is the only Iron Chef to have held his position throughout the life of the show.  He was born in Japan to ethnic Han Chinese father of Japanese nationality and a Japanese mother and his formal name is Ken'ichi Azuma (東 建一 , Azuma Ken'ichi ) .

Dark Empire: Dark Empire is a "Star Wars" comic book metaseries produced by Dark Horse Comics.  It consists of a six-issue limited series written by Tom Veitch and drawn by Cam Kennedy ("Dark Empire I"), followed by a second six-issue limited series by Veitch and Kennedy ("Dark Empire II") and a two-issue limited series written by Veitch and drawn by Jim Baikie ("Empire's End").  "Dark Empire" in particular, is notable for being one of the very first Star Wars comics to be produced by Dark Horse Comics, who had acquired the comic rights to the Star Wars franchise in the early 1990s.

Tough (manga): Kōkō Tekken-den Tough (Japanese: 高校鉄拳伝タフ , literally "High School Iron Fist Legend Tough") , is a martial arts manga series written and illustrated by Tetsuya Saruwatari.  A sequel series, titled simply as Tough (TOUGH—タフ— , Tafu ) was introduced in 2004 which continues the story further after the first series ended its run.  The third series, Tough Gaiden : Ryu wo Tsugu Otoko (Japanese: TOUGH外伝 龍を継ぐ男 , literally "Tough Side Story : The Man Who Inherits The Dragon") , starring one of illegitimate children of Kiryu Miyazawa, has been serialized in Shueisha's Weekly Playboy since December 21, 2015.  A spin-off series, "Oton" (おとん ) , has been serialized in "Business Jump" since 2004.

Julie Kagawa: Julie Kagawa (born October 12, 1982) is an American author, best known for writing The Iron Fey Series consisting of four books: "The Iron King", "The Iron Daughter", "The Iron Queen", and "The Iron Knight".

The Dragons of Babel: The Dragons of Babel is a 2008 novel by American author Michael Swanwick, set in the same world as his earlier work "The Iron Dragon's Daughter" (1993).  It follows the plight of a young man named Will Le Fey after a crippled dragon takes up residence in his town and inside his mind.  Like "The Iron Dragon's Daughter", the novel subverts fantasy tropes while it explores the extremely dark and gritty world of Faerie.

The Invincible Iron Man: The Invincible Iron Man is an Eisner Award-winning comic book series written by Matt Fraction with art by Salvador Larroca, published by Marvel Comics and starring the superhero Iron Man.  After issue #33 The Invincible Iron Man returned to its original numbering with issue #500.  It concluded with issue 527, succeeded by the "Marvel NOW!" -imprinted "Iron Man" series.

The Iron Trial: The Iron Trial is a children's novel of The Magisterium Series written by Holly Black and Cassandra Clare.  The protagonist of the series is twelve-year-old Callum (Call) Hunt who was raised by the mage Alastair Hunt, who after the third mage war with 'The Enemy of Death' also known as Constantine Madden, and the death of his wife Sarah at the Cold Massacre, decided to spurn magic and raised up Call to be the same.  In the first book "The Iron Trial"' Call participates in a test to see whether he has sufficient magic to attend the magisterium and train to be a mage using the four elements fire, air, water, earth.

Cooter (30 Rock): "Cooter" is the fifteenth episode of the second season of "30 Rock" and the thirty-sixth episode of the series.  It was written by series' creator Tina Fey and was directed by one of the season's producers, Don Scardino.  The episode first aired on May 8, 2008, on the NBC network in the United States.  "Cooter" follows Jack Donaghy's (Alec Baldwin) attempt to get fired from his new job in politics; Liz Lemon's (Fey) pregnancy scare and decision to adopt a baby; Tracy Jordan's (Tracy Morgan) creation of a pornographic video game; and Kenneth Parcell's (Jack McBrayer) aspiration to be an NBC page at the Beijing Olympics.  The episode is an unofficial season finale, due to the season being shortened by the 2007–2008 Writers Guild of America strike.

The Iron Fey Series: 'The Iron Fey' is a book series written by Julie Kagawa, a New York Times and International Bestselling Author.  This series follows Meghan Chase, a girl who finds herself drawn into the world of the Fey, including characters from William Shakespeare's A Midsummer Night's Dream.  The books series was published by Harlequin Teen 2010-2012, including several short stories tying into the main four books in the series.  There is a spin-off series, Trilogy

30 Rock: 30 Rock is an American satirical television sitcom created by Tina Fey that ran on NBC from October 11, 2006, to January 31, 2013.  The series, loosely based on Fey's experiences as head writer for "Saturday Night Live", takes place behind the scenes of a fictional live sketch comedy show depicted as airing on NBC.  The series's name refers to 30 Rockefeller Plaza in New York City, the address of the Comcast Building, where the NBC Studios are located and where "Saturday Night Live" is written, produced, and performed.  This series is produced by Broadway Video and Little Stranger, Inc., in association with NBCUniversal.

Question: The Iron Fey is a series written by the author of what nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the book series."
    },
    "author_nationality": {
      "type": "string",
      "description": "The nationality of the author."
    },
    "author_birth_year": {
      "type": "integer",
      "description": "The birth year of the author."
    }
  },
  "required": [
    "author_name",
    "series_name",
    "author_nationality",
    "author_birth_year"
  ],
  "additionalProperties": false
}
