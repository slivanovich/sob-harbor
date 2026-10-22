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
Curley McDimple: Curley McDimple is a musical with music and lyrics by Robert Dahdah and book by Robert Dahdah and Mary Boylan.  The play is a spoof of Depression-era Shirley Temple movies and was presented in a black and white design.  This was one of two musicals in which Bernadette Peters appeared that spoofed some aspect of Hollywood—the other was "Dames at Sea". " "The Meanest Man in Town"" is its best-known song.

Eddie &quot;Rochester&quot; Anderson: Edmund Lincoln Anderson (September 18, 1905 – February 28, 1977) was an American comedian and actor.

Kenne Duncan: Kenne Duncan (February 17, 1903 – February 5, 1972) was a Canadian-born B-movie character actor.  Hyped professionally as "The Meanest Man in the Movies," the vast majority of his over 250 appearances on camera were Westerns, but he also did occasional forays into horror, crime drama, and science fiction.  He also appeared in over a dozen serials.

The Jim Yoshii Pile-Up: The Jim Yoshii Pile-Up is a 5 piece band formed in 1997 in Oakland, California.  Named after a high school friend of the band, their highly textured sound spans the range from indie to post-rock.  They have released three full lengths on Absolutely Kosher Records.  As of 2006, the band is on hiatus.  Paul Gonzenbach is currently releasing albums under his own name.  Noah Blumberg is in the duo Meanest Man Contest.

Ed Sprinkle: Edward Alexander Sprinkle (September 3, 1923 – July 28, 2014) was an American football player.  He was known to many as "The Meanest Man in Pro Football" and was nicknamed "The Claw."  He played for 12 seasons with the Chicago Bears of the National Football League and is credited with calling attention to the NFL's defensive players.  Bears coach George Halas referred to Sprinkle as "the greatest pass-rusher I've ever seen" and "a rough, tough ballplayer, but not a dirty one."  At first he played on both defense and offense.  He caught 32 passes for 451 yards and seven touchdowns during his career.  His ability to rush opposing quarterbacks, however, soon made him a defensive specialist Earning 4 Pro Bowls.  While accused of "dirty play" and unsportsman-like conduct during his career, Sprinkle claimed that his aggressive play was similar to that found all over the NFL throughout the 1950s.  According to Sprinkle, "We were meaner in the 1950s because there were fewer positions and we fought harder for them.  It was a different era."

The Meanest Man in the World: The Meanest Man in the World is a 1943 film directed by Sidney Lanfield, starring Jack Benny and Priscilla Lane, based upon a play that starred George M. Cohan, who produced it on Broadway and released by 20th Century Fox.  The supporting cast features Eddie "Rochester" Anderson, Edmund Gwenn and Anne Revere.  The picture's screenplay was written by George Seaton and Allan House.  The plotline involves a kind lawyer (Benny) who pretends to be mean in order to further his career, which has the unforeseen repercussion of placing his romance with Lane's character in serious jeopardy.

Joseph Kirkland: Joseph Kirkland (January 7, 1830 - April 29, 1894) was an American novelist.  Born in Geneva, New York, to educator William Kirkland and author Caroline Kirkland, he was a businessman in Chicago, then served in the Union Army during the Civil War, reaching the rank of major.  He resigned his Union Army commission and moved to Tilton, Illinois, where he married Theodosia B. Wilkinson in 1863.  In 1864 he founded the Midwestern literary periodical "Prairie Chicken".  After the war he became a lawyer while also pursuing writing.  He is best remembered as the author of two realistic novels of pioneer life in the Far West, "Zury: The Meanest Man in Spring County (1887)" and "The McVeys".  Other works are "The Captain of Company K" and "The Story of Chicago".  He was also the literary editor of the "Chicago Tribune".  Kirkland died in Chicago at the age of 64.

Clyde Thompson: Clyde Thompson (born in 1910) was an American prisoner turned chaplain.  He is most noted for being cited and labeled as The Meanest Man in Texas.

Meanest Man Contest: Meanest Man Contest is a hip hop and electronic music duo based in San Francisco, California.  The members are Quarterbar (Noah Blumberg) and Eriksolo (Eric Steuer).

Albert J. Adams: Albert J. Adams (1845 – October 1, 1906) was known as The Policy King and the Meanest Man in New York.  He ran the numbers game in New York City from around 1890 to around 1905.

Question: The Meanest Man in the World featured the comedian and actor of what nationality in the supporting role?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor in the supporting role."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role the actor played in the film."
        }
      },
      "required": [
        "actor_name",
        "nationality",
        "role_type"
      ],
      "additionalProperties": false
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "film_title",
    "actor_details",
    "film_year"
  ],
  "additionalProperties": false
}
