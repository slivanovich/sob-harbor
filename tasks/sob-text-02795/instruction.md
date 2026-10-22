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
Christina Booth: Christina Maria Booth (born 1965) is a Welsh progressive rock vocalist and singer-songwriter.

Contrast (Conor Maynard album): Contrast is the debut studio album by English pop singer Conor Maynard.  It was released on 30 July 2012 in the United Kingdom through Parlophone and across Europe between August and October.  "Contrast" mainly includes production from The Invisible Men, who produced seven of the fourteen songs available on the album, along with production from Pharrell Williams, Stargate, Benny Blanco, Midi Mafia, Crada, Lucas Secon, Quiz & Larossi, and Eagle Eye, among others, and features guest appearances from American recording artists Ne-Yo and Pharrell Williams, as well as British record artist Rita Ora.

My Name Is My Name: My Name Is My Name is the debut studio album by American hip hop recording artist Pusha T.  It was released on October 8, 2013, by GOOD Music and Def Jam Recordings.  While leading up to the album's announcement, Pusha T released the mixtape "Fear of God" and the EP "" during 2011, along with collaborating on the GOOD Music's compilation album "Cruel Summer" (released in 2012).  In 2013, he also released another mixtape "Wrath of Caine".  The album's production was handled primarily by Kanye West, along with several producers, including Pharrell Williams, The-Dream, Hudson Mohawke, Sebastian Sartor, Don Cannon, Swizz Beatz, Rico Beats, Mano and Nottz, It also features guest appearances from Rick Ross, Young Jeezy, 2 Chainz, Big Sean, Future, Pharrell Williams, Chris Brown and Kendrick Lamar, among others.

Clones (album): The Neptunes Present...Clones is a compilation album produced and released by American production duo The Neptunes (producer-singer Pharrell Williams and producer Chad Hugo).  It was released on August 19, 2003 and has been certified Gold by the RIAA.  The album featured four singles; "Frontin'" by Pharrell Williams, "Light Your Ass on Fire" by Busta Rhymes, "Hot Damn" by Clipse and "It Blows My Mind" by Snoop Dogg.

BET Awards 2014: The 2014 BET Awards were held at the Nokia Theatre L.A. Live in Los Angeles, California on June 29, 2014.  Chris Rock was unveiled as the host for the upcoming BET Awards on May 14 during the network's 106 & Park music video countdown show.  Beyoncé lead the nominations with 6, followed by Jay-Z with 5.  Drake, Pharrell Williams and August Alsina were tied for 4.  Beyoncé was the big winner of the night winning 3 BET Awards, while Nicki Minaj, Drake, August Alsina and Pharrell Williams with 2.

The Voice (U.S. season 8): The eighth season of the American reality talent show "The Voice" premiered on February 23, 2015 on NBC.  Carson Daly returned as host.  Adam Levine, Blake Shelton, and Pharrell Williams returned as coaches.  Gwen Stefani did not return for season eight, making room for the return of Christina Aguilera after a two-season absence.  Sawyer Fredericks, of Team Pharrell, won the competition.

Pharrell Williams: Pharrell Lanscilo Williams ( ; born April 5, 1973), sometimes known as simply Pharrell, is an American rapper, singer, songwriter, record producer, and film producer.

Blurred Lines: "Blurred Lines" is a single written and performed by American recording artists Robin Thicke, T.I., and Pharrell Williams.  Produced by Pharrell, it serves as the lead single from Thicke's album of the same name.  It was released on March 26, 2013 through Pharrell's label Star Trak Recordings.  Recorded in 2012, the song's percussion ideas were primarily inspired by the Marvin Gaye song "Got to Give It Up", and apart from T.I.'s rap, was entirely the work of Williams.  However, Thicke clearly laid claim to writing credits on the track according to a Reuters article.  The song became the subject of a bitter legal dispute with the family of Gaye and Bridgeport Music as to whether the song infringed copyrights to "Got to Give It Up".  Thicke and Williams were found liable for copyright infringement by a federal jury in March 2015, and Gaye was awarded posthumous songwriting credit based on the royalties pledged to his estate.

Sexify: "Sexify" is a song recorded by American singer Leah LaBelle, which was released on May 1, 2012, as part of the sampler album "Pharrell Williams and Jermaine Dupri Present Leah LaBelle" (2012).  Written and produced by Pharrell Williams, it was the first song that LaBelle recorded with Williams as part of a joint record deal with Epic Records, So So Def Recordings, and I Am Other.  It is an R&B song that features throwback elements to 1990s music.  In its lyrics inspired by headlines from the women's fashion magazine "Cosmopolitan", LaBelle instructs a woman on how to draw and keep the attention of a man.

Passion, Pain &amp; Demon Slayin': Passion, Pain & Demon Slayin' is the sixth studio album by American rapper Kid Cudi.  The album was released on December 16, 2016, by Wicked Awesome Records and Republic Records.  It succeeds Cudi's alternative rock album "Speedin' Bullet 2 Heaven" (2015).  The album features guest appearances from André "3000" Benjamin, Pharrell Williams, Travis Scott and Willow Smith.  The production on the album was handled by Cudi himself, alongside Plain Pat, Mike Dean, Dot da Genius, Anthony Kilhoffer, Mike Will Made It and Pharrell Williams, among others.

Question: Who is older - Christina Booth or Pharrell Williams ?

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
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
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
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "older_person_name": {
      "type": "string"
    },
    "age_difference_years": {
      "type": "integer"
    }
  },
  "required": [
    "person_a",
    "person_b",
    "older_person_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
