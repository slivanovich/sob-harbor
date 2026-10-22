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
Chelsea Dagger: "Chelsea Dagger" is a song by Scottish rock band The Fratellis.  It was released as the second single from their debut studio album, "Costello Music" (2006), on 28 August 2006.  It is named after Jon Fratelli's wife Heather, a burlesque dancer whose stage name – a play on Britney Spears – he borrowed for the song.  Fratelli described the tune as "a rock 'n' roll gig in an old speakeasy or something like that."

The Fratellis: The Fratellis are a Scottish rock band from Glasgow, formed in 2005.  The band consists of lead vocalist and guitarist Jon Fratelli (born John Lawler), bass guitarist Barry Fratelli (born Barry Wallace), and drummer and backing vocalist Mince Fratelli (born Gordon McRory).  Their singles "Chelsea Dagger" and "Whistle for the Choir" were both top ten hits in the UK charts.

Lars K. Hustoft: Lars has co-written and A&R´ed several hits (most of which he has also produced or co-produced) in Norway/Europe, including "Ring meg" / "Regn fra blå himmel" / "Bordet" by Gabrielle, "Closer" by Frida Amundsen and "Shattered" by Astrid Smeplass (Astrid S).  In 2012, Hustoft worked with Morten Harket of A-ha on his solo album "Out of My Hands".  They wrote the title song "Out of My Hands" together in Lars´ studio in Los Angeles.

Snorre Bjerck: Snorre Bjartmann Bjerck (born 25 February 1962 in Florø, Norway) is a Norwegian, jazz musician (percussion and vocals).  He has played in bands like "First Set", Jon Balke's Batagraf, and the sami band Transjoik. , and is otherwise known from recordings and performances with the likes of Morten Harket, Sissel Kyrkjebø, Mari Boine, Nils Petter Molvær, Bjørn Eidsvåg, Sigvart Dagsland, Frode Alnæs, Eivind Aarset, Annbjørg Lien, Arve Henriksen, Nils-Olav Johansen, and Tim Whelan (Trans Global Underground, England)

Love Is a Beautiful Thing (Phil Vassar song): "It's a Beautiful Thing", also known as "Love Is a Beautiful Thing", is a country music song co-written by American songwriters Jeffrey Steele and Craig Wiseman.  The first version of this song was released on September 14, 1999 (Morten Harket's 40th birthday) by Canadian singer Paul Brandt from his 1999 album "That's the Truth", from which it was released as a single in both Canada and the United States.  Eight years later, American singer Phil Vassar covered the song under the title "Love Is a Beautiful Thing" on his album "Prayer of a Common Man".  Vassar's version reached its peak of #2 on the "Billboard" Hot Country Songs charts in mid-2008.

Wild Seed (album): Wild Seed is the second studio album and first English-language album by Norwegian pop singer Morten Harket.  The album was released on 4 September 1995 through Warner Bros.  Records.  After a-ha went on a hiatus in 1994, Harket began recording "Wild Seed" with British record producer Christopher Neil, who previously worked with the band on their fourth studio album, "East of the Sun, West of the Moon" (1990).  "Wild Seed" charted at number one in Norway and at number 89 in the United Kingdom.  It has since sold 160.000 copies in Norway.

Morten Harket: Morten Harket (born 14 September 1960) is a Norwegian musician, best known as the lead singer of the synthpop/rock band A-ha, which released ten studio albums and topped the charts internationally after their breakthrough hit "Take on Me" in 1985.  A-ha disbanded in 2010 after they played their last gig in Oslo.  In 2015, after each member pursued his own artistic path, a-ha reunited to produce a new album, "Cast In Steel", and perform a world tour, kicking off at Rock in Rio in Rio de Janeiro, Brazil on 27 September 2015.  Harket has also released six solo albums.  Before joining A-ha in 1982, Harket had appeared on the Oslo club scene as the singer for blues outfit Souldier Blue.

Jon Fratelli: Jon Fratelli (born John Paul Lawler, 4 March 1979, Glasgow, Scotland) is a Scottish musician and songwriter best known for his work with the band The Fratellis.  He has also played in a band called Codeine Velvet Club, and also performed as a solo artist.

Frode Alnæs: Frode Alnæs (born 3 March 1959 in Kristiansund, Norway) is a Norwegian jazz guitarist and composer, known from cooperation with international artists like Morten Harket, Magne Furuholmen, Arild Andersen, Jon Balke, Ole Edvard Antonsen, Ketil Bjørnstad, Henning Sommerro, Ray Charles, Dee Dee Bridgewater, Ian Hunter, Bjørn Alterhaug, Sissel Kyrkjebø, Gustav Lorentzen, and Jan Erik Vold, and appearances in bands like Dance with a Stranger, Masqualero, Jazzpønkensemblet, and Sidsel Endresen Quartet.

Eurovision Song Contest 1996: The Eurovision Song Contest 1996 was the 41st Eurovision Song Contest and was held on 18 May 1996 in Oslo Spektrum in Oslo, Norway.  The presenters were Ingvild Bryn and Morten Harket.  Harket, lead singer of a-ha, opened the show with a performance of his single "Heaven's Not for Saints", which was a smash hit in Norway at the time.  Twenty-three countries participated in the contest, with Eimear Quinn of Ireland crowned the winner after the final voting, with the song, "The Voice".  The song was written by Brendan Graham, who also composed the 1994 winner "Rock 'n' Roll Kids".  It was also a record seventh win for Ireland and the most recent win of Ireland.

Question: Jon Fratelli and Morten Harket, have which occupation in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual and their stated occupations.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations for the individual as stated in the context."
          }
        },
        "required": [
          "name",
          "occupations"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the common occupation was identified."
    }
  },
  "required": [
    "common_occupation",
    "individuals",
    "reasoning"
  ],
  "additionalProperties": false
}
