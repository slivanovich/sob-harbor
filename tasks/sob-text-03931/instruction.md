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
The Gap Band: The Gap Band was an American R&B and funk band which rose to fame during the 1970s and 1980s.  With the nucleus consisting of brothers Charlie, Ronnie, and Robert Wilson.  The band is named after streets (Greenwood, Archer, and Pine) in the historic Greenwood neighborhood in their hometown of Tulsa, Oklahoma.  The group shortened its name to "The Gap Band" in 1973.  After 43 years together, they retired in 2010.

Genocide Superstars: Genocide Superstars (often referred to as or shortened to Genocide SS) was a Swedish hardcore punk, rock n' roll band.  The band was formed in 1994 in Örebro, Sweden.  The lyrics, themes and surrounding artwork tended to revolve around subjects such as violence, totalitarianism, alcohol use, women and motorcycles.  Despite the name, the band had nothing to do with national socialism, and never approved of such opinions.  As the members were veteran parts of the 90's crust/hardcore movement in Sweden, chance is the opposite is true; rather than having right-wing sympathies, they were strongly against it.

1973 CECAFA Cup: The 1973 CECAFA Cup was the inaugural edition of the CECAFA Cup, and was held in Uganda.  The CECAFA Cup is considered Africa's oldest football tournament, and involves teams from Central and Southern Africa.  The matches in the 1973 tournament were played from 22 September 1973 until 29 September 1973.  The tournament was originally the Gossage Cup, contested by the four nations of Kenya, Uganda, Tanzania, and Zanzibar, running from 1929 until 1965.  In 1967, this became the East and Central African Senior Challenge Cup, often shortened to simply the Challenge Cup, which was competed for five years, until 1971, before the CECAFA Cup was introduced in 1973.  Uganda, the hosts, won the Cup, beating Tanzania 2–1 in the final.  The tournament lacked a third-place play-off, so the runners-up in the group stages, Kenya and Zambia, shared third place.  After Uganda and Zambia drew in the group stages with the same number of points, goals conceded and goals scored, a play-off occurred, which Uganda won.  The tournament has been expanded, and the modern-day tournament consists of 12 different teams (Ethiopia, South Sudan, Burundi, Rwanda, Sudan, and Eritrea have joined since 1973).

The Whirling Dervishes (band): Whirling Dervishes are an American alternative rock band from Westfield, New Jersey.  Formed in 1981 initially as Johnny Bravo and his Whirling Dervishes, the band shortened its name in 1983 to Whirling Dervishes.  Their sound has been described as a combination of Roxy Music, The Stooges, Nine Inch Nails and The Wonderstuff.

True Ingredients: True Ingredients are a British Hip Hop band based in London, UK.  The group is composed of Vocalists - Mr. Milk, Aina, Mireilla Sings, Angela, Keyboards - Fenna, Guitar/Bass - Millzy & Drums - Steve O'Gallagher.  Their records also feature guest vocals from BluRum13, Natty, and Mr. Basista who occasionally perform with the band at their live shows.  The band has played gigs all over the UK as well as in many other European countries alongside a number of high-profile artists such as DJ Vadim, Finley Quaye, Kele Le Roc, Jungle Brothers, Aquasky, Foreign Beggars, High Contrast, Bugz in the Attic, and The Gap Band who feature as the brass section on True Ingredients' single "Who's Next?" .  The band released their debut album "Prepare & Assemble" in the form of album sunglasses.  They are the first artist to ever release an album in this format.

Kyuss: Kyuss ( ) was an American rock band, formed in Palm Desert, California, in 1987 by Josh Homme (guitar), John Garcia (vocals), Brant Bjork (drums) and Chris Cockrell (bass).  After releasing an EP under the name Sons of Kyuss in 1990, the band shortened its name to Kyuss and recruited Nick Oliveri, replacing Cockrell as bassist.  Over the next five years the band released four full-length albums, and one last split EP in 1997 as Kyuss and the newly formed Queens of the Stone Age.  This tied up the loose ends of Kyuss and introduced the new band Queens of the Stone Age, which was initially composed entirely of former Kyuss members.

Sons of Kyuss (EP): Sons of Kyuss is the debut EP by American rock band Kyuss, released in 1990 under the group's original name, Sons of Kyuss.  The band released it independently as a vinyl record, pressing only 500 copies.  Following this release, the band shortened its name to Kyuss and included these recordings of the songs "Deadly Kiss" and "Black Widow" on their first full-length album, "Wretch" (1991), while re-recording "Love Has Passed Me By", "Katzenjammer", and "Isolation Desolation" for the album (the latter song's title was shortened to "Isolation").

Between Heaven 'n Hell: Between Heaven 'N Hell is the seventh studio album, from American Christian rock band Resurrection Band, released in 1985.  This is the first album on which Resurrection Band shortened its moniker to "REZ," and it also marks the band's final album for Sparrow Records.

Kinohimitsu: Kinohimitsu (木の秘密 , Kinohimitsu ) is a functional beauty and health brand owned by Kino Biotech, a leading integrated bio-nutraceutical and cosmeceutical public listed company in the Taiwan`s GreTai Securities Market (GTSM) with its head office in Singapore.  According to Euromonitor International, Kinohimitsu was the top selling beauty drink and collagen drink in Malaysia and Singapore between 2008 and 2010.  The brand name, (木の秘密) means the secret of Nature.  The brand name stays true to the company’s practices in using natural ingredients in its products.

Steve Miller Band: The Steve Miller Band is an American rock band formed in 1966 in San Francisco, California.  The band is led by Steve Miller on guitar and lead vocals.  It is best known today for a string of (mainly) mid-1970s hit singles that are staples of classic rock radio, as well as several earlier acid rock albums.  Miller left his first band to move to San Francisco and form the Steve Miller Blues Band.  Shortly after Harvey Kornspan negotiated the band’s landmark contract with Capitol Records in 1967, the band shortened its name to the Steve Miller Band.  In February 1968, the band recorded its debut album, "Children of the Future".  It went on to produce the albums "Sailor", "Brave New World", "Your Saving Grace", "Number 5", "Rock Love" and more.  The band's "Greatest Hits 1974–78", released in 1978, sold over 13 million copies.  The band continued to produce more albums and in 2014 toured with the rock band Journey.  In 2016, Steve Miller was inducted as a solo artist in the Rock and Roll Hall of Fame.

Question: Which band shortened its name in 1973 and played with True Ingredients?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that meets the criteria."
    },
    "year_name_shortened": {
      "type": "integer",
      "description": "The year the band shortened its name."
    },
    "collaborated_with_true_ingredients": {
      "type": "boolean",
      "description": "Indicates if the band collaborated with True Ingredients."
    },
    "collaboration_description": {
      "type": "string",
      "description": "Details about the collaboration with True Ingredients."
    }
  },
  "required": [
    "band_name",
    "year_name_shortened",
    "collaborated_with_true_ingredients",
    "collaboration_description"
  ],
  "additionalProperties": false
}
