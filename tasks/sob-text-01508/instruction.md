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
Tom and Huck: Tom and Huck is a 1995 American adventure comedy-drama film based on Mark Twain's novel "The Adventures of Tom Sawyer", and starring Jonathan Taylor Thomas, Brad Renfro, Mike McShane, and Amy Wright.  The film was directed by Peter Hewitt and produced/co-written by Stephen Sommers (who also worked on another Disney adaptation of Twain's work, 1993's "The Adventures of Huck Finn").  The movie was released in the U.S. and Canada on December 22, 1995.

Piglet's Big Game: Disney's Piglet's Big Game is a 2003 action-adventure video game by Gotham Games, Disney Interactive Studios and Doki Denki Studio.  The game centers around Piglet and how he tries to show how he can help.  The game is based on "Piglet's Big Movie".

Tom Sawyer, Detective: Tom Sawyer, Detective is an 1896 novel by Mark Twain.  It is a sequel to "The Adventures of Tom Sawyer" (1876), "Adventures of Huckleberry Finn" (1884), and "Tom Sawyer Abroad" (1894).  Tom Sawyer attempts to solve a mysterious murder in this burlesque of the immensely popular detective novels of the time.  Like "Adventures of Huckleberry Finn", the story is told using the first-person narrative voice of Huck Finn.

Huck Finn Jubilee: The Huck Finn Jubilee Bluegrass Music Festival or simply The Huck Finn Jubilee is an annual three-day bluegrass event held in Ontario, California.  It is held during the second weekend in June at the Cucamonga-Guasti Regional Park and features RV and tent camping, traditional "Americana" activities, and live bluegrass music.  The festival also features activities, such as greased pole climbing, tomahawk throwing, pie eating, river rafting, and arts and crafts.  The event is also the West Coast’s biggest bluegrass festival, with acts such as The String Cheese Incident, Ralph Stanley, Steve Martin & the Steep Canyon Rangers, and Rhonda Vincent.  On September 30, 2016 the Greater Ontario Convention & Visitors Bureau announced that 2016 would be the last festival sponsored by it at the Cucamonga-Guasti Regional Park.

The Adventures of Huck Finn (1993 film): The Adventures of Huck Finn is a 1993 American adventure film written and directed by Stephen Sommers, distributed by Walt Disney Studios Motion Pictures and Buena Vista Pictures, and starring Elijah Wood, Courtney B. Vance, Jason Robards and Robbie Coltrane; it is based on Mark Twain's novel "Adventures of Huckleberry Finn" and focuses on at least three-fourths of the book.  The film follows a boy named Huckleberry Finn and an escaped slave named Jim, who travel the Mississippi River together and overcome various obstacles along the way.

Shohola Falls: Shohola Falls is a 2003 novel written by Michael Pearson.  The novel imagines the true story of Thomas Blankenship, the young man that Mark Twain reputedly based the character of Huck Finn upon in his novel Adventures of Huckleberry Finn.  In "Shohola Falls", Mark Twain is set as an important character, the fictional reality aligned to the historical one.

Huck Finn's Playland: Huck Finn’s Playland is an amusement park located on the grounds of Huck Finn’s Warehouse furniture store in Albany, New York.  It first opened in 2015 in response to Hoffman's Playland, the amusement park where all of the rides used to be, closed at that time.

The New Adventures of Huckleberry Finn: The New Adventures of Huckleberry Finn is an American live-action and animated television series that originally aired on NBC from September 15, 1968 through February 23, 1969.  Produced by Hanna-Barbera and based on the classic Mark Twain characters, the program starred its three live-action heroes, Huck Finn (Michael Shea), Becky Thatcher (LuAnn Haslam), and Tom Sawyer (Kevin Schultz), navigating weekly adventures within an animated world as they attempted to outrun a vengeful "Injun Joe" (voiced by Ted Cassidy).  After the show's original run, the series continued to air in reruns as part of "The Banana Splits and Friends Show" syndication package.

Piglet's Big Movie: Piglet's Big Movie is a 2003 American animated musical comedy-drama adventure film produced by Walt Disney Feature Animation and animated by Walt Disney Animation (Japan).  It was released by Walt Disney Pictures on March 21, 2003.  The film is based upon the characters in the "Winnie-the-Pooh" books written by A. A. Milne.  It is the second in a recent series of theatrically released "Winnie the Pooh" films, preceded by "The Tigger Movie" (2000) and followed by "Pooh's Heffalump Movie" (2005).  In the film, Piglet is ashamed of being small and wanders off into the Hundred Acre Woods, leading his friends to form a search party to find him.

Huckleberry no Bōken: Huckleberry no Bōken (ハックルベリィの冒険 ) is a 1976 anime series based on the novel "Adventures of Huckleberry Finn" by Mark Twain.  It is the first of two Huckleberry Finn anime.  A second Huck Finn television series was made in 1994, "Huckleberry Finn Monogatari".

Question: Were The Adventures of Huck Finn and Piglet's Big Movie distributed by the same studio?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "boolean",
      "description": "True if the entities were distributed by the same studio, false otherwise."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Title of the first entity."
        },
        "distributors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of distributors for the first entity."
        }
      },
      "required": [
        "title",
        "distributors"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Title of the second entity."
        },
        "distributors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of distributors for the second entity."
        }
      },
      "required": [
        "title",
        "distributors"
      ],
      "additionalProperties": false
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of the comparison result based on the distributors identified."
    }
  },
  "required": [
    "comparison_result",
    "entity_1",
    "entity_2",
    "reasoning"
  ],
  "additionalProperties": false
}
