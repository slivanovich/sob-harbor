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
Jimmy Boyd: Jimmy Devon Boyd (January 9, 1939 – March 7, 2009) was an American singer, musician, and actor known for his recording of the song "I Saw Mommy Kissing Santa Claus".

Dylan and Cole Sprouse: Dylan Thomas Sprouse and Cole Mitchell Sprouse (born August 4, 1992) are American actors.  They are twins and are referred to as the Sprouse brothers or Sprouse Bros.  Their first major theatrical film role was in the 1999 comedy, "Big Daddy", in which they co-starred with Adam Sandler.  They later appeared in several television sitcoms and starred in the straight-to-DVD films "I Saw Mommy Kissing Santa Claus" and "Just for Kicks".

Santa Claus Is a Black Man: "Santa Claus Is a Black Man" is a Christmas song by record producer and songwriter Teddy Vann, performed by his daughter Akim Vann (billed as Akim) and his Teddy Vann Production Company for a 1973 single.  The song, described as "Vann's take on 'I Saw Mommy Kissing Santa Claus'", has been called a cult classic, and continues to receive Christmas airplay.

The Two Little Bears: The Two Little Bears is a 1961 American comedy film directed by Randall Hood and written by George W. George.  The film stars Eddie Albert, Jane Wyatt, Soupy Sales, Butch Patrick, Donnie Carter and Jimmy Boyd.  The film was released on November 1, 1961, by 20th Century Fox.

Jackson 5 Christmas Album: Jackson 5 Christmas Album was the fourth studio album (and only holiday album) by Motown family quintet The Jackson 5, released in October 1970.  Included on the "Christmas Album" is the Jackson 5's hit single version of "Santa Claus Is Coming to Town".  The Jackson 5's versions of "I Saw Mommy Kissing Santa Claus" and "Santa Claus Is Coming to Town" remain frequent radio requests during the Christmas season .  The album spent all four weeks at the number one position on "Billboard" magazine's special Christmas Albums chart that the magazine published in December 1970, making it the best-selling Christmas album of that year.  It has sold over 3.5 million copies worldwide.

I Saw Mommy Kissing Santa Claus (film): I Saw Mommy Kissing Santa Claus is a 2001 made-for-TV family film, based on the classic holiday song of the same name.  The movie's tagline was "Christmas is coming, and Santa's a dirty rat."  "I Saw Mommy Kissing Santa Claus" first aired December 9, 2001, on the PAX Network where it aired until 2007.  As of 2008, it is shown in the 25 Days of Christmas programming block on Freeform.

Molly Bee: Molly Bee (August 18, 1939 – February 7, 2009), born Mollie Gene Beachboard, was an American country music singer famous for her 1952 recording of the early perennial, "I Saw Mommy Kissing Santa Claus", and as Pinky Lee's sidekick on "The Pinky Lee Show".

Tommie Connor: Thomas Patrick "Tommie" Connor (16 November 1904 – 28 November 1993) was an English songwriter, credited with several hit songs over his long career.  Most notable among these was "I Saw Mommy Kissing Santa Claus", which has been recorded by many artists and is among the most-played Christmas songs played on American radio.  This was one of several non-religious Christmas songs that he wrote, others being "The Little Boy that Santa Claus Forgot" and "I'm Sending a Letter to Santa".

Merry Christmas for You: Merry Christmas For You is a Yuki Uchida's Christmas-themed mini-album, released in Japan on 1995/11/22 on King Records label (reference: KICS-530).  It charted n°19 on Oricon charts.  It contains six songs (and a message), including two cover of American songs : "Mama ga Santa ni Kiss wo Shita", a cover of Jimmy Boyd's "I Saw Mommy Kissing Santa Claus", and "Akahana no Tonakai", a cover of Harry Brannon's "Rudolph the Red-Nosed Reindeer".

I Saw Mommy Kissing Santa Claus: "I Saw Mommy Kissing Santa Claus" is a Christmas song with music and lyrics by British songwriter Tommie Connor.

Question: What film did the singer of "I Saw Mommy Kissing Santa Claus" star in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the singer."
        },
        "known_for_song": {
          "type": "string",
          "description": "The title of the song the singer is known for."
        }
      },
      "required": [
        "name",
        "known_for_song"
      ],
      "additionalProperties": false
    },
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the singer starred in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "director",
        "genre"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of the relationship between the singer and the film."
    }
  },
  "required": [
    "singer",
    "film",
    "relationship_description"
  ],
  "additionalProperties": false
}
