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
To Tulsa and Back: To Tulsa and Back is a 2004 album by J. J. Cale.  The song "These Blues" was used on an episode of "Dog the Bounty Hunter".

Eusèbe Jaojoby: Eusèbe Jaojoby (born 29 July 1955), commonly known by his surname Jaojoby ] , is a Malagasy composer and singer of "salegy", a musical style of northwestern Madagascar.  Critics consider him to be one of the originators of the modern salegy style that emerged in the 1970s, and credit him with transforming the genre from an obscure regional musical tradition into one of national and international popularity.  Jaojoby also contributed to the creation of two salegy subgenres, "malessa" and "baoenjy".  Jaojoby has been called the most popular singer in Madagascar and the Indian Ocean islands, and is widely referred to as the "King of Salegy".  His success has earned him such honors as Artist of the Year in Madagascar for two consecutive years (1998–1999) and the role of Goodwill Ambassador for the United Nations Population Fund in 1999.

William Wadé Harris: William Wadé Harris (c. 1860 – 1929) was a Liberian Grebo evangelist, who preached in Liberia, Côte d'Ivoire and Ghana.  He has been described as the "most extraordinary one man evangelical crusade that Africa has ever known" and is considered one of the originators of today's prosperity gospel.

Genre painting: Genre painting, also called genre scene or petit genre, depicts aspects of everyday life by portraying ordinary people engaged in common activities.  One common definition of a genre scene is that it shows figures to whom no identity can be attached either individually or collectively—thus distinguishing "petit genre" from history paintings (also called "grand genre") and portraits.  A work would often be considered as a genre work even if it could be shown that the artist had used a known person—a member of his family, say—as a model.  In this case it would depend on whether the work was likely to have been intended by the artist to be perceived as a portrait—sometimes a subjective question.  The depictions can be realistic, imagined, or romanticized by the artist.  Because of their familiar and frequently sentimental subject matter, genre paintings have often proven popular with the bourgeoisie, or middle class.

Manuel Perez (musician): Emanuel "Manuel" Perez (28 December 1871 – 1946) was an early New Orleans jazz cornetist and bandleader.  Being a contemporary of Buddy Bolden, Perez is considered one of the originators, and was influential in crafting the early jazz and ragtime sound.

Jon Hendricks: Jon Hendricks (born September 16, 1921) is an American jazz lyricist and singer.  He is considered one of the originators of vocalese, which adds lyrics to existing instrumental songs and replaces many instruments with vocalists (such as the big-band arrangements of Duke Ellington and Count Basie).  Furthermore, he is considered one of the best practitioners of scat singing, which involves vocal jazz soloing.  For his work as a lyricist, jazz critic and historian Leonard Feather called him the "Poet Laureate of Jazz", while "Time" dubbed him the "James Joyce of Jive".  Al Jarreau called him "pound-for-pound the best jazz singer on the planet—maybe that's ever been".

Benjamin G. Wilkinson: Benjamin George Wilkinson (1872–1968) was a Seventh-day Adventist missionary, educator, theologian and considered one of the originators of the King James Only beliefs.  He was also the Dean of Theology at the Seventh-day Adventist Washington Missionary College (now known as Washington Adventist University) which is located in Takoma Park, Maryland, near Washington, D.C.

Susarion: Susarion (Greek: Σουσαρίων) was an Archaic Greek comic poet, was a native of Tripodiscus in Megaris (see Megara) and is considered one of the originators of metrical comedy and, by others, he was considered the founder of Attic Comedy.  Nothing of his work, however, survives except one iambic fragment (see below) and this is not from a comedy but instead seems to belong within the Iambus tradition.

Tulsa race riot: The Tulsa race riot, or Tulsa race riot of 1921, occurred between May 31 and June 1, 1921, when a white mob started attacking residents and businesses of the African-American community of Greenwood in Tulsa, Oklahoma, in what is considered one of the worst incidents of racial violence in the history of the United States.  The attack, carried out on the ground and by air, destroyed more than 35 blocks of the district, at the time the wealthiest black community in the nation.  More than 800 people were admitted to hospitals and more than 6,000 black residents were arrested and detained, many for several days.  The Oklahoma Bureau of Vital Statistics officially recorded 39 dead, but the American Red Cross estimated 300, a number supported by historians since then.

J. J. Cale: John Weldon "J. J." Cale (December 5, 1938 – July 26, 2013) was an American guitarist, singer, and songwriter.  Though he deliberately avoided the limelight his influence as a musical artist has been widely acknowledged by figures such as Mark Knopfler, Neil Young, and Eric Clapton, who described him as "one of the most important artists in the history of rock".  He is considered to be one of the originators of The Tulsa Sound, a loose genre drawing on blues, rockabilly, country, and jazz.

Question: To Tulsa and Back is by an artist who is considered one of the originators of what genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who created the album."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the question."
    },
    "genre_originated": {
      "type": "string",
      "description": "The musical genre the artist is considered an originator of."
    },
    "genre_influences": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Musical styles that the genre draws upon."
    }
  },
  "required": [
    "artist_name",
    "album_name",
    "genre_originated"
  ],
  "additionalProperties": false
}
